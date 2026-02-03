# Copy a List

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Use the copy() method

# You can use the built-in List method copy() to copy a list.

# thisList = ["apple","banana","cherry"]

# mylist = thisList.copy()

# print(mylist)
# print(thisList)



# Use the list() method

# Another way to make a copy is to use the built-in method list().

# thisList = ["apple","banana","cherry"]

# myList = list(thisList)

# print(myList)
# print(thisList)



# Use the slice Operator

# You can also make a copy of a list by using the : (slice) operator.


thisList = ["apple","banana","cherry"]

myList = thisList[:]

print(myList)
print(thisList)
# ['apple', 'banana', 'cherry']
# ['apple', 'banana', 'cherry']