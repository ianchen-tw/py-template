from rich.console import Console

console = Console()


def main(name: str = "Ian"):
    console.print(f"[green]Hello {name}! :tada::tada::tada:")
