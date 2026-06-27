import os

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "recipes-dev-key")

bcrypt = Bcrypt(app)
DATABASE = os.getenv("MYSQL_DB", "recipes_schema_db")
