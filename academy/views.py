from django.shortcuts import render, get_object_or_404
from .models import Lesson, Quiz, Certificate

def home(request):
    lessons = Lesson.objects.all().order_by('order')
    return render(request, 'academy/home.html', {'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'academy/lesson_detail.html', {'lesson': lesson})

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        # Calculate score & issue certificate if passed
        score = calculate_score(request.POST, quiz)
        if score >= quiz.pass_mark:
            cert = Certificate.objects.create(
                user=request.user,
                lesson=quiz.lesson,
                score=score
            )
            return redirect('certificate', cert_id=cert.id)
    return render(request, 'academy/quiz.html', {'quiz': quiz})

def certificate_view(request, cert_id):
    cert = get_object_or_404(Certificate, id=cert_id)
    return render(request, 'academy/certificate.html', {'cert': cert})

def calculate_score(post_data, quiz):
    correct_answers = 0
    questions = quiz.question_set.all()
    for question in questions:
        selected_answer = post_data.get(f'question_{question.id}')
        if selected_answer and Answer.objects.get(id=selected_answer).is_correct:
            correct_answers += 1
    return (correct_answers / questions.count()) * 100