# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module

# Python has a built-in package called re, which can be used to work with Regular Expressions.


# (IMP)
# Import the re module


# RegEx in Python

# When you have imported the re module, you can start using regular expressions:

# import re

# #Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")



# RegEx Functions

# The re module offers a set of functions that allows us to search a string for a match:


# Function	Description

# findall :-	Returns a list containing all matches
# search :- 	Returns a Match object if there is a match anywhere in the string
# split  :- 	Returns a list where the string has been split at each match
# sub 	:-     Replaces one or many matches with a string


# Flags

# You can add flags to the pattern when using regular expressions.


# Special Sequences

# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# The findall() Function

# The findall() function returns a list containing all matches.


# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)



# The list contains the matches in the order they are found.

# If no matches are found, an empty list is returned:

# import re

# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)

# The search() Function

# The search() function searches the string for a match, and returns a Match object if there is a match.


# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())


# If no matches are found, the value None is returned:



# The split() Function

# The split() function returns a list where the string has been split at each match:


# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)


# You can control the number of occurrences by specifying the maxsplit parameter:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)

