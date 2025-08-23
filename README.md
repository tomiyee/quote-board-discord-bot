# Quote Board Discord Bot

Quote Board Discord Bot is a Discord bot for collecting, storing, and displaying memorable quotes from your server. It uses Discord.py, PostgreSQL (via Docker), and Poetry for dependency management.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Scripts](#scripts)
- [Docker & Database](#docker--database)
- [Testing](#testing)
- [Contributing](#contributing)
- [Troubleshooting & FAQ](#troubleshooting--faq)

## Features

- Add, store, and display quotes from Discord messages
- PostgreSQL database for persistent storage
- Easy-to-use command scripts
- Style checking and auto-formatting

## Setup Instructions

Follow these steps to set up your development environment:

1. **(Optional) Install PyEnv**

   - PyEnv helps manage multiple Python versions. See [PyEnv Installation Guide](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).
   - Example for Ubuntu:
     ```bash
     curl https://pyenv.run | bash
     # Follow the instructions to add pyenv to your shell config
     pyenv install 3.10.0
     pyenv global 3.10.0
     ```

2. **Install Poetry**

   - Poetry manages dependencies and scripts.
   - Install via official installer:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     # Add Poetry to your PATH (see installer output for details)
     poetry --version
     ```

3. **Install Project Dependencies**

   - Run in the project root:
     ```bash
     poetry install
     ```

4. **Install Docker**

   - Docker is required for running the PostgreSQL database locally.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)

5. **Configure Environment Variables**
   - If needed, create a `.env` file in the project root for secrets (e.g., Discord bot token, database URL).
   - Example:
     ```env
     DISCORD_TOKEN=your_token_here
     DATABASE_URL=postgresql://user:password@localhost:5432/quotes
     ```

## Project Structure

```
/quote-board-discord-bot
├── quote_bot/           # Main bot source code
│   ├── __init__.py      # Package init
│   ├── database.py      # Database connection and models
│   ├── main.py          # Bot entry point
│   ├── parser.py        # Message parsing logic
│   └── discord_components/
│       ├── client.py    # Discord client setup
│       └── DiscordButtons.py # UI components for Discord
├── scripts/             # Utility scripts
│   ├── start.py         # Bot start script
│   └── style.py         # Style checker/formatter
├── tests/               # Test files
│   └── parser.py        # Parser tests
├── docker-compose.yaml  # Docker config for Postgres
├── pyproject.toml       # Poetry config
├── poetry.lock          # Poetry lock file
├── README.md            # This file
└── setup.cfg            # Additional config
```

## Usage

### Starting the Local Postgres Docker Container

Start Postgres locally (add `-d` to run in detached mode):

```bash
docker compose up
```

Stop Postgres:

```bash
docker compose down
```

### Starting the Discord Bot

Use the provided script to start the bot:

```bash
poetry run start
```

To connect to the production database:

```bash
USE_PROD_DB=true poetry run start
```

### Adding a New Dependency

Add a dependency:

```bash
poetry add <dependency>
```

Add a dev dependency:

```bash
poetry add <dependency> --group=dev
```

### Adding a Poetry Script

Define a new script in `pyproject.toml` under `[tool.poetry.scripts]`:

```
[tool.poetry.scripts]
style = "scripts.style:main"
```

This lets you run:

```bash
poetry run style
```

## Scripts

- `scripts/start.py`: Entry point for starting the bot. Handles environment setup and launches the Discord bot.
- `scripts/style.py`: Runs style checks and auto-formatting. Use `poetry run style --check` to check for issues without fixing.

## Docker & Database

- The bot uses PostgreSQL for persistent storage. The Docker Compose file sets up a local database for development.
- Default connection settings are in your environment variables or can be configured in `docker-compose.yaml`.

## Testing

- Tests are located in the `tests/` directory.
- To run all tests:
  ```bash
  poetry run pytest
  ```
- To run a specific test file:
  ```bash
  poetry run pytest tests/parser.py
  ```

## Contributing

1. Fork and clone the repository.
2. Install dependencies as described above.
3. Create a new branch for your feature or fix.
4. Make your changes and commit.
5. Push your branch and open a pull request.

## Troubleshooting & FAQ

**Q: Poetry can't find my Python version?**
A: Make sure you have the correct Python version installed and available in your PATH. Use PyEnv if needed.

**Q: Docker won't start Postgres?**
A: Check Docker is running and ports are available. Use `docker ps` to see running containers.

**Q: Bot won't start / can't connect to Discord?**
A: Ensure your Discord token is set in the environment and valid. Check for typos in `.env`.

**Q: How do I add a new command to the bot?**
A: Add your command logic in `quote_bot/main.py` or a new module, then register it with the Discord client in `discord_components/client.py`.

**Q: How do I run style checks?**
A: Run `poetry run style` to auto-fix, or `poetry run style --check` to only check.

## References

- [Discord.py Quickstart](https://discordpy.readthedocs.io/en/stable/quickstart.html)
- [Poetry Documentation](https://python-poetry.org/docs/)

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
