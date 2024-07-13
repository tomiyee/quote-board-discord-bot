import subprocess


def main() -> None:
    """Runs the command that starts the quote board bot"""
    subprocess.run(["poetry", "run", "python", "./quote_bot/main.py"])
