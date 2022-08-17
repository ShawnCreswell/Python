from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import comment
from flask_app import flash

DATABASE = 'users_and_comments'


class Favorite:

    def __init__(self, data):
        self.id = data['id'],
        self.user_id = data['user_id'],
        self.comment_id = data['comment_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO favorites (user_id, comment_id) VALUES (%(user_id)s, %(comment_id)s);"
        connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM favorites WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        favorite = cls(result[0])
        return favorite

    @classmethod
    def get_all_non_faves(cls, data):
        query = "SELECT favorites.comment_id FROM favorites WHERE favorites.user_id != %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        non_faves = []
        for result in results:
            non_faves.append(result['comment_id'])
        return non_faves