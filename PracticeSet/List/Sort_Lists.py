# Python Sort Lists 

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:



# sort list Alphanumerically


# thisList = ["orange","mango","kiwi","pineapple","banana"]

# thisList.sort()

# print(thisList)

# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']



# Sort the list numerically:

# thislist = [100,50,65,82,23]

# thislist.sort()

# print(thislist)

# [23, 50, 65, 82, 100]


# Sort Descending

# To sort descending, use the keyword argument reverse = True:

# thisList = ["orange","mango","kiwi","pineapple","banana"]

# thisList.sort(reverse=True)

# print(thisList)

# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


# thisList = [100,50,65,82,23]

# thisList.sort(reverse=True)

# print(thisList)
# [100, 82, 65, 50, 23]



# Customize Sort Function

# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):


# def myfunc(n):
#     return abs(n-50)

# thisList = [100,50,65,82,23]

# thisList.sort(key=myfunc)

# print(thisList)


# Case Insensitive Sort

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# thisList = ["banana","Orange","Kiwi","cherry"]

# thisList.sort()

# print(thisList)

# ['Kiwi', 'Orange', 'banana', 'cherry']


# if you want a case-insensitive sort function, use str.lower as a key function:

# thisList = ["banana","Orange","Kiwi","cherry"]

# thisList.sort(key=str.lower)

# print(thisList)

# Reverse Order

# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.

# thisList = ["banana","Orange","Kiwi","cherry"]

# thisList.reverse()

# print(thisList)

# ['cherry', 'Kiwi', 'Orange', 'banana']