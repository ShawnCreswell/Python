# #1. Update Values in Dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# #1
x[1][0]= 15
print(x)
# #2
students[0]["last_name"] = "bryant"
print(students)
# #3
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# #4
z = [ {'x': 10, 'y': 30} ]
print(z)
# print(z) 

#2. Iterate through a list of dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for some_list in students:
        print('first name -', some_list['first_name'],'last name -',some_list['last_name'])

iterateDictionary(students)

#3 Get Values from a list of dictionaries

def iterateDictionary2(key_name, students):
    for person in students:
        print(person[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(len(dojo["locations"]), "Locations")
    for places in dojo['locations']:
        print(places)  
    print(len(dojo['instructors']), "Instructors")
    for people in dojo['instructors']:
        print(people)

printInfo(dojo)