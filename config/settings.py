import os
from pathlib import Path

from django.conf.global_settings import AUTH_USER_MODEL, LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, EMAIL_HOST, \
    EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, EMAIL_USE_SSL, SERVER_EMAIL, DEFAULT_FROM_EMAIL

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--2g7c%w=lpl^#l(*mycl1o36y7w4rnto&2#h(_5*tq+azn6-qz'

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
    'blog',
    'users',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "HM_22.1",
        "USER": "postgres",
        "PASSWORD": "123454321",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = (BASE_DIR / 'static',)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "sania.antsiferoff@yandex.ru"
EMAIL_HOST_PASSWORD = "qqwzsrlmvlphzmvv"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER