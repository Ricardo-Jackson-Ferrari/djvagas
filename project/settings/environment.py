from pathlib import Path

from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS', default='127.0.0.1, localhost', cast=Csv()
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROLEPERMISSIONS_MODULE = 'project.roles'

ROLEPERMISSIONS_REDIRECT_TO_LOGIN = True

ROLEPERMISSIONS_SUPERUSER_SUPERPOWERS = False

AUTH_USER_MODEL = 'account.User'

LOGIN_REDIRECT_URL = LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = 'account:login'

PER_PAGE = 10
