# Quote Board Discord Bot

Based on the quick start here.
https://discordpy.readthedocs.io/en/stable/quickstart.html

## Setup Instructions

To setup the dev environment, these are the high level steps:
1. (Optional) Install PyEnv
2. Install Pre-Commits
3. Install Poetry
4. Install Package Dependencies

Keep reading for a short explanation for what each tool is and how to install it.

### (Optional) Install PyEnv

PyEnv is a simple, highly-recommended tool for managing different versions of Python on the same device. If something is Python version specific, we'll find out the hard way.

To install PyEnv, follow the instructions [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).

### Install Pre-Commits

Pre-commit is a framework for running code before every GitHub commit. I'm using it to run the style script to ensure that any new Python code follows style conventions.

To install pre-commit, (based on the instructions [here](https://pre-commit.com/#install)), run:
```bash
pip install pre-commit
pre-commit install
```

### Install Poetry

Poetry is a powerful tool for dependency management and packaging in Python. It allows for defining dependencies powerfully and manages virtual environments in the background for you when working on different projects.

Follow the instructions [here](https://python-poetry.org/docs#installing-with-the-official-installer).

### Install Package Dependencies

I'm running with Python 3.10. You can use PyEnv to set the Python version:

```bash
pyenv install 3.10
pyenv global 3.10
```

In the parent directory, you can install all the dependencies with:

```bash
poetry install
```

## Development

A quick tour of the source code:
```
/quote-board-discord-bot
├── /quote_bot       # Project source code
│   └── ...
└── /scripts         # Poetry command scripts
    ├── /style.py    # Runs a style checker
    └── ...
```

### Starting the Discord Bot

I made a script to simplify starting the robot.

```bash
poetry run start
```

### Adding a New Dependency

To add a new dependency, use the following Poetry command:

```bash
poetry add <dependency>
```

If it is intended as a dev dependency only, add the `--group=dev` flag.
```bash
poetry add <dependency> --group=dev
```

### Adding a Poetry Script

The key file for Poetry is the `./pyproject.toml` file. This file specifies what packages the project depends on and what Python functions are scripts that you can run in the file.

To add a new script (a new `poetry run <script>`), you can modify the section at the bottom of `./pyproject.toml` under the section `[tool.poetry.scripts]`. To define a command, follow the pattern:
```
<command> = "<path.to.file>:<function>"
```

For example, let's say there is a function in the file `scripts/style.py` called `main()`, and I want to call this function when I type `poetry run style`. Under the scripts header of `pyproject.toml`, I add this:
```
[tool.poetry.scripts]
style = "scripts.style:main"
```

## Hardware:

Developed on Ubuntu (WSL-2 specifically) and Mac.

## Development Notes

I referenced the instructions [here](https://discordpy.readthedocs.io/en/stable/intro.html#installing) for installing the dependencies of the Discord bot.

