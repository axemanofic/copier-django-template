from config.env import env

from .base import *  # noqa: F403


DEV_APPS = []

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS  # noqa: F405

DEV_MIDDLEWARE = []

MIDDLEWARE = DEV_MIDDLEWARE + MIDDLEWARE  # noqa: F405

# -------------------------------------

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

ROOT_URLCONF = "config.urlpatterns.local"
