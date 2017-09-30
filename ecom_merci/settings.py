# import os
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
import os

BASE_DIR = Path(__file__).ancestor(1)
PROJECT_DIR = Path(__file__).ancestor(2)

SECRET_KEY = config('SECRET_KEY', default='')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DATABASES = {
        'default': config(
            'DATABASE_URL', default='sqlite://:memory:',
            cast=db_url,
        )
    }

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'django_extensions',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom_merci.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'users/templates/'),
                 os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecom_merci.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation' +
            '.UserAttributeSimilarityValidator'),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation' +
            '.MinimumLengthValidator'),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation' +
            '.CommonPasswordValidator'),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation' +
            '.NumericPasswordValidator'),
    },
]

LANGUAGE_CODE = 'PT-BR'
LANGUAGES = (
    ('pt-br', 'Português'),
)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# DATE_FORMAT = 'N j, Y'
DATE_FORMAT = 'd/m/Y'
SHORT_DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i:s'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%m-%d-%Y', '%Y-%m-%d')

LOCALE_PATHS = (
    'locale',
)

# Django suit Customization
SUIT_CONFIG = {
     'ADMIN_NAME': 'Ecom_merci',
}

# Static Files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "ProductsMedia")
