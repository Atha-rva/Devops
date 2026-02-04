# Add Items

# Once a set is created, you cannot change its items, but you can add new items.

#  add() method.

# Add an item to a set, using the add() method:

# thisset = {"apple","banana","cherry"}

# thisset.add("orange")

# print(thisset)
# {'cherry', 'orange', 'apple', 'banana'}


# Add Sets

# To add items from another set into the current set, use the update() method.

# thisset = {"apple","banana","cherry"}
# tropical = {"pinapple","mango","papaya"}

# thisset.update(tropical)

# print(thisset)
# {'papaya', 'cherry', 'pinapple', 'mango', 'banana', 'apple'}


# Add Any Iterable

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# thisset = {"apple","banana","cherry"}
# myList = ["kiwi","orange"]

# thisset.update(myList)

# print(thisset)

# {'orange', 'banana', 'apple', 'kiwi', 'cherry'}