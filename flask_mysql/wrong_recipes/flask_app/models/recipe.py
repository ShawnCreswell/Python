from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
# import re

DATABASE = 'recipes'
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        recipe = Recipe(results[0])
        return recipe

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes ( name , description , instruction, date_made, created_at, updated_at ) VALUES ( %(name)s , %(description)s , %(instruction)s , %(date_made)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )