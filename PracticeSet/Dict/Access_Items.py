# Access Dictionary Items

# Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
#   }
# x = thisdict["model"]
# print(x)


# (IMP)

# There is also a method called get() that will give you the same result:

# (Note :- )
#  Using a get method if the key is wrong then also it will no show error there 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1
# }

# x = thisdict.get("model")
# print(x)


# (IMP)

# Get Keys

# The keys() method will return a list of all the keys in the dictionary.

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = thisdict.keys()
# print(x)
# dict_keys(['brand', 'model', 'year'])


# (IMP)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x)  # before the change 

# car["color"] = "white"

# print(x)  # after the change"

# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])

# Get Values

# The values() method will return a list of all the values in the dictionary.


# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }


# x = thisdict.values()
# print(x)
# dict_values(['Ford', 'Mustang', 1964])


# (IMP)
# Add a new item to the original dictionary, and see that the values list gets updated as well:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x)  # before the change

# car["color"] = "red"

# print(x)  # after the change

# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 1964, 'red'])


# Get Items

# The items() method will return each item in a dictionary, as tuples in a list.

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = thisdict.items()
# print(x)

# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# The items() method will return each item in a dictionary, as tuples in a list.


# Check if Key Exists

# To determine if a specified key is present in a dictionary use the in keyword:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Update Dictionary

# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.update({"color":'red'})

# print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


