
from flask_app.config.mysqlconnection import connectToMySQL




DATABASE = 'recipes'
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under = data['under']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! Read ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes 

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        recipe = Recipe(results[0])
        return recipe

    # ! Create
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes (first_name, last_name, age, user_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(user_id)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    # ! Delete
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)

    # ! Update
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, user_id = %(user_id)s WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)