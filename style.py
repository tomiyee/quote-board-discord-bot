import subprocess

if __name__ == "__main__":
    subprocess.run(["black", "."], check=True)
    subprocess.run(["flake8", "."], check=True)
    subprocess.run(["mypy", "."], check=True)
