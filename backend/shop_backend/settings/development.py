from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_ENV') == 'dev'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7b#hyk+5obk*utdd2gmqrj%ho8yhn9qt(8+qot25cj8zy83r@l'



ALLOWED_HOSTS = ['localhost', '127.0.0.1']


CORS_ORIGIN_ALLOW_ALL = True