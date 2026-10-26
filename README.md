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

Generate table migration

- uv run alembic revision --autogenerate -m "create tasks table"

Apply the migration

- uv run alembic upgrade head

Check the applied migration

- uv run alembic current

Rollback the applied migration

- uv run alembic downgrade -1

Reset migration

- uv run alembic downgrade base

Check migrated tables

- uv run alembic history

Install pydantic settings to read env variables

- uv add pydantic-settings

Install authentication

- pyjwt (creates and verifies jwt)
- pwdlib[argon2] (securely hashes and verifies passwords)
- python-multipart (supports OAuth2 form-based login requests)
- uv add pyjwt "pwdlib[argon2]" python-multipart

Install pymsql when using mysql
- uv add pymsql
