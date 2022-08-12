
from ast import Import
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja
from pprint import pprint


DATABASE = 'dojos_and_ninjas'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(result[0])
        return dojo


    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        dojo = Dojo(results[0])
        for result in results:
            ninja_dict = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'age': result['age'],
                'dojo_id': result['dojo_id'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at'],
            }
            dojo.ninjas.append(Ninja(ninja_dict))
        return dojo
        print(dojo)

    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
    #     return connectToMySQL(DATABASE).query_db(query, data )

    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
    # @classmethod
    # def destroy(cls, data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)