# *args and **kwargs

# By default, a function must be called with the correct number of arguments.

# However, sometimes you may not know how many arguments that will be passed into your function.

# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.

# This way, the function will receive a tuple of arguments and can access the items accordingly:

# def my_function(*kids):
#     print("The youngest child is :- "+kids[2])

# my_function("Emil","Tobias","@@@","Daa")

# Arbitrary Arguments are often shortened to *args in Python documentation.


# What is *args?

# The *args parameter allows a function to accept any number of positional arguments.

# Inside the function, args becomes a tuple containing all the passed arguments:


# def my_function(*args):
#     print("Type: ",type(args))
#     print("First Arguement :-",args[0])
#     print("Second Argument :- ",args[1])
#     print("All Arguments :- ",args)

# my_function("Emil","Tobias","Linus")

# Type:  <class 'tuple'>
# First Arguement :- Emil
# Second Argument :-  Tobias
# All Arguments :-  ('Emil', 'Tobias', 'Linus')


