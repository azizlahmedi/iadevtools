# -*- coding: utf-8 -*-
import os

from neoxam.settings.base import Mixin


class Core(Mixin):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ADMINS = (
        ('Olivier Mansion', 'olivier.mansion@neoxam.com'),
    )
    MANAGERS = ADMINS
    DEFAULT_FROM_EMAIL = 'olivier.mansion@neoxam.com'
    DEBUG = True
    ALLOWED_HOSTS = ('.iadev-tools',)
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ROOT_URLCONF = 'neoxam.urls'
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
                    'neoxam.elastic.context_processors.kibana',
                ],
            },
        },
    ]

    DATABASE_DEFAULT_HOST = 'localhost'

    @property
    def DATABASE_DEFAULT_PASSWORD(self):
        raise NotImplementedError('DATABASE_DEFAULT_PASSWORD')

    @property
    def DATABASES(self):
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'neoxam_db',
                'USER': 'neoxam_user',
                'PASSWORD': self.DATABASE_DEFAULT_PASSWORD,
                'HOST': self.DATABASE_DEFAULT_HOST,
                'PORT': '5432',
            },
            'versioning': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'vers',
                'USER': 'maschiel',
                'PASSWORD': 'sungard',
                'HOST': 'neptune.sungard-finance.fr',
                'PORT': '3307',
            }
        }
        dblocks = databases['default'].copy()
        dblocks['TEST'] = {'MIRROR': 'default',}
        databases[self.DBLOCKS_DATABASE_ALIAS] = dblocks
        return databases

    WSGI_APPLICATION = 'neoxam.wsgi.application'
    DATABASE_ROUTERS = ['neoxam.routers.VersioningRouter']
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
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = False
    USE_L10N = False
    USE_TZ = True
    STATIC_URL = '/static/'

    @property
    def LOGGING(self):
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'root': {
                'level': 'NOTSET',
                'handlers': ['console', ],
            },
            'formatters': {
                'verbose': {
                    'format': self.CELERYD_LOG_FORMAT,
                },
            },
            'handlers': {
                'console': {
                    'level': self.LOGGING_LEVEL,
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose'
                },
            },
            'loggers': {
                # Override Gunicorn configuration
                'gunicorn.error': {
                    'propagate': True,
                    'handlers': [],
                },
                # Do not spam logs with amqp
                'amqp': {
                    'level': 'WARNING',
                    'handlers': [],
                },
                # Do not spam debug logs with celery pool
                'celery.pool': {
                    'level': 'WARNING',
                    'handlers': [],
                },
                # Do not spam with Delia
                'delia': {
                    'level': 'INFO',
                    'handlers': [],
                },
                # Do not spam with paramiko
                'delia': {
                    'level': 'INFO',
                    'paramiko': [],
                },
                # Override default Django config
                'py.warnings': {
                    'handlers': [],
                },
                'django': {
                    'handlers': [],
                },
                'django.db.backends': {
                    'level': 'ERROR',
                    'handlers': ['console'],
                    'propagate': False,
                },
            },
        }

    @property
    def LOGGING_LEVEL(self):
        return 'DEBUG' if self.DEBUG else 'INFO'
