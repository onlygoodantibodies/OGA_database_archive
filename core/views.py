from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def projects(request):
    return render(request, 'core/projects.html')

def publications(request):
    return render(request, 'core/publications.html')

def partners(request):
    return render(request, 'core/partners.html')

def data_view(request):
    return render(request, 'core/data.html') 

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'Contact Form Submission from {name}'
        full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'

        send_mail(
            subject,
            full_message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return redirect('success')  # Redirect to the success page
    
    return render(request, 'core/contact.html')

def success(request):
    return render(request, 'core/success.html')

def news(request):
    return render(request, 'core/news.html')


def projects(request):
    return render(request, 'core/projects.html')
