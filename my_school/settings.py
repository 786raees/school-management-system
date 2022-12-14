from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-43h6y40*trrqh)!+(rrq*&*-ql0uw57@%nxw6a*$n0#yuc5_j*'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_select2', # https://django-select2.readthedocs.io/en/latest/
    'django_extensions', # https://django-extensions.readthedocs.io/en/latest/
    'django_htmx', # https://django-htmx.readthedocs.io/en/latest/
    'crispy_forms', #  https://django-crispy-forms.readthedocs.io/en/latest/install.html
    'django_tables2', # https://django-tables2.readthedocs.io/en/latest/
    'sweetify', # https://github.com/Atrox/sweetify-django
    'slippers', # https://mitchel.me/slippers/docs/introduction/
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'import_export',
    'croppie',
    'django_filters',
]

USER_INSTALLED_APPS = [
    'configurations.apps.ConfigurationsConfig',
    'users.apps.UsersConfig',
    'academics.apps.AcademicsConfig',


    "compressor", # https://django-compressor.readthedocs.io/en/stable/quickstart.html
    'django_cleanup.apps.CleanupConfig',  # should go after your apps

]

INSTALLED_APPS = DJANGO_INSTALLED_APPS + THIRD_PARTY_APPS + USER_INSTALLED_APPS

CRISPY_TEMPLATE_PACK = "bootstrap4"

SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional' # it can "mandatory" or "none"
# ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = 'confurations:default_school_view'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# ACCOUNT_FORMS = {
#             'signup': 'accounts.forms.SuperAdminUserCreationForm'
# }


LOGIN_URL = 'account_login'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'my_school.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            "builtins": ["slippers.templatetags.slippers"],

        },
    },
]

WSGI_APPLICATION = 'my_school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR/'assets'
MEDIA_ROOT = BASE_DIR/'media'

STATICFILES_DIRS = [
    # BASE_DIR / 'assets',
    BASE_DIR / 'static',
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Cached values for backwards compatibility
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'select2': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = 'select2'

# possible options: 'sweetalert', 'sweetalert2' - default is 'sweetalert2'
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

AUTH_USER_MODEL = 'users.AllUser'