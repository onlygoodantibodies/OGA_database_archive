from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About Us page
    path('projects/', views.projects, name='projects'),  # Projects page
    path('partners/', views.partners, name='partners'),  # Partners page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('news/', views.news, name='news'),  # News page
    path('publications/', views.publications, name='publications'),  # Publications page
    path('resources/', views.resources, name='resources'),
    path('<int:gene_id>/', views.antibody_table, name='antibody_table'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
