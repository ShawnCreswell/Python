# This is a comment

my_name = "Shawn Creswell"

my_age = 8 #int

intrest_rate = .2 #float

my_age = "eight"

#lists
colors = ['red', 'blue', 'green']

#dictionaries
monster = {
    'id': 1,
    'name': 'Charizard',
    'types': ['fire', 'posion']
}

class Pet:
    def __init__(self, name):
        self.name = name

my_cat = Pet('patches')

print(my_cat.name)

print(monster['types'][0])

#function
  #start , end , increase by (0, 256, 2)--> (256)
def print_1_to_255():                 
    for i in range(1, 256, 1):     
        print(i)

#print_1_to_255

if 10 > 2:
    print('greater than')
elif 10 < 2:
    print('less than')

if '1' == 1:
     print('equal')
else:
    print('not equal')