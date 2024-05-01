from ..config import BASE_DIR
from ..helpers import Context, task

TEMPLATES_DIR = BASE_DIR / "scripts" / "django" / "templates"


@task()
def run_manage(ctx: Context):
    """
    This is a shortcut to run manage.py
    """
    ctx.run(["python", "manage.py"])


@task()
def run_startapp(ctx: Context):
    """
    This is a shortcut to run manage.py startapp
    """
    app_template = TEMPLATES_DIR / "app_template"
    ctx.run(["python", "manage.py", "startapp", f"--template={app_template}",])


@task()
def run_runserver(ctx: Context):
    """
    This is a shortcut to run manage.py runserver
    """
    ctx.run(["python", "manage.py", "runserver"])


@task()
def run_makemigrations(ctx: Context):
    """
    This is a shortcut to run manage.py makemigrations
    """
    ctx.run(["python", "manage.py", "makemigrations"])


@task()
def run_migrate(ctx: Context):
    """
    This is a shortcut to run manage.py migrate
    """
    ctx.run(["python", "manage.py", "migrate"])
