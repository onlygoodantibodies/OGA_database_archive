from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Gene, Antibody
from django.conf import settings


def home(request):
    # Get the search query from the request
    query = request.GET.get('search', '').strip()  # Retrieve the search query from the URL

    # Fetch all genes by default and order them alphabetically
    genes = Gene.objects.all().order_by('name')

    # Filter genes if a query is provided
    if query:
        genes = genes.filter(name__icontains=query).order_by('name')  # Case-insensitive partial match, ordered alphabetically

    # Check if there are no results
    no_results = not genes.exists() and bool(query)  # True if query exists but no genes match

    return render(request, "core/home.html", {
        "genes": genes,
        "search_query": query,  # Pass the query to pre-fill the search bar
        "no_results": no_results,  # Whether or not there are results for the query
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

def resources(request):
    return render(request, 'core/resources.html')

def antibody_table(request, gene_id):
    gene = get_object_or_404(Gene, id=gene_id)
    antibodies = gene.antibodies.all().select_related("description")

    # Get filter parameters
    host_filter = request.GET.get("host")
    clonality_filter = request.GET.get("clonality")
    recombinant_filter = request.GET.get("recombinant")

    # Apply filters
    if host_filter:
        antibodies = antibodies.filter(description__host=host_filter)
    if clonality_filter:
        antibodies = antibodies.filter(description__clonality=clonality_filter)
    if recombinant_filter:
        antibodies = antibodies.filter(description__recombinant=recombinant_filter)

    # Prepare structured dataset
    antibody_data = []
    for antibody in antibodies:
        experiments = {
            "WB": None,
            "IP": None,
            "ICC_IF": None,
            "FC": None,
        }

        for experiment in antibody.experiments.all():
            key = experiment.experiment_type.replace("-", "_")
            if experiment.file_path:
                experiments[key] = experiment.file_path.url

        description = None
        if hasattr(antibody, "description"):
            description = {
                "rrid": antibody.description.rrid,
                "supplier": antibody.description.supplier,
                "host": antibody.description.host,
                "clonality": antibody.description.clonality,
                "recombinant": antibody.description.recombinant
            }

        antibody_data.append({
            "name": antibody.name,
            "experiments": experiments,
            "description": description,
        })

    # Fetch unique filter options
    hosts = gene.antibodies.filter(description__host__isnull=False).values_list("description__host", flat=True).distinct()
    clonality_options = gene.antibodies.filter(description__clonality__isnull=False).values_list("description__clonality", flat=True).distinct()
    recombinant_options = gene.antibodies.filter(description__recombinant__isnull=False).values_list("description__recombinant", flat=True).distinct()

    return render(request, "core/antibody_table.html", {
        "gene": gene,
        "f1000_report_link": gene.f1000_report_link,  # Pass the link to the template
        "antibody_data": antibody_data,
        "hosts": hosts,
        "clonality_options": clonality_options,
        "recombinant_options": recombinant_options,
    })

