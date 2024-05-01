from config.django.base import * # noqa: E402, F403

DEV_APPS = []

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS  # noqa

DEV_MIDDLEWARE = []

MIDDLEWARE = DEV_MIDDLEWARE + MIDDLEWARE  # noqa
