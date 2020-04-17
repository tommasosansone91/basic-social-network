"""
Django settings for simplesocial project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os ###
import django_heroku ###
from decouple import config ###

# per gestire user e password del database postgresql che cambiano ogni 24 ore sugli host
import dj_database_url ###

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# questo c'era già, ma forse ho aggiunto la cosa identica in TEMPLATE_DIR

#aggiungo
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
# scret_key hidden in env variable files hidden from git
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'groups',
    'posts',
    'bootstrap3',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', #zips up static files
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'simplesocial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

                # aggiungo 
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'simplesocial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
    }
}


database__default_credential_url= config("DATABASE_URL")

# nascondi questa password
# password 1 - .passwords.txt
DATABASES['default']=dj_database_url.config(default=database__default_credential_url)

# #postgres://user:password@host:porta/database_name

#di questo comandi qui sopra DATABASES['default']=dj_database_url.config(default=  
# non c'è bisogno in produzione  
# perchè heroku maneggia questo usando dj database che ho messo sopra con dj_database_url
# ne ho bisogno solo in locale per accedere al database.
# quindi alla fine della produzione devo cancellarlo

# questi sono settings minori
db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# aggiunta delle funzioni di hashers per user authentication


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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# aggiungo 
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]

# aggiunti per fixare failed deploy
# raise ImproperlyConfigured("You're using the staticfiles app " remote:        django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.
STATICSTORAGE = "Whitenoise.storage.CompressedManifestStaticFilesStorage" #zips up static files
django_heroku.settings(locals())  ###

# provo ad aggiungere io in modo indipendente
# STATIC_ROOT = [ os.path.join(BASE_DIR, 'staticfiles')]
# in questa ci devo mettere un file a caso per farla beccare da git
# non funiona

# login logout
# mi dice quali sono le pagine cui veng reindirizzato quando eseguo login o logout
# i nomi delle variabili sono probabilemtne preimpostate da django
LOGIN_REDIRECT_URL = "test"
LOGOUT_REDIRECT_URL = "thanks"