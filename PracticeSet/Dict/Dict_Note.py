# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# Dictionary

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# Note :- 

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# print(thisDict)


# Dictionary Items

# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.


# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# print(thisDict["brand"])
# print(thisDict["model"])
# print(thisDict["year"])


# Changeable

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed

# Dictionaries cannot have two items with the same key:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)


#  Note :- 
# Dictionaries cannot have two items with the same key:
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Dictionary Length

# To determine how many items a dictionary has, use the len() function:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2
# }
# print(len(thisdict))


# Dictionary Items - Data Types

# The values in dictionary items can be of any data type:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)
# print(type(thisdict))

# type()

# From Python's perspective, dictionaries are defined as objects with the data type 'dict':

# <class 'dict'>

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))




# The dict() Constructor

# It is also possible to use the dict() constructor to make a dictionary.

# thisdict = dict(name="Atharva Deshmukh", age=22, country="India")
# print(thisdict)
# print(type(thisdict))

