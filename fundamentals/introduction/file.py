num1 = 42 #variable declaration, integer
num2 = 2.3 #variable declaration, float
boolean = True #variable declaration, boolean
string = 'Hello World'#variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Dictionries
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Tuples
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, string
print(type(fruit)) #Log statment, Type check
print(pizza_toppings[1]) #Log statment, access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #Lg statment, access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value
print(fruit[2]) #Log statmtent, access value

if num1 > 45: #if 
    print("It's greater")#log statment
else: #else
    print("It's lower")#log statment

if len(string) < 5: #if
    print("It's a short word!") #log statment
elif len(string) > 15: #else if
    print("It's a long word!") #log statment
else: #else
    print("Just right!") #log statment

for x in range(5): #for loop, start at 0 stop at 5
    print(x) #log statment
for x in range(2,5): #for loop, start at 2 stop at 5
    print(x) #log statment
for x in range(2,10,3):#for loop start at 2 stop at 10, increment by 3
    print(x) #log statment
x = 0
while(x < 5): #start at 0 stop at 5 
    print(x) #log statment
    x +=  #increment by 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1)#delete value

print(person)#log statment
person.pop('eye_color')#delete value
print(person)#log statment

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #boolean
        continue #continue
    print('After 1st if statement') #log statment
    if topping == 'Olives':#boolean
        break #break

def print_hello_ten_times():  #function
    for num in range(10): #parameter
        print('Hello') #return

print_hello_ten_times() #argument

def print_hello_x_times(x): #function
    for num in range(x):  #parameter
        print('Hello') #return

print_hello_x_times(4) #argument

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #parameter
        print('Hello') #return

print_hello_x_or_ten_times()#argument
print_hello_x_or_ten_times(4)#argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)