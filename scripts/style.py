import argparse
import subprocess


def main() -> None:
    """Runs style checker tools."""
    parser = argparse.ArgumentParser(description="Style.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="error if failing style",
    )
    args = parser.parse_args()
    check_flag = ["--check"] if args.check else []
    subprocess.run(["isort", ".", *check_flag], check=True)
    subprocess.run(["black", ".", *check_flag], check=True)
    subprocess.run(["flake8", "."], check=True)
    subprocess.run(["mypy", "."], check=True)
