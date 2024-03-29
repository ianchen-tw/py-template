import shutil
import subprocess as sp
import sys
from pathlib import Path

dep_main = [
    "attrs",
    "rich",
    "loguru",
    "typer",
]
dep_dev = [
    "autoflake",
    "black",
    "isort",
    "poethepoet",
    "pytest",
    "pytest-cov",
    "ruff",
]


def require_exe(name: str) -> Path:
    exe = shutil.which(name)
    if not exe:
        print(f"require executable: {exe}")
        sys.exit(1)
    return Path(exe)


def run_exe(target: str, *args):
    exe = require_exe(target)
    final_args = []
    final_args.append(exe)
    final_args.extend(args)
    print(f"Execute: {final_args}")
    sp.run(final_args, check=True)


def do_git_init():
    run_exe("git", "init")
    run_exe("git", "add", "README.md", ".gitignore")
    run_exe("git", "commit", "-m", "inital commit")

    current_branch = (
        sp.check_output(["git", "branch", "--show-current"]).decode().strip()
    )
    if current_branch == "master":
        run_exe("git", "branch", "-m", "master", "main")

    run_exe("git", "add", ".")
    run_exe("git", "commit", "-m", "Setup for python development")


if __name__ == "__main__":
    run_exe("poetry", "env use", "{{ cookiecutter.python_version }}")
    run_exe("poetry", "add", *dep_main)
    run_exe("poetry", "add", "-G", "dev", *dep_dev)
    run_exe("poetry", "install", "--with", "dev")

    do_git_init()
    print("Post run done!!")
