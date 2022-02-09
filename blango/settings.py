import os
from pathlib import Path
from configurations import Configuration
from configurations import values
import dj_database_url
import logging

"""
Django settings for blango project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Development Configuration 

class Dev(Configuration):
  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent

  # Admin Settings 
  ADMINS = [("Jordan Brocker Rudow", "jbrockerrudow@gmail.com")]

  # Logging Configuration Settings
  # This config sets up one handler with the ID console. 
  # The handler eill log to the console.
  LOGGING = {
      "version": 1,
      "disable_existing_loggers": False,
      "filters": {
          "require_debug_false": {
              # Error Emails are only sent in production enviroments
              # The class below only passes messages through when DEBUG is False.
              "()": "django.utils.log.RequireDebugFalse",
          },
      },
      "formatters": {
          "verbose": {
              "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
              # Outputs the log level, time of the message (asctime), name of 
              # the module that generated the message, the process ID, 
              # thread ID, and lastly, the message.
              "style": "{",
          },
      },
      "handlers": {
          "console": {
              "class": "logging.StreamHandler", 
              "stream": "ext://sys.stdout",
              "formatter": "verbose",
          },
          "mail_admins": {
              "level": "ERROR", 
              "class": "django.utils.log.AdminEmailHandler",
              "filters": ["require_debug_false"],
          },
      },
      "loggers": {
          # Django.request so that only unhandled exceptions get sent.
          "django.request": {
              "handlers": ["mail_admins"],
              "level": "ERROR",
              # Add propagate: True; so the stack traces are logged to the console during development.
              "propagate": True,
          },
      },
      "root": {
          "handlers": ["console"],
          "level": "DEBUG",
      },
  }
  
  # Authentication and Authorization 
  # Point to Custom User Model
  AUTH_USER_MODEL= "blango_auth.User"
  
  # Django Registration Email
  # console email backend prints to terminal
  EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

  # Activation Key valid for 77 days
  ACCOUNT_ACTIVATION_DAYS = 7

  # Quick-start development settings - unsuitable for production
  # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = values.BooleanValue(True)

  ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io"])
  # Equivalent way of setting the above values as an env_var:
  # ALLOWED_HOSTS=localhost,0.0.0.0,.codio.io python3 manage.py runserver 0.0.0.0:8000
  X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
  CSRF_COOKIE_SAMESITE = None
  CSRF_TRUSTED_ORIGINS = [os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
  CSRF_COOKIE_SECURE = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SAMESITE = 'None'
  SESSION_COOKIE_SAMESITE = 'None'

  CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
  CRISPY_TEMPLATE_PACK = 'bootstrap5'

  # Application definition

  INSTALLED_APPS = [
      'rest_framework',
      'rest_framework.authtoken',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      # Sites must come after messages 
      'django.contrib.sites',
      'django.contrib.staticfiles',
      'blog.apps.BlogConfig',
      'crispy_forms',
      'crispy_bootstrap5',
      'debug_toolbar',
      'blango_auth.apps.BlangoAuthConfig',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
      'drf_yasg',
  ]

  MIDDLEWARE = [
      # The order of MIDDLEWARE is important. You should include the Debug
      # Toolbar middleware as early as possible in the list. However, it must
      # come after any other middleware that encodes the response’s content,
      # such as GZipMiddleware.
      'debug_toolbar.middleware.DebugToolbarMiddleware',
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      #'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      #'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]

  # The list of IP addresses that are allowed to use DJDT
  INTERNAL_IPS = ["192.168.10.93"]

  ROOT_URLCONF = 'blango.urls'

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR/'templates',],
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

  WSGI_APPLICATION = 'blango.wsgi.application'


  # Database
  # https://docs.djangoproject.com/en/3.2/ref/settings/#databases


  # Dj_Database_Url Module and the DatabaseURLValue Class
  # https://github.com/kennethreitz/dj-database-url#url-schema

  # Example URL schema to connect to a MySQL database:
  # mysql://username:password@mysql-host.example.com:3306/db_name?option1=value1&option2=value2

  # How we would make use of different databases with django configurations
  DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")

  # Password Hashing 
  # Argon2 Password Hashing Algorithm
  PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  ]

  # Password validation
  # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
  # https://docs.djangoproject.com/en/3.2/topics/i18n/

  LANGUAGE_CODE = 'en-us'

  TIME_ZONE = values.Value("UTC")

  USE_I18N = True

  USE_L10N = True

  USE_TZ = True


  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/

  STATIC_URL = '/static/'

  # Default primary key field type
  # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  
  # Configuration for AllAuth / Google Integration 
 
  # SITE_ID tells the app which "Site" object to use these 
  # settings for.
  SITE_ID = 1

  # Django Allauth creates a User object from a social account login
  # Since the Custom User model removed usernames, the
  # settings below will help ensure allauth doesn't fail 
  ACCOUNT_USER_MODEL_USERNAME_FIELD = None
  ACCOUNT_EMAIL_REQUIRED = True
  ACCOUNT_USERNAME_REQUIRED = False
  ACCOUNT_AUTHENTICATION_METHOD = "email"

  REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
      "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
}

# Browsable API - Swagger OpenAPI Specification
# https://swagger.io/specification/
# https://github.com/axnsan12/drf-yasg
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
        "Basic": {"type": "basic"},
    }
}

# Production 
class Prod(Dev):
    DEBUG = False
    # Prevent secret keys committed in code, from being used in production 
    SECRET_KEY = values.SecretValue()
