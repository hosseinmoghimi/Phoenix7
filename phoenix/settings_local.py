from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'sth here ....'

 
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

INSTALLED_APPS.append("utility")
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
CURRENCY="تومان"

##########################################################

##########################################################

##########################################################