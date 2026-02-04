# Removing Items

# There are several methods to remove items from a dictionary:


# The pop() method removes the item with the specified key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.pop("model")
# print(thisdict)

# {'brand': 'Ford', 'year': 1964}


# (IMP)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):


# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# thisdict.popitem()
# print(thisdict)

# {'brand': 'Ford', 'model': 'Mustang'}


# del Keyword 

# The del keyword removes the item with the specified key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# del thisdict["model"]

# print(thisdict)

# {'brand': 'Ford', 'year': 1964}


# The del keyword can also delete the dictionary completely:

# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# del thisDict

# print(thisDict) #this will cause an error because "thisdict" no longer exists.


# ( IMP ) 

# The clear() method empties the dictionary:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
#   }

# thisdict.clear()
# print(thisdict)

# {}