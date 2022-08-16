from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL




DATABASE = 'users_and_comments'
class Comment:
    def __init__( self , data ):
        self.id = data['id']
        self.text = data['text']
        self.like = data['like']
        self.user_id = data['user_id']
        if 'first_name' in data:    
            self.first_name = data ['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! Read ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        comments = []
        for comment in results:
            comments.append( cls(comment) )
        return comments 

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM comments JOIN users ON comments.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        comments =[]
        for comment in results:
            comments.append(cls(comment))
        return comments

    # ! READ/RETRIEVE ONE
    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM comments WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     print(results)
    #     comment = comment(results[0])
    #     return comment

    @classmethod
    def get_one_comment(cls, data):
        query = "SELECT * FROM comments WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        comment = Comment(results[0])
        return comment

    # ! Create
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO comments (text, user_id, created_at, updated_at ) VALUES ( %(text)s ,%(user_id)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    # ! Delete
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM comments WHERE id = %(id)s ;"
        return  connectToMySQL(DATABASE).query_db(query, data)

    # ! Update
    @classmethod
    def update2(cls, data):
        query = "UPDATE comments SET text = %(text)s, like = %(like)s, user_id = %(user_id)s WHERE id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update_like(cls, data):
        # query = "UPDATE comments SET like = %(like)s + 1  WHERE id = %(id)s ;"
        query = "UPDATE comments SET comments.like = %(like)s + 1  WHERE id = %(id)s"
        # UPDATE comments SET comments.like = comments.like + 1  WHERE id = 9
        return  connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_thought(comment):
        is_valid = True
        if len(comment['text']) < 4:
            is_valid = False
            flash("Thought must be at least 5 characters.", 'text')
        return is_valid
    




    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE comments SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)