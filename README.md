Fast API Installation

Download UV

- powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Make UV available in terminal

- $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"

Create initial python files and configuration

- mkdir my-fastapi-app
- cd my-fastapi-app
- uv init

Installs FastAPI and records it as a project dependency

- uv add "fastapi[standard]"

Create file and simple api

- main.py

Run the project for development

- uv run fastapi dev src/my_fastapi_app_v2/main.py

Install package

uv add sqlalchemy alembic

- sqlalchemy (model)
- alembic (for migration)

uv add -D pytest httpx

- pytest (for testing)
- httpx2 (testing api endpoints) (dev)

Run Test

- uv run pytest -v

Initialize alembic

- uv run alembic init migrations
