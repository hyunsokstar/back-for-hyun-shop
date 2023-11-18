from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# env 객체 및 env_path 설정 추가
env = environ.Env()
env_path = BASE_DIR / ".env"

# env_path 가 존재 할 경우 파일 읽기
if env_path.exists():
    with env_path.open("rt", encoding="utf8") as f:
        env.read_env(f)

print(env.str("CHEATKEY", default="Hello Django !"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-_*^na62&as=mlyhyrf@%g)%4n=f5u_(8xkcdw-y9o7^m6j4v79"

# .env 에 SECRET_KEY 이 있을 경우 사용 없으면 default 값 사용
SECRET_KEY = env.str(
    "SECRET_KEY",
    default="django-insecure-_*^na62&as=mlyhyrf@%g)%4n=f5u_(8xkcdw-y9o7^m6j4v79",
)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool("DEBUG", default=True)

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third app
    "debug_toolbar",
    "django_bootstrap5",
    "rest_framework",
    "rest_framework_simplejwt",
    # local apps
    "accounts",
    "mall_test",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="ko-kr")


TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# simple jwt 관련 start

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "your-secret-key",  # 실제로는 보안을 위해 비밀 키를 환경 변수 등으로 저장할 것을 권장
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

# Authentication 및 Authorization 설정
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # 다른 백엔드도 추가 가능
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # 다른 인증 클래스들과 함께 사용 가능
    ],
}

# simple jwt 관련 end


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = env.str("STATIC_ROOT", default=BASE_DIR / "staticfiles")
MEDIA_URL = "media/"
MEDIA_ROOT = env.str("MEDIA_ROOT", default=BASE_DIR / "mediafiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

INTERNAL_IPS = ["127.0.0.1"]
