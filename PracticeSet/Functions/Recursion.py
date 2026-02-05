# Recursion is when a function calls itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.



# def countdown(n):
#     if n<=0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)


# Base Case and Recursive Case

# Every recursive function must have two parts:

# A base case - A condition that stops the recursion

# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.

# def factorial(n):
#     # Base Case 
#     if n == 0 or n == 1:
#         return 1
    
#     # Recursive Case 

#     else:
#         return n * factorial(n - 1)
# print(factorial(5))


# The base case is crucial. Always make sure your recursive function has a condition that will eventually be met

# Fibonacci Sequence

# The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:

# 0, 1, 1, 2, 3, 5, 8, 13, ...

# The sequence continues indefinitely, with each number being the sum of the two preceding ones.



# def fibonnaci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonnaci(n - 1) + fibonnaci(n - 2)
    

# data = int(input("Enter the Number :- "))
# result = fibonnaci(data)
# print(result)
    

# Recursion with Lists

# Recursion can be used to process lists by handling one element at a time:

# def sum_list(numbers):
#     if len(numbers) == 0:
#         return 0 
#     else:
#         return numbers[0] + sum_list(numbers[1:])

# mylist = [1,2,3,4,5]
# print(sum_list(mylist))



# Recursion Depth Limit

# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

# import sys

# print(sys.getrecursionlimit())

# If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

