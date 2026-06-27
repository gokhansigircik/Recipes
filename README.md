# Recipe Manager

A Flask and MySQL recipe manager with user authentication, recipe creation, editing, detail pages, and dashboard views.

## Product story

Recipe Manager turns a familiar hospitality domain into a full stack CRUD app. It fits Gokhan's background because recipes, prep, and operational consistency are part of restaurant life, while the implementation demonstrates backend fundamentals.

## What it demonstrates

| Area | Evidence |
| --- | --- |
| Authentication | Registration, login, bcrypt password hashing, sessions, and dashboard access. |
| CRUD workflow | Create, read, update, and view recipe records. |
| MVC structure | Controllers, models, templates, static styles, and shared app config. |
| Database integration | MySQL connection layer and model level queries. |

## Stack

Python, Flask, Jinja, MySQL, PyMySQL, Flask Bcrypt, HTML, CSS.

## Run locally

1. Install dependencies with Pipenv.
2. Create a MySQL database named `recipes_schema_db`.
3. Copy `.env.example` to `.env` and update the values.
4. Start the app.

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

## Next improvements

1. Add recipe categories and prep time filters.
2. Add screenshots of the recipe dashboard and detail page.
3. Add form validation tests.
4. Add schema and seed data for demo review.
5. Add deployment notes for a small Flask host.
