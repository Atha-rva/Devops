# Join Sets

# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.



# Union

# The union() method returns a new set with all items from both sets.


# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya"}


# set3 = set1.union(set2)

# print(set3)

# {'pinapple', 'cherry', 'papaya', 'mango', 'banana', 'apple'}


#  Union of set and List 

# set1 = {"apple","banana","cherry"}
# set2 = ["pinapple","mango","papaya"]


# set3 = set1.union(set2)

# print(set3)

# {'banana', 'cherry', 'apple', 'mango', 'pinapple', 'papaya'}


# Note 

# you can use the | operator instead of the union() method, and you will get the same result.


# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya"}


# set3 = set1 | set2 

# print(set3)


# (IMP)

# Join Multiple Sets

# All the joining methods and operators can be used to join multiple sets.

# When using a method, just add more sets in the parentheses, separated by commas:


# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {True,False}
# set4 = {"apple","banana","cherry"}
# set5 = {"pinapple","mango","papaya"}

# set6 = set1.union(set2,set3,set4,set5)

# print(set6)

# {False, 1, 2, 3, 'cherry', 'apple', 'papaya', 'mango', 'b', 'pinapple', 'banana', 'a', 'c'}

# It is Coming Like this Because sets are unordered 



# (IMP)

# When using the | operator, separate the sets with more | operators:


# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {True,False}
# set4 = {"apple","banana","cherry"}
# set5 = {"pinapple","mango","papaya"}

# set6 = set1 | set2 | set3 | set4 | set5


# print(set6)
# {False, 1, 2, 'a', 3, 'b', 'mango', 'cherry', 'pinapple', 'papaya', 'banana', 'apple', 'c'}



# (IMP)

# Join a Set and a Tuple

# The union() method allows you to join a set with other data types, like lists or tuples.

# set1 = {"a","b","c"}
# set2 = (1,2,3)

# set3 = set1.union(set2)

# print(set3)

# {1, 2, 3, 'b', 'a', 'c'}


# (IMP)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# set1 = {"a","b","c"}
# set2 = (1,2,3)

# set3 = set1 | set2

# print(set3)

# TypeError: unsupported operand type(s) for |: 'set' and 'tuple'



# Update

# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set1.update(set2)

# print(set1)

# {1, 2, 3, 'b', 'a', 'c'}


# (IMP)

# Note: Both union() and update() will exclude any duplicate items.


# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set1.update(set2)

# print(set1)
# {'pinapple', 'mango', 'banana', 'cherry', 'papaya', 'apple'}


# Intersection

# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1.intersection(set2)

# print(set3)

# {'banana'}


# (IMP)

# You can use the & operator instead of the intersection() method, and you will get the same result.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1 & set2

# print(set3)
# {'banana'}


# (IMP)

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# set1 = {"apple","banana","cherry"}
# set2 = ["pinapple","mango","papaya","banana"]

# set3 = set1 & set2

# print(set3)
# {'banana'}

#     set3 = set1 & set2
#            ~~~~~^~~~~~
# TypeError: unsupported operand type(s) for &: 'set' and 'list'


# (IMP)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set1.intersection_update(set2)

# print(set1)
# {'banana'}


# (IMP)

# The values True and 1 are considered the same value. The same goes for False and 0.


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)

# {False, 1, 'apple'}


# (IMP)
# Difference

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1.difference(set2)

# print(set3)
# {'cherry', 'apple'}


# (IMP)

# You can use the - operator instead of the difference() method, and you will get the same result.


# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1 - set2 

# print(set3)
# {'cherry', 'apple'}


# (IMP)

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# set1 = {"apple","banana","cherry"}
# set2 = ["pinapple","mango","papaya","banana"]

# set3 = set1 - set2

# print(set3)

#     set3 = set1 - set2
#            ~~~~~^~~~~~
# TypeError: unsupported operand type(s) for -: 'set' and 'list'


# (IMP)

# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.


# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set1.difference_update(set2)

# print(set1)
# {'cherry', 'apple'}


# (IMP)

# Symmetric Differences

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1.symmetric_difference(set2)

# print(set3)
# {'pinapple', 'mango', 'cherry', 'papaya'}



# (IMP)
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1 ^ set2

# print(set3)
# {'mango', 'papaya', 'apple', 'pinapple', 'cherry'}


# (IMP)

# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# set1 = {"apple","banana","cherry"}
# set2 = ["pinapple","mango","papaya","banana"]

# set3 = set1 ^ set2

# print(set3)

# TypeError: unsupported operand type(s) for ^: 'set' and 'list'


# (IMP)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

# set1 = {"apple","banana","cherry"}
# set2 = {"pinapple","mango","papaya","banana"}

# set1.symmetric_difference_update(set2)

# print(set1)
# {'papaya', 'mango', 'apple', 'pinapple', 'cherry'}