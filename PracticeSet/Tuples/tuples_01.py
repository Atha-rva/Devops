# Tuple

# Tuples are used to store multiple items in a single variable.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.


# mytuple = ("apple","banana","cherry")
# print(mytuple)
# print(type(mytuple))

# ('apple', 'banana', 'cherry')
# <class 'tuple'>


# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.


#  tuples are ordered, it means that the items have a defined order, and that order will not change.

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# Allow Duplicates

# Since tuples are indexed, they can have items with the same value:

# thisTuple = ("apple","banana","cherry","apple","cherry")
# print(thisTuple)


# using len Function

# mytuple = ("apple","banana","cherry")
# print(len(mytuple))

# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# # tuple
# thistuple = ("apple",)
# print(type(thistuple))


# Tuple Items - Data Types

# Tuple items can be of any data type:

# String, int and boolean data types

# mytuple = ("apple","banana","cherry")
# print(mytuple)

#
# mytuple = (1,5,7,9,3)
# print(mytuple)

#
# mytuple = (True,False,False)
# print(mytuple)


#
# mytuple = ("abc",34,True,40,"male")
# print(mytuple)


# type()

# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# <class 'tuple'>


# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.


thistuple = tuple(("apple","banana","cherry"))
print(thistuple)
print(type(thistuple))

# ('apple', 'banana', 'cherry')
# <class 'tuple'>