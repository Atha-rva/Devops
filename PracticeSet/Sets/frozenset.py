# Python frozenset

# * frozenset is an immutable version of a set.

# Like sets, it contains unique, unordered, unchangeable elements.

# Unlike sets, elements cannot be added or removed from a frozenset.


# x = frozenset({"apple","banana","cherry"})

# print(x)
# print(type(x))

# frozenset({'cherry', 'banana', 'apple'})


# Frozenset Methods

# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.


# 1) copy()	 	Returns a shallow copy

# fs = frozenset({"apple","banana","cherry"})
# x = fs.copy()
# print(x)
# frozenset({'cherry', 'apple', 'banana'})


# 2) difference()	-	Returns a new frozenset with the difference

# set1 = frozenset({"apple","banana","cherry"})
# set2 = {"pinapple","mango","papaya","banana"}

# set3 = set1.difference(set2)

# print(set3)
# frozenset({'cherry', 'apple'})


# 3) intersection()	 &	Returns a new frozenset with the intersection

# set1 = frozenset({"apple","banana","cherry"})
# set2 = frozenset({"pinapple","mango","papaya","banana"})

# set3 = set1.intersection(set2)

# print(set3)
# frozenset({'banana'})


# 4) isdisjoint()	 	Returns whether two frozensets have an intersection

# a = frozenset({1, 2})
# b = frozenset({3, 4})
# c = frozenset({2, 3})

# print(a.isdisjoint(b))
# # True
# print(a.isdisjoint(c))
# # False


# 5) issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another 

# a = frozenset({1, 2})
# b = frozenset({1, 2, 3})

# print(a.issubset(b))
# # True
# print(b.issubset(a))
# # False

# print(a <= b)
# print(a < b)


# 6 ) issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another

# a = frozenset({1, 2, 3})
# b = frozenset({1, 2})

# print(a.issuperset(b))
# # True

# print(b.issuperset(a))
# # False


# 7) symmetric_difference()	^	Returns a new frozenset with the symmetric differences


# a = frozenset({1,2,3,4})
# b = frozenset({3,4,5,6})

# c = a.symmetric_difference(b)

# print(c)
# frozenset({1, 2, 5, 6})


# 8) union()	|	Returns a new frozenset containing the union

# a = frozenset({1,2,3,4})
# b = frozenset({3,4,5,6})

# c = a.union(b)

# print(c)
# frozenset({1, 2, 3, 4, 5, 6})