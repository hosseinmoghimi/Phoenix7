from . import server_settings

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

 
SECRET_KEY = server_settings.SECRET_KEY
ALLOWED_HOSTS = server_settings.ALLOWED_HOSTS
INSTALLED_APPS = server_settings.INSTALLED_APPS
DEBUG = server_settings.DEBUG
DATABASES = server_settings.DATABASES

SITE_URL = server_settings.SITE_URL
STATIC_URL = server_settings.STATIC_URL
MEDIA_URL = server_settings.MEDIA_URL
QRCODE_URL = server_settings.QRCODE_URL
FILE_URL = server_settings.FILE_URL
STATICFILES_DIRS = server_settings.STATICFILES_DIRS
ADMIN_URL = server_settings.ADMIN_URL
FULL_SITE_URL = server_settings.FULL_SITE_URL


PUBLIC_ROOT = server_settings.PUBLIC_ROOT
PRIVATE_ROOT = server_settings.PRIVATE_ROOT
MEDIA_ROOT = server_settings.MEDIA_ROOT
STATIC_ROOT = server_settings.STATIC_ROOT
QRCODE_ROOT = server_settings.QRCODE_ROOT
FILE_ROOT = server_settings.FILE_ROOT
 
 
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
