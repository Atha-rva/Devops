# Set

# Sets are used to store multiple items in a single variable.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# thisset = {"apple","banana","cherry"}

# print(thisset)


# Set Items

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered

# Unordered means that the items in a set do not have a defined order.

# Unchangeable

# Set items are unchangeable, meaning that we cannot change the items after the set has been created.


# Duplicates Not Allowed

# Sets cannot have two items with the same value.

# thisset = {"apple","banana","cherry","apple"}

# print(thisset)

# Duplicate values will be ignored:
# {'banana', 'cherry', 'apple'}


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates

# thisset = {"apple", "banana", "cherry", True, 1}

# print(thisset)
# print(type(thisset))


# Get the Length of a Set

# To determine how many items a set has, use the len() function.

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# 3 

# Set Items - Data Types

# Set items can be of any data type:

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

# print(set1)
# print(set2)
# print(set3)

#  It Can Contain a Mixed DataType also 

# set1 = {"abc", 34, True, 40, "male"}
# print(set1)


# type()

# From Python's perspective, sets are defined as objects with the data type 'set':

# myset = {"apple", "banana", "cherry"}
# print(type(myset))


# The set() Constructor

# It is also possible to use the set() constructor to make a set.

thisset = set(("apple","banana","cherry"))
print(thisset)
print(type(thisset))