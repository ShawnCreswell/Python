
# # # # print('Welcome to Python!')

# # # # print('This is a loop printing 5 times')
# # # # for x in range(1, 6):
# # # #     print(f'x is: {x}')

# # # # weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# # # # day = random.choice(weekdays)

# # # # print(f'Today is: {day}')

# # # # if day == 'Monday':
# # # #     print('It will be a long week!')
# # # # elif(day == 'Friday'):
# # # #     print('Woohoo, time for the weekend!')
# # # # else:
# # # #     print('Not quite there yet.')



# # # # print(type(24))
# # # # print(type(3.9))
# # # # print(type(3j))

# # # # int_to_float = float(35)
# # # # float_to_int = int(44.2)
# # # # int_to_complex = complex(35)
# # # # print(int_to_float)
# # # # print(float_to_int)
# # # # print(int_to_complex)
# # # # print(type(int_to_float))
# # # # print(type(float_to_int))
# # # # print(type(int_to_complex))

# # # # import random
# # # # print(random.randint(2,5)) # provides a random number between 2 and 5

# # # first_name = "Zen"
# # # last_name = "Coder"
# # # age = 27
# # # print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # # # output: My name is Zen Coder and I am 27 years old.
# # # print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # # # output: My name is 27 Zen and I am Coder years old.




# # ninjas = ['Rozen', 'KB', 'Oliver']
# # my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# # empty_list = []



# # fruits = ['apple', 'banana', 'orange', 'strawberry']
# # vegetables = ['lettuce', 'cucumber', 'carrots']
# # fruits_and_vegetables = fruits + vegetables
# # print(fruits_and_vegetables)
# # salad = 3 * vegetables
# # print(salad)

# # drawers = ["documents", "envelopes", "pens"]
    
# # # access the drawer with index of 0 and print value
# # print(drawers[0])  #prints documents
# # # access the drawer with index of 1 and print value
# # print(drawers[1]) #prints envelopes
# # # access the drawer with index of 2 and print value
# # print(drawers[2]) #prints pens
    
# # # replace "documents" with "tchotchkes"
# # drawers[0] = "tchotchkes"
# # print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# # # stores the value "tchotchkes" in a temporary variable.
# # top_contents = drawers[0]
    
# # # Replaces the value at index 1
# # # with whatever value is stored at index 0
# # drawers[1] = drawers[0]
# # print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

# # count = 0
# # while count <= 5:
# #     print("looping - ", count)
# #     count += 1

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

