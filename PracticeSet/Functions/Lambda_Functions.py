# Lambda Functions

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax

# lambda arguments : expression


# x = lambda a : a + 5 

# print(x(5))
# 10

# Multiplication using 2 Argument 

# x = lambda a , b: a * b;

# print(x(10,10))


# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Use that function definition to make a function that always doubles the number you send in:

# def myfunc(n):
#     return lambda a : a * n

# mydoubler = myfunc(10)

# print(mydoubler(11))

# Note :- 

# Use lambda functions when an anonymous function is required for a short period of time.


# Lambda with Built-in Functions
    
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map()

# The map() function applies a function to every item in an iterable:


# numbers = [1,2,3,4,5,6,7,8,9,10]


# mydata = list(map(lambda x: x * 2, numbers))

# print(mydata)


# Using Lambda with filter()

# The filter() function creates a list of items for which a function returns True:

# numbers = [1,2,3,4,5,6,7,8,9,10]

# data = list(filter(lambda x: x % 2 !=0, numbers))

# print(data)
# [1, 3, 5, 7, 9]



# Sorted Method in a Lambda 

# Using Lambda with sorted()

# The sorted() function can use a lambda as a key for custom sorting:


# numbers = [("Atharva","24"),("Rohit","22"),("Mohit","25")]

# data = list(sorted(numbers, key=lambda x : x[1]))

# for x in numbers:
#     print("x =", x)
#     print("x[0] (name) =", x[0])
#     print("x[1] (age)  =", x[1])
#     print()



