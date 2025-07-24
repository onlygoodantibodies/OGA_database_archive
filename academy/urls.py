# academy/urls.py
from django.urls import path
from . import views
from allauth.account.views import SignupView
from .views import (
    AcademyLoginView,
    AcademyLogoutView,
    ProfileUpdateView,
    delete_account,
)

app_name = "academy"

urlpatterns = [
    path('', views.home, name='academy_home'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz'),
    path('signup/', SignupView.as_view(template_name='academy/signup.html'), name='signup'),
    path('login/', AcademyLoginView.as_view(), name='login'),
    path('account/', views.account_view, name='account'),
    path('logout/', AcademyLogoutView.as_view(), name='logout'),
    path("account/edit/", ProfileUpdateView.as_view(), name="edit_account"),
    path("account/delete/", delete_account, name="delete_account"),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('certificate/<int:cert_id>/', views.certificate_view, name='certificate'),
    path('certificate/<int:cert_id>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('lesson/mark_section/',views.mark_section_viewed,name='mark_section'),

]
