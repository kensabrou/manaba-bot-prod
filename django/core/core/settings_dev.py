import os
from settings import *

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*"]
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE"),
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASS"),
        'HOST': '',
        'PORT': ''
    }
}

# 開発用サーバ起動コマンド
# python manage.py runserver --settings core.settings_dev