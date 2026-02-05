# Python - Loop Lists

# Loop Through a List

# You can loop through the list items by using a for loop:

# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango","pineapple","papaya","watermelon","guava"]

# for x in thisList:
#     print(x)


# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.


# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango","pineapple","papaya","watermelon","guava"]

# for i in range(len(thisList)):
#     print("",i,")",thisList[i])

#  0 ) apple
#  1 ) banana
#  2 ) cherry
#  3 ) orange
#  4 ) kiwi
#  5 ) melon
#  6 ) mango
#  7 ) pineapple
#  8 ) papaya
#  9 ) watermelon
#  10 ) guava



# While Using a While Loop 

# myList=["apple","banana","cherry"]
# i=0
# while i<len(myList):
#     print(myList[i])
#     i+=1

# apple
# banana
# cherry


# Looping Using List Comprehension

# List Comprehension offers the shortest syntax for looping through lists:


# thisList = ["apple","banana","cherry"]

# [print(x) for x in thisList]

# apple
# banana
# cherry


# for x in ["apple","banana","cherry"]:
#     print(x)

# apple
# banana
# cherry


# List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.


# mylist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
# newlist = []

# for x in mylist:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

# ['apple', 'banana', 'orange', 'mango']


# Using a List Campresion 


# myList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# newList = [x for x in myList if "a" in x]

# print(newList)

# ['apple', 'banana', 'orange', 'mango']


# The Syntax
# newlist = [expression for item in iterable if condition == True]



# myList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# newlist = [x for x in myList if x!="apple"]

# print(newlist)

# ['banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# for x in newlist:
#     if "apple" in x:
#         print(True)
#         break;
#     else:
#         print(False)
#         break;


# with no if Statement 

# myList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# newList = [x for x in myList]

# print(newList)

# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']



#  using a range Function 

# Iterable

# The iterable can be any iterable object, like a list, tuple, set etc.

# newList = [x for x in range(10) ]

# print(newList)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# newlist = [x for x in range(10) if x<5]
# print(newlist)

# [0, 1, 2, 3, 4]


# Expression

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# myList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# newList = [x.upper() for x in myList]

# print(newList)
# ['APPLE', 'BANANA', 'CHERRY', 'ORANGE', 'KIWI', 'MELON', 'MANGO']



#  Using a String also

# Set all values in the new list to 'hello':

# fruits = ["apple","banana","cherry","orange","kiwi","melon","mango"]


# newList = ['hello' for i in fruits]

# print(newList)
# ['hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello']


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# Return "orange" instead of "banana":

# myList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# newList = [x if x!="banana" else "orange" for x in myList]

# print(newList)

# ['apple', 'orange', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# Return the item if it is not banana, if it is banana return orange".