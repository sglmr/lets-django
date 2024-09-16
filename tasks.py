from invoke import task
from invoke.context import Context as Ctx

mng_py = "./web/manage.py"


@task
def tailwind_start(c: Ctx):
    c.run(f"python {mng_py} tailwind start")


@task
def tailwind_build(c: Ctx):
    c.run(f"python {mng_py} tailwind start")


@task
def collectstatic(c: Ctx):
    c.run(f"python {mng_py} collectstatic --no-input --clear | grep -v 'Deleting '")


@task(collectstatic)
def runserver(c: Ctx):
    c.run(f"python {mng_py} runserver")


@task
def update(c: Ctx):
    c.run("python -m pip install --upgrade pip")
    c.run("python -m pip install -r requirements.txt")
    c.run("python -m pip list --outdated")


@task(collectstatic)
def test(c: Ctx):
    c.run("clear")
    c.run("pytest -rsf -cov=web --cov-report=html")
