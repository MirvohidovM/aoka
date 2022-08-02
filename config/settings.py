"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
import django.conf.locale
import django.conf.locale
import os
import environ

env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.utils.translation import gettext_lazy, gettext_noop

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o(*m3u1h+(8zpka%coig6$38$_ij9(6$+182q6_-0g1ff&c!_%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

AUTH_USER_MODEL = 'accounts.CustomUser'

INSTALLED_APPS = [
    # 'debug_toolbar',

    'jazzmin',
    'corsheaders',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework_simplejwt',
    'config',
    'django_filters',
    'drf_yasg',
    'django_summernote',
    'mptt',
    'tinymce',
    'imagekit',
    'slugify',

    'accounts',
    'baseapp',
    'useful_link',
    'menu',
    'opendata',
    'news',
    'contact',
    'organizations',
    'employee',
    'data',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'config.default_language.ForceDefaultLanguageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'config.authenticate.CustomAuthentication'
    ],
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ('uz', gettext_noop('Uzbek')),
    ('uzb', gettext_noop('uz_Cyrl')),
    ('ru', gettext_noop('Russian')),
    ('en', gettext_noop('English')),
]

EXTRA_LANG_INFO = {
    'uzb': {
        'bidi': False,  # right-to-left
        'code': 'uzb',
        'name': 'uz_Cyrl',
        'name_local': "Ўзбек",
    },
}

LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'config.translation'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'back.aoka.technocorp.uz']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "https://back.aoka.technocorp.uz",
    "https://aoka.technocorp.uz",
    "http://aoka.uz",
    "https://aoka.uz",
    "http://localhost:3000",
]

CSRF_TRUSTED_ORIGINS = [
    "https://back.aoka.technocorp.uz",
    "https://aoka.technocorp.uz",
    "https://aoka.uz",
    "http://aoka.uz",
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'authorizations',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

LOGIN_REDIRECT_URL = '/'
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken', 'Access-Control-Allow-Origin']
SECURE_BROWSER_XSS_FILTER = True

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

JAZZMIN_SETTINGS = {
    "site_title": "AOKA",
    "site_header": "AOKA",
    "site_brand": "AOKA",

    "order_with_respect_to": [  'accounts',
                                # "auth.User",  "auth.Group",
                                'auth', 'menu', 'contact', 'opendata',
                               'useful_link', 'news', 'organizations',
                              ],

    "icons": {
        "accounts.CustomUser": "fas fa-user",
        "auth.Group": "fas fa-users",
        "menu.menu": "fas fa-list",
        "useful_link.usefullink": "fas fa-link",
        "opendata.opendata": "far fa-folder-open",
        "opendata.opendataattachments": "fas fa-plus",
        "news.news": "fas fa-newspaper",
        "organizations.organization": "fas fa-sitemap",
        "contact.contact": "fas fa-id-card",
        "data.data": "fas fa-info",
        "employee.regionaladministration": "fas fa-location-crosshairs",
    },
}

TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")
# TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "100%",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    # 'images_upload_url': '/upload_image/', #add to plugin: image imagetools
    'relative_urls': False,
    'remove_script_host': False,
    'convert_urls': True,
    'fontsize_formats': "8px 9px 10px 11px 12px 14px 16px 18px 24px 30px 36px 48px 60px 72px 96px"
}


DOMAIN = 'back.aoka.technocorp.uz'
# BACK_URL = 'https://back.aoka.technocorp.uz'
# FRONT_URL = 'https://aoka.technocorp.uz'

BACK_URL = 'http://localhost:8000'
FRONT_URL = 'http://localhost:8000'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'technocorp.kh@gmail.com'
# EMAIL_HOST_PASSWORD = 'h1UdtuRYiSulOzIi' #old
EMAIL_HOST_PASSWORD = 'jdmhfpytyulygydv' #google-generated

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.cm.uz'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'matn@aoka.uz'
# EMAIL_HOST_PASSWORD = '$ayt*567' #old

# INTERNSHIP_EMAIL = "internship@aoka.uz"
# INTERNSHIP_PASSWORD = "stajirovka123"
# # internship@aoka.uz
# # stajirovka123

# MUROJAAT_EMAIL = "murojaat@aoka.uz"
# MUROJAAT_PASSWORD = "2022#fond"
# # Mail.aoka.uz
# # murojaat@aoka.uz
# # 2022#fond

# ERROR_EMAIL = "matn@aoka.uz"
# ERROR_PASSWORD = "$ayt*567"
# matn@aoka.uz
# $ayt*567

