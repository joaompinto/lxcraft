import os

from invoke import task


@task
def docker(c):
    c.run("sh develop/docker-bash", pty=True)


@task
def setup(c):
    print("Installing Python requirements...")
    c.run("pip install -r requirements.txt -r requirements-dev.txt", hide=True)


@task
def test(c):
    c.run("python -m pytest -x tests/", pty=True)


@task
def test_only(c, filter: str):
    c.run(f"python -m pytest -x -v -s -k {filter}", pty=True)


@task
def cover(c):
    c.run("python -m pytest -x --cov-report term-missing --cov=lxcraft tests", pty=True)


@task
def cover_only(c, filter: str):
    c.run(
        f"python -m pytest -x --cov-report term-missing --cov=lxcraft tests -k {filter}",
        pty=True,
    )


@task
def run_sample(c, filename: str):
    os.chdir("samples")
    os.environ["PYTHONPATH"] = ".."
    c.run(
        f"python ../{filename}",
        pty=True,
    )
