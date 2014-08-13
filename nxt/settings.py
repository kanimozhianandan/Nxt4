"""


For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ac5c9b0r^)vtp4yd95nh0^kwgmtdw@@pcf@$z1ndlbv%p5i=wz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration',
    'userprofile',
    'collegelist',
    'friendship',
    'django_messages',
    'privacy',
    'hvad',
    'feeds',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nxt.urls'

WSGI_APPLICATION = 'nxt.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS=(
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',)

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'corenxt',
        'USER': 'root',
        'PASSWORD':'thangamm',
        'HOST':'',
        'PORT':'',
        
    }
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..', 'static/corenxtvid').replace('\\','/')

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
APPEND_SLASH = False
ACCOUNT_ACTIVATION_DAYS = 2
ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'
# https://docs.djangoproject.com/en/dev/howto/static-files/

LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGIN_URL = '/login/'
STATICFILES_DIRS = os.path.join(BASE_DIR,"static"),
STATIC_URL = '/static/'
TEMPLATE_DIRS=(os.path.join(BASE_DIR,"templates"),os.path.join(BASE_DIR,"registration"),os.path.join(BASE_DIR,"friendship"),os.path.join(BASE_DIR,"messages"),(os.path.join(BASE_DIR,"privacy")))
