from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-qofy6lsk)yh8#+sonz%&ez8cronjz@jf%73invcs7!7v--e83+"

DEBUG = True

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'trips.User'

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'trips',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.vk',
    'sslserver',
    'django_extensions',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = "memotrips.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]
# Перенаправления

WSGI_APPLICATION = "memotrips.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'login'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'

# SOCIALACCOUNT_PROVIDERS = {
#     'vk': {
#         'APP': {
#             'client_id': '51933756',
#             'secret': '77dd87e377dd87e377dd87e33f74c5f5df777dd77dd87e3118aa0370ce76002c09aa362',
#             'key': '5SaoLVSNW57YiEKQ5uem',
#         },
#         'SCOPE': [
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'v': '5.131',
#         },
#         'METHOD': 'oauth2',
#         'REDIRECT_URI': 'https://1cc1-193-218-138-35.ngrok-free.app/accounts/vk/login/callback/',
#
#     }
# }
#
# CSRF_TRUSTED_ORIGINS = [
#     'https://1cc1-193-218-138-35.ngrok-free.app',
# ]

SITE_ID = 1
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
