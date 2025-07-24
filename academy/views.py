from django.shortcuts                     import render, get_object_or_404, redirect
from django.http                          import HttpResponse
from django.contrib.auth.decorators      import login_required
from django.contrib.auth.forms           import UserCreationForm
from django.contrib.auth                 import authenticate, login, logout as auth_logout
from django.urls                         import reverse_lazy
from allauth.account.views                import LoginView as AllAuthLoginView
from django.contrib.auth.views            import LogoutView
from django.contrib.auth.mixins           import LoginRequiredMixin
from django.views.generic                 import TemplateView, UpdateView
from django.contrib.auth                  import get_user_model

from reportlab.pdfgen                     import canvas

from .models import (
    Lesson, LessonProgress, LessonSection, SectionProgress,
    Quiz, Question, Answer, Certificate
)

from .forms                               import ProfileUpdateForm

User = get_user_model()
# views.py
import os
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Certificate

@login_required
def home(request):
    lessons = Lesson.objects.all().order_by('order')
    progress_data = []

    for lesson in lessons:
        # 1. Total sections in this lesson
        total_sections = lesson.sections.count()

        # 2. Sections the user has viewed
        viewed_sections = SectionProgress.objects.filter(
            user=request.user,
            section__lesson=lesson
        ).count()

        # 3. Compute a raw percentage
        percent = round((viewed_sections / total_sections) * 100) if total_sections else 0

        # 4. If they've passed the final quiz, show 100%
        if LessonProgress.objects.filter(
            user=request.user,
            lesson=lesson,
            completed=True
        ).exists():
            percent = 100

        progress_data.append({
            'lesson': lesson,
            'progress': percent,
        })

    return render(request, 'academy/home.html', {
        'progress_data': progress_data
    })
from django.shortcuts               import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models                        import Lesson, LessonProgress, LessonSection, SectionProgress

@login_required
def lesson_detail(request, lesson_id):
    # 1) Fetch lesson & its sections
    lesson   = get_object_or_404(Lesson, pk=lesson_id)
    sections = lesson.sections.all()

    # 2) Ensure we have a LessonProgress record (visited but not necessarily completed)
    LessonProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson,
        defaults={'completed': False},
    )

    # 3) Count how many sections the user has viewed
    total_sections  = sections.count()
    viewed_sections = SectionProgress.objects.filter(
        user=request.user,
        section__lesson=lesson
    ).count()

    # 4) Compute a percentage (round to nearest whole number)
    progress = round((viewed_sections / total_sections) * 100) if total_sections else 0

    return render(request, 'academy/lesson_detail.html', {
        'lesson':   lesson,
        'sections': sections,
        'progress': progress,
    })

@login_required
def quiz_view(request, quiz_id):
    quiz      = get_object_or_404(Quiz, id=quiz_id)
    lesson    = quiz.lesson
    questions = quiz.question_set.all()

    if request.method == 'POST':
        # 1) Grade
        score = calculate_score(request.POST, quiz)
        passed = score >= quiz.pass_mark

        # 2) Mark progress
        LessonProgress.objects.update_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'completed': passed},
        )

        if passed:
            # 3a) Create Certificate + redirect
            cert = Certificate.objects.create(
                user=request.user,
                lesson=lesson,
                score=score
            )
            return redirect('academy:certificate', cert_id=cert.id)

        # 3b) Failed → try again
        return render(request, 'academy/quiz_failed.html', {
            'quiz': quiz,
            'score': score,
            'pass_mark': quiz.pass_mark,
        })

    # GET → show the quiz form
    return render(request, 'academy/quiz.html', {
        'quiz': quiz,
        'questions': questions,
    })


def calculate_score(post_data, quiz):
    correct_answers = 0
    questions = quiz.question_set.all()
    for question in questions:
        selected = post_data.get(f'question_{question.id}')
        if selected and Answer.objects.get(id=selected).is_correct:
            correct_answers += 1
    return (correct_answers / questions.count()) * 100


@login_required
def certificate_view(request, cert_id):
    cert = get_object_or_404(Certificate, id=cert_id, user=request.user)
    return render(request, 'academy/certificate.html', {'cert': cert})

@login_required
def generate_pdf(request, cert_id):
    cert = get_object_or_404(Certificate, id=cert_id, user=request.user)

    # Prepare HTTP response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{cert.user.username}.pdf"'

    # Create canvas
    c = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Draw border
    c.setLineWidth(4)
    margin = 0.5 * inch
    c.rect(margin, margin, width - 2*margin, height - 2*margin)

    # Draw logo at top center (optional)
    logo_path = os.path.join(settings.STATIC_ROOT, 'core', 'logo.png')
    if os.path.exists(logo_path):
        logo_width = 1.5 * inch
        c.drawImage(
            logo_path,
            (width - logo_width) / 2,
            height - margin - logo_width,
            logo_width,
            logo_width,
            preserveAspectRatio=True
        )

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - margin - (1.6*inch), "Certificate of Completion")

    # Recipient name
    full_name = cert.user.get_full_name() or cert.user.username
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height - margin - (2.4*inch), full_name)

    # Static text
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height - margin - (3.2*inch), "has successfully completed the module")
    c.setFont("Helvetica-BoldOblique", 16)
    c.drawCentredString(width/2, height - margin - (3.8*inch), cert.lesson.title)

    # Score and date
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height - margin - (4.6*inch), f"Score: {cert.score}%")
    date_str = cert.issued_at.strftime('%B %d, %Y')
    c.drawCentredString(width/2, height - margin - (5.2*inch), f"Issued on {date_str}")

   
    c.showPage()
    c.save()

    return response


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            if user:
                login(request, user)
                return redirect('academy:academy_home')
    else:
        form = UserCreationForm()
    return render(request, 'academy/signup.html', {'form': form})


class AcademyLoginView(AllAuthLoginView):
    template_name = "academy/login.html"
    success_url  = reverse_lazy("academy:academy_home")


@login_required
def account_view(request):
    return render(request, 'academy/account.html', {'user': request.user})


class AcademyLogoutView(LogoutView):
    template_name   = "academy/logout.html"
    http_method_names = ['get', 'post', 'head', 'options']
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return render(request, self.template_name)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model         = User
    form_class    = ProfileUpdateForm
    template_name = "academy/edit_account.html"
    success_url   = reverse_lazy("academy:account")
    def get_object(self):
        return self.request.user


@login_required
def delete_account(request):
    if request.method == "POST":
        auth_logout(request)
        request.user.delete()
        return redirect("home")
    return render(request, "academy/account_confirm_delete.html")


def privacy_policy(request):
    return render(request, 'academy/privacy_policy.html')

from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
@require_POST
def mark_section_viewed(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(LessonSection, id=section_id)
    SectionProgress.objects.get_or_create(
        user=request.user,
        section=section
    )
    # recalc progress
    lesson = section.lesson
    total = lesson.sections.count()
    viewed = SectionProgress.objects.filter(user=request.user, section__lesson=lesson).count()
    return JsonResponse({
        'viewed': viewed,
        'total': total,
        'progress': round((viewed/total)*100,1),
    })