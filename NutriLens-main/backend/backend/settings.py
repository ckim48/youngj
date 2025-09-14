import os
from pathlib import Path

# --- 기본 설정 ---
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'your-secret-key'  # 나중에 .env로 옮기는 게 좋을듯
DEBUG = True
ALLOWED_HOSTS = []

# --- 앱 등록 ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'accounts',
]

# --- 미들웨어 ---
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS가 먼저 와야 함
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# --- 템플릿 ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'backend/templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# --- DB ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- 인증 관련 ---
AUTH_USER_MODEL = 'accounts.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# --- 비밀번호 검증 ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# --- 언어 / 시간대 ---
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

# --- 정적/미디어 파일 ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend' / 'dist']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- CORS 허용 ---
CORS_ALLOW_ALL_ORIGINS = True

# --- GPT API Key (임시, 나중에 .env 처리 권장) ---
from dotenv import load_dotenv
load_dotenv(BASE_DIR / '.env_exam')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
