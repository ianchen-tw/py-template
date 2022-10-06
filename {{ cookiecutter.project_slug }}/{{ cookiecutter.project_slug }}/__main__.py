import logging

import typer
from loguru import logger
from rich.console import Console
from rich.logging import RichHandler

from .cli import main

logger.configure(
    handlers=[{"sink": RichHandler(level=logging.DEBUG), "format": "{message}"}]
)
console = Console()

app = typer.Typer(
    help="",
    add_completion=False,
    no_args_is_help=True,
    add_help_option=True,
    pretty_exceptions_enable=False,
    context_settings={
        # click context settings
        # reference: https://click.palletsprojects.com/en/8.1.x/api/#context
        "help_option_names": ["-h", "--help"],
        "show_default": True,
    },
)

app.command()(main)

if __name__ == "__main__":
    app()
