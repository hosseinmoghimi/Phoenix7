from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-e=r6(=1-$v62u+!!y@45c2s6w)=^20(r1eq*z_k2b2brp7x6#)'
DATABASE_NAME="ghoghnus_db_2024_09_07__01_00_00"

MOEIN_ACCOUNT_LEVELS=2
TAFSILI_ACCOUNT_LEVELS=6

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
INSTALLED_APPS.append("tinymce")
INSTALLED_APPS.append("rest_framework")
 
INSTALLED_APPS.append("core")
INSTALLED_APPS.append("utility")
INSTALLED_APPS.append("authentication")
INSTALLED_APPS.append("market")
INSTALLED_APPS.append("accounting")
INSTALLED_APPS.append("processmanagement")

##########################################################

DB_NAME=os.path.join(BASE_DIR,DATABASE_NAME+".sqlite3")
#  databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_NAME,
    }
}
##########################################################
#  urls
SITE_URL="/"
STATIC_URL = SITE_URL+'static/'
MEDIA_URL = SITE_URL+'media/'
QRCODE_URL = SITE_URL+'qrcode/'
FILE_URL = SITE_URL+'file/'
ADMIN_URL=SITE_URL+"admin/"
FULL_SITE_URL="http://127.0.0.1:8085/"
##########################################################
#  roots
PUBLIC_ROOT="d:\\public\\phoenix7\\"
PRIVATE_ROOT="d:\\private\\phoenix7\\"
MEDIA_ROOT =os.path.join(PUBLIC_ROOT,"media")
STATIC_ROOT =os.path.join(PUBLIC_ROOT,"static")
QRCODE_ROOT =os.path.join(PUBLIC_ROOT,"qrcode")
FILE_ROOT =os.path.join(PRIVATE_ROOT,"file")
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

##########################################################
CURRENCY="ریال"

##########################################################
# parameter

CREATE_PROFILE_ON_USER_ADD=True
##########################################################

##########################################################