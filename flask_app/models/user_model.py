from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app.models.recipe_model import Recipe

from flask_app import DATABASE, bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []

# validates user by email for login
    @classmethod
    def find_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)

        if results and len(results) > 0:
            found_user = cls(results[0])
            return found_user
        else:
            return False

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,%(email)s, %(password)s);"

        return connectToMySQL(DATABASE).query_db(query,data)


# validates login
    @classmethod
    def validate_login(cls, data):

        found_user = cls.find_by_email(data)

        if not found_user:
            flash("Invalid login...")
            return False
        elif not bcrypt.check_password_hash(found_user.password, data['password']):
            flash("Invalid login...")
            return False

        return found_user

#checks email duplication for registration
    @classmethod
    def unique_email(cls, data):
        is_valid = True
        query = "SELECT email FROM users WHERE email = %(email)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)

        if not results:
            return is_valid
        elif data['email'] in results[0]['email']:
            flash("Email already in use!")
            is_valid = False
        return is_valid

# Joins users and recipes together
    @classmethod
    def all_recipes_with_users(cls):
        query = "SELECT * FROM recipes left join users on recipes.user_id = users.id"
        results = connectToMySQL(DATABASE).query_db( query )
        all_recipes = []
        for row in results:
            one_recipe = Recipe(row)

            user_data = {
                "id" : row["users.id"],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_recipe.owner = cls(user_data)
            all_recipes.append(one_recipe)
        return all_recipes

    @classmethod
    def get_user_with_recipes( cls , data ):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )

        user = cls( results[0] )
        for row in results:

            recipe_data = {
                "id" : row['id'],
                "name" : row['name'],
                "description" : row['description'],
                "instructions" : row['instructions'],
                "under_30_minutes" : row['under_30_minutes'],
                "date_cooked" : row['date_cooked'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
                "user_id" : row['user_id']
            }
            user.recipes.append(Recipe(recipe_data))
        print(user.recipes)
        return user

    @staticmethod
    def validate(data):
        is_valid = True

# validates first name
        if len(data['first_name']) == 0:
            flash("Please provide a first name!")
            is_valid = False
        elif len(data["first_name"]) < 2:
            flash("User first name must be at least two characters")
            is_valid = False
        elif not data['first_name'].isalpha():
            flash("First name must only contain characters")
            is_valid = False

# validates last name
        if len(data['last_name']) == 0:
            flash("Please provide a last name!")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("User last name must be at least two characters")
            is_valid = False
        if not data['last_name'].isalpha():
            flash("last name must only contain characters")
            is_valid = False

#  validates email and password
        if len(data['email']) == 0:
            flash("Please provide an email!")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least eight characters")
            is_valid = False
        if data["password"] != data["confirm_password"]:
            flash("Passwords do not match!")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        if User.find_by_email(data):
            flash("Email is already registered!")
            is_valid = False

        return is_valid