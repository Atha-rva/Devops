# Python Functions

# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

# Creating a Function using a def keyword 



# def my_function():
#     print("Hello from a Function")

# my_function()


# You can call the same function multiple times:

# def my_function():
#   print("Hello from a function")

# my_function()
# my_function()
# my_function()


# Function Names

# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)


# Eg :- 

# calculate_sum()
# _private_function()
# myFunction2()


# def frahnit_to_celsius(fahranhit):
#     return (fahranhit - 32) * 5/9

# print(frahnit_to_celsius(77))
# print(frahnit_to_celsius(95))
# print(frahnit_to_celsius(50))


# Return Values

# Functions can send data back to the code that called them using the return statement.

# def get_greeting():
#     return "Hello from a Function"

# message = get_greeting()

# print(message)


# The pass Statement

# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

# def my_function():
#   pass



# Function Arguments

# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# def my_function(fname):
#     print(fname,"Refnes")

# my_function("Welcome to Streets")



# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

# def my_function(name): # name is a parameter
#   print("Hello", name)

# my_function("Emil") # "Emil" is an argument


# Default Parameter Values

# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

# def my_function(name="my friends"):
#     print("Hello",name)

# my_function("Emil")
# my_function("Tobias")
# my_function()


# Keyword Arguments

# You can send arguments with the key = value syntax.


# def my_animal(animal,name):
#     print("I Have a ",animal)
#     print("I Have a the following things",name)

# my_animal(name="Atharva Deshmukh", animal="Tigar")

# This way, with keyword arguments, the order of the arguments does not matter.

# my_animal(animal="Lion", name="Welcome to Text")



# Positional Arguments

# When you call a function with arguments without using keywords, they are called positional arguments.

# def my_function(animal,name):
#     print("I have a ",animal)
#     print("My",animal+"s name is",name)

# my_function("dog","Buddy")


# Passing Different Data Types

# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# def my_function(fruits):
#     for x in fruits:
#         print(x)

# fruits = ["apple","banana","cherry","mango"]

# my_function(fruits)


# using a Dict ( for Loop )

# def my_function(fruits):
#     for x in fruits:
#         print("My Name is ", fruits["name"])
#         print("My Age is ",fruits["age"])


# thisdict = {
#     "name":"Atharva",
#     "age":24
# }


# my_function(thisdict)


# Return Values

# Functions can return values using the return statement:


# def myfunction(x):
#     return x * x 

# ans = myfunction(10)

# print(ans)


# Returning Different Data Types

# Functions can return any data type, including lists, tuples, dictionaries, and more.

# def my_function():
#     return ["apple","mango","cherry","banana"]

# fruits = my_function()

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])


# def my_function():
#     return (10,20)

# x,y = my_function()
# print("x :- ",x)
# print("y :- ",y)


# Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:

# def my_function(name, /):
#     print("hello",name)

# my_function("Atharva")

# With , /, you will get an error if you try to use keyword arguments:


# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:

# def my_function(*,name):
#     print("Hello ",name)

# my_function(name="Atharva")



# Combining Positional-Only and Keyword-Only

# You can combine both argument types in the same function.

# Arguments before / are positional-only, and arguments after * are keyword-only:

# def my_function(a,b,/,*,c,d):
#     return a + b + c + d 

# result = my_function(5,10, c=15,d=20)

# print(result)

