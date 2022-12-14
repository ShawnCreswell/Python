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

from wsgiref import validate


users_list = [
    {'first': 'Tre', 'last': 'Mays', 'email': 'tdog@hotmail.com'},
    {'first': 'Lucie', 'last': 'chevreuil', 'email': 'lc@hotmail.com'},
    {'first': 'Nisrine', 'last': 'Kane', 'email': 'nk@gmail.com'},
    {"first": '4', 'last': 42, 'email': 'hi mom'},
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
            if not User.validate_user(user_in_list):
                print('sorry, invalid')
            cls.users.append(User(user_in_list))

    @staticmethod
    def validate_user(user: dict) -> bool:
        is_valid = True
        if len(user['first']) < 2:
            is_valid = False
        if len(user['last']) < 2:
            is_valid = False
        return is_valid


if not User.validate_user(users_list[-1]):
    print("Sorry, D! you need a longer name")

user1 = User(users_list[0])
user2 = User(users_list[1])

user_instances = User.register(users_list)
