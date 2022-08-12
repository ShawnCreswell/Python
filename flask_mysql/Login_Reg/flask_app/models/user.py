from operator import imod
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re



DATABASE = 'login_reg'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        user = User(results[0])
        return user

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("email must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_email( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_password( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['password']): 
            flash("Invalid password!")
            is_valid = False
        return is_valid
    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(email)s, %(password)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     print(results)
    #     user = User(results[0])
    #     return user

        # if not EMAIL_REGEX.match(user['email']):
        #     flash("Email must be at least 3 characters.")
        #     is_valid = False