"""
Django settings for tsukuriga project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = str(environ.Path(__file__) - 3)

ENV_PATH = os.path.join(BASE_DIR, '.env')

env = environ.Env()
if os.path.isfile(ENV_PATH):
    env.read_env(ENV_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='z4dmv4gx*^lqkgmly!3-v3-w!f(tg+9ru1bh75)hm_+h%ac%fy')

ALLOWED_HOSTS = env('ALLOWED_HOST', default='*').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # social-auth-app-django
    'social_django',
    # django-webpack-loader
    'webpack_loader',
    # django-bulma
    'bulma',
    # django-markdownx
    'markdownx',
    # django-cleanup
    'django_cleanup',
    # django-maintenance-mode
    'maintenance_mode',
    # original apps
    'core.apps.CoreConfig',
    'upload.apps.UploadConfig',
    'browse.apps.BrowseConfig',
    'ajax.apps.AjaxConfig',
    'notify.apps.NotifyConfig',
    'account.apps.AccountConfig',
    'pages.apps.PagesConfig',
    'tools.apps.ToolsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'unslashed.middleware.RemoveSlashMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
]

ROOT_URLCONF = 'tsukuriga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.common',
                'account.context_processors.contribution_ranking',
                'browse.context_processors.labels',
                'pages.context_processors.pages',
                'notify.context_processors.notification',
            ],
        },
    },
]

WSGI_APPLICATION = 'tsukuriga.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/assets/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'tsukuriga', 'assets')

SITE_ID = 1

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# social-auth-app-django
# https://github.com/python-social-auth/social-app-django

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'account.pipeline.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_TWITTER_KEY = env('TWITTER_KEY', default='')
SOCIAL_AUTH_TWITTER_SECRET = env('TWITTER_SECRET', default='')

AUTH_USER_MODEL = 'account.User'

# django-webpack-loader
# https://github.com/owais/django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

# django-unslashed
# https://github.com/frnhr/django-unslashed
APPEND_SLASH = False
REMOVE_SLASH = True

# django-markdownx
MARKDOWNX_MEDIA_PATH = 'pages/'

MARKDOWNX_MARKDOWNIFY_FUNCTION = 'pages.utils.markdownify'

# django-maintenance-mode
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
MAINTENANCE_MODE_IGNORE_SUPERUSER = True
MAINTENANCE_MODE_IGNORE_STAFF = True
MAINTENANCE_MODE_STATE_FILE_PATH = os.path.join(BASE_DIR, 'tsukuriga', 'settings', 'maintenance_mode_state.txt')
MAINTENANCE_MODE_STATE_BACKEND = 'core.utils.LocalFileBackend'

# upload.models
ENCODE_OPTIONS = {
    'audio_codec': 'aac'
}
