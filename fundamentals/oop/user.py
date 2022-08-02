class user:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(user_shawn.first_name)
        print(user_shawn.last_name)
        print(user_shawn.email)
        print(user_shawn.age)
        

    def enroll(self):
        self.is_reward_member = True
        self.gold_card_points = 200
        # user_shawn.is_reward_member = True
        # user_shawn.gold_card_points = 0
        return
    
    def spend_points(self, amount):
        self.gold_card_points -= 10


user_shawn = user("Shawn", "Creswell", "creswellshawn@gmail.com", 25)
print(user_shawn.display_info())
print(user_shawn.enroll())
print(user_shawn.enroll())

