
import os
from pathlib import Path

# ─── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Secrets & Debug ───────────────────────────────────────────────────────────
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-in-env')
DEBUG      = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# ─── Hosts ─────────────────────────────────────────────────────────────────────
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost') \
                       .split(',')

# ─── Installed Apps ────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your apps
    'core',
    'academy',

    # third‑party
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_extensions',
    'grappelli',
    'ckeditor',
    'ckeditor_uploader',
]

# ─── Middleware & URLs ─────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF  = 'OGA_website.urls'
WSGI_APPLICATION = 'OGA_website.wsgi.application'
ASGI_APPLICATION = 'OGA_website.asgi.application'

# ─── Templates ─────────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],               # add paths here if you have project‑level templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# ─── Database ──────────────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE':   os.environ.get('DB_ENGINE',
                                  'django.db.backends.sqlite3'),
        'NAME':     os.environ.get('DB_NAME',
                                  BASE_DIR / 'db.sqlite3'),
        'USER':     os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST':     os.environ.get('DB_HOST', ''),
        'PORT':     os.environ.get('DB_PORT', ''),
    }
}

# ─── Password Validation ───────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── Internationalisation ──────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = os.environ.get('DJANGO_TIME_ZONE', 'UTC')
USE_I18N      = True
USE_TZ        = True

# ─── Static & Media ────────────────────────────────────────────────────────────
STATIC_URL        = '/static/'
STATIC_ROOT       = BASE_DIR / 'staticfiles'   # collectstatic target
STATICFILES_DIRS  = [BASE_DIR / 'core' / 'static']

MEDIA_URL         = '/media/'
MEDIA_ROOT        = BASE_DIR / 'media'

# ─── Email (SMTP) ──────────────────────────────────────────────────────────────
EMAIL_BACKEND     = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST        = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT        = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS     = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER   = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# ─── Sessions & Cookies ───────────────────────────────────────────────────────
SESSION_COOKIE_HTTPONLY   = True
CSRF_COOKIE_HTTPONLY      = True
SESSION_COOKIE_SECURE     = os.environ.get('DJANGO_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE        = os.environ.get('DJANGO_COOKIE_SECURE', 'False') == 'True'
SESSION_COOKIE_SAMESITE   = 'Lax'
CSRF_COOKIE_SAMESITE      = 'Lax'
SESSION_COOKIE_AGE        = int(os.environ.get('DJANGO_SESSION_AGE', 1800))
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ─── Authentication ───────────────────────────────────────────────────────────
LOGIN_URL          = 'academy:login'
LOGIN_REDIRECT_URL = 'academy:academy_home'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# django‑allauth settings
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_VERIFICATION         = 'optional'
ACCOUNT_LOGIN_METHODS              = ['username', 'email']
ACCOUNT_SIGNUP_FIELDS              = ['username', 'email', 'password1', 'password2']
ACCOUNT_FORMS = {'signup': 'academy.forms.CustomSignupForm'}

# ─── Social Providers Placeholders ────────────────────────────────────────────
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id':     os.environ.get('GOOGLE_CLIENT_ID', ''),
            'secret':        os.environ.get('GOOGLE_CLIENT_SECRET', ''),
            'key':           '',
        }
    }
}

# ─── CKEditor ─────────────────────────────────────────────────────────────────
CKEDITOR_UPLOAD_PATH   = "lesson_uploads/"
CKEDITOR_CONFIGS       = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    }
}

# ─── Crispy Forms ──────────────────────────────────────────────────────────────
CRISPY_ALLOWED_TEMPLATE_PACKS = ['bootstrap5']
CRISPY_TEMPLATE_PACK         = 'bootstrap5'

# ─── Default primary key field type ───────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

