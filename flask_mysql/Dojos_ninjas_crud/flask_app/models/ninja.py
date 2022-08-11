
from flask_app.config.mysqlconnection import connectToMySQL




DATABASE = 'dojos_and_ninjas'
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        ninja = Ninja(results[0])
        return ninja

    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO ninjas ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
    #     return connectToMySQL('ninjas').query_db( query, data )

    # @classmethod
    # def destroy(cls, data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)