class user:
    
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        
        

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - (amount)
        return self


user_shawn = user("Shawn", "Creswell", "creswellshawn@gmail.com", 25, False, 0)
# print(user_shawn.display_info())
user_shawn.enroll()
# print(user_shawn.display_info())

user_marcus = user("Marcus", "Creswell", "creswellmarcus@gmail.com", 22, False, 0)
user_sarina = user("Sarina", "Creswell", "creswellsarina@gmail.com", 28, False, 0)
user_marcus.spend_points(50)
user_sarina.enroll()

user_sarina.spend_points(80)
print(user_shawn.display_info())
print(user_marcus.display_info())
print(user_sarina.display_info())






