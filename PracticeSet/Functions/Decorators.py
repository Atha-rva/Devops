# Decorators let you add extra behavior to a function, without changing the function's code.

# A decorator is a function that takes another function as input and returns a new function.


# ( IMP )

# Basic Decorator

# Define the decorator first, then apply it with @decorator_name above the function.

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())


# By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.

# The function changecase is the decorator.

# The function myfunction is the function that gets decorated.


# Multiple Decorator Calls

# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

# def changecase(func):
#     def innerFunc():
#         return func().upper()
#     return innerFunc 


# @changecase 
# def myFunc():
#     return "Data Welcoming"

# @changecase
# def MyData():
#     return "Data Mining EveryWhere"

# print(myFunc())
# print(MyData())



# Arguments in the Decorated Function

# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:


# def changecase(func):
#     def innerDatafn(x):
#         return func(x).upper()
#     return innerDatafn

# @changecase
# def NameFn(name):
#     return f"Hello {name}"

# print(NameFn("Atharva Deshmukh"))


# *args and **kwargs

# Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

# def myfunction(func):
#     def innerFunc(*args,**krgs):
#         return func(*args,**krgs).upper()
#     return innerFunc

# @myfunction
# def dataFunc(name , middlename , lastname):
#     return f"Welcome to Streets {name} {middlename} {lastname}"

# print(dataFunc("Atharva", "Deelip" ,"Deshmukh"))

# WELCOME TO STREETS ATHARVA DEELIP DESHMUKH


# Decorator With Arguments

# Decorators can accept their own arguments by adding another wrapper level.

# def changecase(n):
#     def changecase(func):
#         def innerFunc():
#             if n == 1:
#                 a = func().lower()
#             else:
#                 a = func().upper()
#             return a 
#         return innerFunc
#     return changecase

# @changecase(1)
# def myDataFunc():
#     return "Hello Atharva"

# print(myDataFunc())





# Multiple Decorators

# You can use multiple decorators on one function.

# This is done by placing the decorator calls on top of each other.

# Decorators are called in the reverse order, starting with the one closest to the function.


# def changecase(func):
#     def inner():
#         return func().upper()
#     return inner

# def changeData(func):
#     def inner():
#         return func().lower()
#     return inner


# @changecase
# @changeData
# def FuncData():
#     return "Hello Welcome to Text"

# print(FuncData())
# print(FuncData())

# HELLO WELCOME TO TEXT
# HELLO WELCOME TO TEXT


# Preserving Function Metadata

# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# def myFunc():
#     return "You have a Nice Day"

# print(myFunc.__name__)
# print(myFunc.__doc__)

# myFunc
# None


# But, when a function is decorated, the metadata of the original function is lost.

# def changecase(func):
#     def inner():
#         return func().upper()
#     return inner 

# @changecase 
# def changeData():
#     return "Welcome to the Data"

# print(changeData.__name__)


# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.



# import functools

# def changecase(func):
#     @functools.wraps(func)
#     def inner():
#         return func().inner()
#     return inner 

# @changecase
# def myfunction():
#     return "Have a Great Day"

# print(myfunction.__name__)




