from config.env import env

from .base import *  # noqa: F403


DEBUG = False

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

ROOT_URLCONF = "config.urlpatterns.prod"
