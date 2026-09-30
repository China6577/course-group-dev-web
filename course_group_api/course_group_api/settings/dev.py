"""
course_group_api 开发环境配置
"""
from .base import *  # 导入所有公共配置
from django.core.management.utils import get_random_secret_key

# 开发环境Debug开启
DEBUG = True

# 开发环境允许的主机
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# 开发密钥从环境变量读取；未配置时仅为当前进程生成临时密钥
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') or get_random_secret_key()

# 开发环境数据库配置
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
        "PORT": int(os.environ.get("DB_PORT", "3306")),
        "USER": os.environ.get("DB_USER", "root"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "NAME": os.environ.get("DB_NAME", "course_group_db"),
    }
}

# 开发环境允许的跨域URL（保留原有配置）
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}