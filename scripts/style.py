import subprocess


def main() -> None:
    """Runs style checker tools."""
    subprocess.run(["black", "."], check=True)
    subprocess.run(["flake8", "."], check=True)
    subprocess.run(["mypy", "."], check=True)
