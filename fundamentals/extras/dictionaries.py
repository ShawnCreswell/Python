# # #literal notation
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# capitals = {} #create an empty dictionary
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# print(capitals)
# person_2 = {"first_name": "Shawn", "last_name": "creswell", "age": 25, "is_organ_donor": True}

# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)

# print(person["first"])
# full_name = person["first"] + " " + person["last"]

# # will remove the key 'svk' and return it's value
# value_removed = capitals.pop('svk')
# print(capitals)
# # will delete the key, and not return anything
# del capitals['dnk']
# print(capitals)

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(each_key)
# # output: name, language

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(my_dict[each_key])
# # output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

