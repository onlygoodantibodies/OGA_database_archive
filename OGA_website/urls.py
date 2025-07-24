
from django.contrib import admin
from django.urls import path, include
from core import views as core_views  #  Alias core views
from academy import views as academy_views  #  Alias academy views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), 
    path('certificate/<int:cert_id>/pdf/', academy_views.generate_pdf, name='generate_pdf'),  
    path('academy/', include('academy.urls', namespace='academy')),
    path('accounts/', include('allauth.urls')),
    path('grappelli/', include('grappelli.urls')),      # if you installed django-grappelli


    # CKEditor upload endpoints
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Serve media files in development mode (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files manually in production (DEBUG=False)
if not settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
