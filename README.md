# copier-django-template

This template is based on [copier](https://copier.readthedocs.io/en/stable/) for [django](https://docs.djangoproject.com/en/stable/).

View project
---

```
./
├── scripts # project tasks
│   ├── django # list task for django
│   │   └── __init__.py
│   ├── config.py # config file for tasks
│   └── helpers.py # helpers for tasks
├── src # source code project
│   ├── config
│   │   ├── django # configuration for django
│   │   ├── settings # settings for database and etc.
│   │   ├── urlpatterns # url patterns for django
│   │   ├── asgi.py
│   │   ├── env.py
│   │   ├── gunicorn.conf.py # config for gunicorn
│   │   └── wsgi.py
│   ├── manage.py
│   └── __version__.py # version of project
├── pyproject.toml # dependencies for project
└── README.md
```

Installation
---

1. Install Python 3.8 or later
2. Install Git latest version
3. Install copier: 
    * via pipx: ``pipx install copier``
    * via pip: ``pip install copier``

Genearate project
---

On the command line: 
```
copier copy https://github.com/axemanofic/copier-django-template.git <path/to/destination>
```
Or in Python code:

```python
from copier import run_copy

# Or from a Git URL.
run_copy("https://github.com/axemanofic/copier-django-template.git", "path/to/destination")

# You can also use "gh:" as a shortcut of "https://github.com/"
run_copy("gh:axemanofic/copier-django-template.git", "path/to/destination")
```
