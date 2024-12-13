
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About Us page
    path('projects/', views.projects, name='projects'),  # Projects page
    path('data/', views.data_view, name='data'),  # Data page
    path('partners/', views.partners, name='partners'),  # Partners page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('news/', views.news, name='news'),  # News page
    path('publications/', views.publications, name='publications')  # Publications page
]
