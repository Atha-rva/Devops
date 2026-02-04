# Remove Set Items

# To remove an item in a set, use the remove(), or the discard() method.

# thisset = {"apple","banana","cherry"}

# thisset.remove("banana")

# print(thisset)
# {'cherry', 'apple'}


# If the Element to remove in a set dosnot exist then it will give error 

# thisset = {"apple","banana","cherry"}

# thisset.remove("pinapple")

# print(thisset)
# KeyError: 'pinapple'


# remove "banana" by using the discard() method:


# thisset = {"apple","banana","cherry","mango"}

# thisset.discard("banana")

# print(thisset)
# {'cherry', 'apple', 'mango'}

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# thisset = {"apple","banana","cherry","mango"}

# thisset.discard("pinapple")

# print(thisset)
# {'cherry', 'mango', 'apple', 'banana'}


# you can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.


# thisset = {"apple","banana","cherry","mango"}

# x = thisset.pop()

# print(x)
# print(thisset)

# banana
# {'mango', 'cherry', 'apple'}


# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.



# The clear() method empties the set:

# thisset = {"apple","banana","cherry","mango"}

# thisset.clear()

# print(thisset)

# set()


# The del keyword will delete the set completely:


# thisset = {"apple","banana","cherry","mango"}

# del thisset

# print(thisset)

#    print(thisset)
#           ^^^^^^^
# NameError: name 'thisset' is not defined
