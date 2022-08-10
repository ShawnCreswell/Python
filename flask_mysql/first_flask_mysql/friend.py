from mysqlconnection import connectToMySQL
DATABASE = 'first_flask'
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends