# Local Scope

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# def  myfunc():
#     x = 300
#     print(x)

# myfunc()


# Function Inside Function

# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# def myfunc():
#     x = 300
#     def insidefunc():
#         print(x)
#     insidefunc()
# myfunc()


# x = 300
# def myfunc():
#     print(x)

# myfunc()

# print(x)


# Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.


# def myfunc():
#     global x 
#     x = 300

# myfunc()

# print(x)




# Nonlocal Keyword

# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.


# def myfunc1():
#     x = "Jane"
#     def myfunc2():
#         nonlocal x
#         x = "hello"
#     myfunc2()
#     return x
# print(myfunc1())





# The LEGB Rule

# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace


# x = "global"

# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print("Inner :- ",x)
#     inner()
#     print("Outer",x)

# outer()
# print("Global:",x)

