
from ast import And, Import
from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

from flask_app.models.magazine import Magazine
from pprint import pprint


DATABASE = 'user_and_magazines'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.magazines = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        user = User(result[0])
        return user


    @classmethod
    def get_one_with_magazines(cls, data):
        query = "SELECT * FROM users LEFT JOIN magazines ON users.id = magazines.user_id WHERE users.id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        user = User(results[0])
        for result in results:
            magazine_dict = {
                'id': result['magazines.id'],
                'title': result['title'],
                'info': result['info'],
                'user_id': result['user_id'],
                'created_at': result['magazines.created_at'],
                'updated_at': result['magazines.updated_at'],
            }
            user.magazines.append(Magazine(magazine_dict))
        print(user)
        return user


    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )


    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s ;"
        return  connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First Name must be at least 3 characters.", 'first_name')
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last Name must be at least 3 characters.", 'last_name')
        if not EMAIL_REGEX.match(user['email']): 
            is_valid = False
            flash("Invalid email address!", 'email')
        if user['password'] != user['password_confirm' ]:
            is_valid = False
            flash("Passwords must match", 'password')
        if len(user['password']) < 1:
            is_valid = False
            flash("Passwords must not be empty", 'password')
        
        return is_valid


    @staticmethod
    def validate_user_password( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['password']): 
            flash("Invalid password!", 'password')
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
