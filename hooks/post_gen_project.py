import shutil
import sys
from subprocess import run
from typing import Optional, List
from pathlib import Path

def require_exe(name: str) -> Path:
    exe = shutil.which(name)
    if not exe:
        print(f"require executable: {exe}")
        sys.exit(1)
    return Path(exe)

def do_poetry_install_dependency():
    poetry = require_exe("poetry")
    run([poetry,"install", "--no-interaction"])

def do_git_init():
    git = require_exe("git")
    run([git, "init"])
    run([git, "branch", "-m", "master", "main"])
    run([git, "add", "README.md", ".gitignore"])
    run([git, 'commit', "-m", "inital commit"]) 

    
if __name__ == "__main__":
    do_poetry_install_dependency()
    do_git_init()
    print("Post run done!!")
