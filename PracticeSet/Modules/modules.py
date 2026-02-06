# What is a Module?

# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.


# Create a Module

# 1. What is a Module in Python?

# A module is just a Python file with .py extension that contains:

# * functions
# * variables
# * classes

# Example file:

# math_utils.py


# Inside it:

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b


# This file itself is a module.

# 2. How to use a Module

# Create another file:

# main.py

# import math_utils

# print(math_utils.add(5, 3))
# print(math_utils.multiply(4, 2))


# Output:

# 8
# 8


# Python opens the toolbox and uses the tools inside.

# Note: When using a function from a module, use the syntax: module_name.function_name.



# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }


# Example

# Import the module named mymodule, and access the person1 dictionary:

# import mymodule

# a = mymodule.person1["age"]
# print(a)



# Naming a Module

# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module

# You can create an alias when you import a module, by using the as keyword:


# Create an alias for mymodule called mx:

# import mymodule as mx

# a = mx.person1["age"]
# print(a)


# Built-in Modules

# There are several built-in modules in Python, which you can import whenever you like.

# import platform

# x = platform.system()

# print(x)


# Using the dir() Function

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# import platform

# x = dir(platform)

# print(x)


# Note: The dir() function can be used on all modules, also the ones you create yourself.



# Import From Module

# You can choose to import only parts from a module, by using the from keyword.

# Example

# The module named mymodule has one function and one dictionary:

# def greeting(name):
#   print("Hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# Example

# Import only the person1 dictionary from the module:

# from mymodule import person1

# print (person1["age"])



# (IMP)
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]