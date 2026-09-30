"""
course_group_api 生产环境配置
"""
from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ["example.com", "localhost", "127.0.0.1"]

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("请设置 DJANGO_SECRET_KEY 环境变量！")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get('DB_HOST'),
        "PORT": int(os.environ.get('DB_PORT')),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "NAME": os.environ.get('DB_NAME'),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        }
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
