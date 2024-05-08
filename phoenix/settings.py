from . import settings_server

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

 
SECRET_KEY = settings_server.SECRET_KEY
ALLOWED_HOSTS = settings_server.ALLOWED_HOSTS
INSTALLED_APPS = settings_server.INSTALLED_APPS
DEBUG = settings_server.DEBUG
DATABASES = settings_server.DATABASES

SITE_URL = settings_server.SITE_URL
STATIC_URL = settings_server.STATIC_URL
MEDIA_URL = settings_server.MEDIA_URL
QRCODE_URL = settings_server.QRCODE_URL
FILE_URL = settings_server.FILE_URL

PUBLIC_ROOT = settings_server.PUBLIC_ROOT
PRIVATE_ROOT = settings_server.PRIVATE_ROOT
MEDIA_ROOT = settings_server.MEDIA_ROOT
STATIC_ROOT = settings_server.STATIC_ROOT
QRCODE_ROOT = settings_server.QRCODE_ROOT
FILE_ROOT = settings_server.FILE_ROOT
 
 
# SECURITY WARNING: don't run with debug turned on in production!
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'phoenix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'phoenix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
