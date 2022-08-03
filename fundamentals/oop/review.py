# class Bird:
#     def __init__(self, color, wingspan, noise, has_fight = True):
#         self.color = color
#         self.wingspan = wingspan
#         self.has_flight = has_fight
#         self.noise = noise

#     def make_noise(self):
#         print(self.noise)
    
# tweetie = Bird('yellow', 'small', 'tweet')
# raven = Bird('black', 'big and nasty', 'squawk')

users_list = [
    {'first': 'Tre', 'last': 'Mays', 'email': 'tdog@hotmail.com'},
    {'first': 'Lucie', 'last': 'chevreuil', 'email': 'lc@hotmail.com'},
    {'first': 'Nisrine', 'last': 'Kane', 'email': 'nk@gmail.com'},
]

class User:

    users = []

    def __init__(self, data):
        self.first = data['first']
        self.last = data['last']
        self.email = data['email']
        
    def login(self):
        print(f"Welcome {self.first}")

    @classmethod
    def register(cls, the_list):
        for user_in_list in the_list:
            cls.users.append(User(user_in_list))
        
    
user1 = User(users_list[0])
user2 = User(users_list[1])

user_instances = User.register(users_list)