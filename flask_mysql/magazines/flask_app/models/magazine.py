from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import user




DATABASE = 'user_and_magazines'

class Magazine:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.info = data['info']
        self.user_id = data['user_id']
        if 'first_name' in data:    
            self.first_name = data ['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! Read ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM magazines;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        magazines = []
        for magazine in results:
            magazines.append( cls(magazine) )
        return magazines 


   

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM magazines JOIN users ON magazines.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        magazines =[]
        for magazine in results:
            magazines.append(cls(magazine))
        return magazines

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one_magazine(cls, data):
        query = "SELECT * FROM magazines WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        magazine = Magazine(results[0])
        return magazine

    @classmethod
    def get_one_with_users(cls, data):
        # query = "SELECT * FROM magazines LEFT JOIN users ON magazines.user_id = user.id WHERE users.id = %(id)s ;"
        query = "SELECT * FROM magazines LEFT JOIN users ON magazines.user_id = user.id WHERE users.id  ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        magazine = cls(results[0])
        for result in results:
            user_data = {
                'id': result['users.id'],
                'first_name': result['first_name'],
                'last_name ': result['last_name'],
                'created_at': result['magazines.created_at'],
                'updated_at': result['magazines.updated_at'],
            }
        if result['first_name']:
            magazine.users.append(user(user_data))
        print(magazine)
        return magazine

    # ! Create
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO magazines (title, info, user_id, created_at, updated_at ) VALUES ( %(title)s, %(info)s ,%(user_id)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )
    

    # ! Delete
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM magazines WHERE id = %(id)s ;"
        return  connectToMySQL(DATABASE).query_db(query, data)

    # ! Update
    @classmethod
    def update2(cls, data):
        query = "UPDATE magazines SET title = %(title)s, info = %(info)s, user_id = %(user_id)s WHERE id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def update_like(cls, data):
    #     query = "UPDATE magazines SET magazines.like = %(like)s + 1  WHERE id = %(id)s ;"
    #     return  connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_thought(magazine):
        is_valid = True
        if len(magazine['title']) < 3:
            is_valid = False
            flash("Magazine must be at least 3 characters.", 'title')
        if len(magazine['info']) < 3:
            is_valid = False
            flash("Magazine must be at least 3 characters.", 'info')
        return is_valid
    
