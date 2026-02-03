# Change Tuple Values

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


# x = ("apple","banana","cherry")

# y = list(x)

# y[1] = "kiwi"

# x = tuple(y)

# print(x)


#  Add Items 

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list,
# add your item(s), and convert it back into a tuple.

# x = ("apple","banana","cherry")

# y = list(x)

# y.append("orange")

# x = tuple(y)

# print(x)


# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# thistuple = ("apple","banana","cherry")

# y = ("orange", )

# thistuple +=y

# print(thistuple) 

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.  


#  Remove Items 

# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround
# as we used for changing and adding tuple items:


# thistuple = ("apple","banana","Cherry")

# y = list(thistuple)

# y.remove("apple")

# thistuple = tuple(y)

# print(thistuple)


# The del keyword can delete the tuple completely:

thistuple = ("apple","banana","Cherry")

del thistuple

print(thistuple) #this will raise an error because the tuple no longer exists)