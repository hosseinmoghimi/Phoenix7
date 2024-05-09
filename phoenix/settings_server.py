from pathlib import Path

import os
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-e=r6(=1-$v62u+!!y@45c2s6w)=^20(r1eq*z_k2b2brp7x6#)'

 
DEBUG = True
ALLOWED_HOSTS = ['*']

##########################################################
#  installed apps
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS.append("core")

INSTALLED_APPS.append("authentication")

##########################################################
#  databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
##########################################################
#  urls
SITE_URL="/"
STATIC_URL = SITE_URL+'static/'
MEDIA_URL = SITE_URL+'media/'
QRCODE_URL = SITE_URL+'qrcode/'
FILE_URL = SITE_URL+'file/'

##########################################################
#  roots
PUBLIC_ROOT="d:\\public\\phoenix7\\"
PRIVATE_ROOT="/"
MEDIA_ROOT =os.path.join(PUBLIC_ROOT,"media")
STATIC_ROOT =os.path.join(PUBLIC_ROOT,"static")
QRCODE_ROOT =os.path.join(PUBLIC_ROOT,"qrcode")
FILE_ROOT =os.path.join(PRIVATE_ROOT,"file")
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

##########################################################


##########################################################

##########################################################

##########################################################