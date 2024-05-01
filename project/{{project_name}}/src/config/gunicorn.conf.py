import multiprocessing
import os

gunicorn_host = os.getenv("DJANGO_GUNICORN_HOST", default="0.0.0.0")
gunicorn_port = os.getenv("DJANGO_GUNICORN_PORT", default="8000")
bind = f"{gunicorn_host}:{gunicorn_port}"
workers = multiprocessing.cpu_count() * 2 + 1
