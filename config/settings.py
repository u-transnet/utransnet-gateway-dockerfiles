from .base import *
from .production import *

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'public', 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'public', 'media')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'put your own secrent key'

BLOCKCHAIN_NOBROADCAST = False

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_CALLER_ID = ''

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

ALLOWED_HOSTS = ['web']

DATABASES = {  
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
} 
