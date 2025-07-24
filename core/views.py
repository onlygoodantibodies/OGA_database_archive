# core/views.py

from django.shortcuts      import render, redirect, get_object_or_404
from django.core.mail      import send_mail
from django.conf           import settings
from .models               import Gene, Antibody

def home(request):
    query   = request.GET.get('search', '').strip()
    genes   = Gene.objects.all().order_by('name')
    if query:
        genes = genes.filter(name__icontains=query)
    no_results = not genes.exists() and bool(query)
    return render(request, "core/home.html", {
        "genes":       genes,
        "search_query": query,
        "no_results":   no_results,
    })

def about(request):
    return render(request, 'core/about.html')

def projects(request):
    return render(request, 'core/projects.html')

def publications(request):
    return render(request, 'core/publications.html')

def partners(request):
    return render(request, 'core/partners.html')

def contact(request):
    if request.method == 'POST':
        name, email, message = (request.POST.get(f) for f in ('name','email','message'))
        subject   = f'Contact Form Submission from {name}'
        full_msg  = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        send_mail(subject, full_msg, email, [settings.EMAIL_HOST_USER])
        return redirect('success')
    return render(request, 'core/contact.html')

def success(request):
    return render(request, 'core/success.html')

def news(request):
    return render(request, 'core/news.html')

def resources(request):
    return render(request, 'core/resources.html')

def antibody_table(request, gene_id):
    gene       = get_object_or_404(Gene, id=gene_id)
    qs         = gene.antibodies.select_related("description").all()
    # apply filters…
    # build antibody_data…
    # build hosts, clonality_options, etc…
    return render(request, "core/antibody_table.html", {
        "gene": gene,
        # …other context…
    })

def set_dark_mode(request):
    resp = redirect('home')
    resp.set_cookie(
        'dark_mode', 'enabled',
        max_age=60*60*24*30,
        secure=True, httponly=True, samesite='Lax'
    )
    return resp

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

