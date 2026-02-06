# Python range

# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# This set of numbers has its own data type called range.

# Note: Immutable means that it cannot be modified after it is created.

# Creating ranges

# The range() function can be called with 1, 2, or 3 arguments, using this syntax:

# range(start, stop, step)


# The start argument is optional, and if not provided, it defaults to 0.

# range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).


# for i in range(10):
#     print(i)




# Using List to Display Ranges

# The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.

# print(list(range(5)))
# print(list(range(1,6)))
# print(list(range(5,20,3)))


# Slicing Ranges

# Like other sequences, ranges can be sliced to extract a subsequence.

# r = range(10)
# print(r[2])
# print(r[:3])


# Membership Testing

# Ranges support membership testing with the in operator.


# r = range(0, 10, 2)
# print(6 in r)
# print(7 in r)

# r = range(0,10,2)
# print(len(r))