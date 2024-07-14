# Quote Board Discord Bot

Based on the quick start here.
https://discordpy.readthedocs.io/en/stable/quickstart.html

## Setup Instructions

To setup the dev environment, these are the high level steps:
1. (Optional) Install PyEnv [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. Install Pre-Commits (based on the instructions [here](https://pre-commit.com/#install))
    ```bash
    pip install pre-commit
    pre-commit install
    ```
3. Install Poetry (a powerful tool for dependency management) [here](https://python-poetry.org/docs#installing-with-the-official-installer)
    - After running the installation, you'll need to add it to your path. The specific location depends on the OS and your shell config file.
4. Install Package Dependencies:
    - `poetry install`
5. Install Docker

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

### Starting the Local Postgres Docker Container

This command will start postgres locally (add the flag `-d` to run in detached mode)
```bash
docker compose up
```

This command will stop the postgres locally:
```bash
docker compose down
```


### Starting the Discord Bot

I made a script to simplify starting the bot.

```bash
poetry run start
```

If you want to run the Discord bot and connect to the production database, add the flag `USE_PROD_DB=true` to the beginning:
```bash
USE_PROD_DB=true poetry run start
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

### Poetry Scripts

Run `poetry run style` to auto-fix any style issues. Adding `--check` will throw an error if a style issue exists but not fix it.

## Hardware:

Developed on Ubuntu (WSL-2 specifically) and Mac.

## Development Notes

I referenced the instructions [here](https://discordpy.readthedocs.io/en/stable/intro.html#installing) for installing the dependencies of the Discord bot.

