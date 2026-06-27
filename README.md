# Recipes

Recipes is a Flask and MySQL application for managing recipe records behind authenticated user accounts.

## Product problem

A recipe workflow is a clean way to show real backend fundamentals: users, records, validation, create and edit screens, dashboards, detail pages, and database backed ownership.

## What it shows

| Area | Evidence |
| --- | --- |
| Authentication | Registration, login, bcrypt password hashing, sessions, and protected dashboard access. |
| CRUD workflow | Recipe creation, recipe editing, detail views, and user linked records. |
| MVC structure | Controllers, models, templates, static assets, app config, and database connection code. |
| Hospitality domain fit | Recipes connect naturally to Gokhan's operations background while still proving backend execution. |

## Stack

Python, Flask, Jinja2, MySQL, PyMySQL, Flask Bcrypt, HTML, CSS.

## Run locally

1. Create a MySQL database named `recipes_schema_db`.
2. Copy `.env.example` to `.env` and update the values.
3. Install dependencies and start the app.

```bash
pipenv install
pipenv shell
python server.py
```

## Environment variables

| Variable | Purpose |
| --- | --- |
| `FLASK_SECRET_KEY` | Session signing key. |
| `MYSQL_HOST` | Database host. |
| `MYSQL_USER` | Database username. |
| `MYSQL_PASSWORD` | Database password. |
| `MYSQL_DB` | Database name. |

## Hiring signal

This repo is a simple, reviewable proof of backend fundamentals: authentication, session state, form handling, data models, controller routes, and template based UI.
