# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python

# Python has a built-in package called json, which can be used to work with JSON data.


# ( IMP )

# Parse JSON - Convert from JSON to Python

# If you have a JSON string, you can parse it by using the json.loads() method.

# The result will be a Python dictionary.

# import json 

# # some json 

# data = '{ "name":"Atharva" , "age":30,"address":"N-5 CIDCO Auronday Colony Sambhajinagar" }'

# y = json.loads(data)

# print(y)

# #  The Result will be in a Dict

# print(y["name"])


# Convert from Python to JSON

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# import json 

# # a Python Object 

# x = {
#     "name":"Atharva",
#     "age":30,
#     "city":"New York"
# }


# ans = json.dumps(x)

# print(ans)




# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))



# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))



# ( IMP )

# Format the Result

# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:




# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# #  Indent ( Imp )
# print(json.dumps(x, indent=4))

#  Output :- 

# {
#     "name": "John",
#     "age": 30,
#     "married": true,
#     "divorced": false,
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "pets": null,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ]
# }


# ( IMP )

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=4, separators=(".","=")))



# {
#     "name"="John".
#     "age"=30.
#     "married"=true.
#     "divorced"=false.
#     "children"=[
#         "Ann".
#         "Billy"
#     ].
#     "pets"=null.
#     "cars"=[
#         {
#             "model"="BMW 230".
#             "mpg"=27.5
#         }.
#         {
#             "model"="Ford Edge".
#             "mpg"=24.1
#         }
#     ]
# }



# Order the Result

# The json.dumps() method has parameters to order the keys in the result:


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=4, sort_keys=True))


#  Output 

# {
#     "age": 30,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ],
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "divorced": false,
#     "married": true,
#     "name": "John",
#     "pets": null
# }