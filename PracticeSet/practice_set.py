# import sys 

# print("Python version")
# print (sys.version)


# if 5>2:
#     print("Five is greater than two!")


# x = 5
# y = "Hello, World!"
# print(x)
# print(y)



# print("Hello, World!", end=" ")
# print("Hello, World!", end=" ")
# print("Hello, World!")


# print(3)
# print(2 + 3)
# print(2 * 3)
# print(3 / 2)
# print(3 ** 2)
# print(3 % 2)
# print(3 // 2)
# print(3 > 2)
# print(3 < 2)
# print(3 >= 2)
# print(3 <= 2)
# print(3 == 2)
# print(3 != 2)


# You Can Combine a number and string a in a print Statement Using a Comma

# print("Welcome to",2026,"Where we explore the future!")


# x = str(3)
# y = int(3)
# z = float(3)
# print(x)
# print(y)
# print(z)

# for x in "banana":
#     print(x)


# x = "banana"
# print(len(x))

# Using a ( in ) keyword 
#  To Check a String for a Certain Phrase, Use the in Keyword or not 

# a = "Hello, World!"
# print("Hello" in a )

# Using an ( if ) Statement to Check if a String Contains a Certain Phrase

# a = "Hello, World!"

# if "Hello" in a:
#     print("Yes, 'Hello' is present.")
# else:
#     print("No, 'Hello' is not present.")


# Check if NOT a Certain Phrase is Present in a String, Use the not in Keyword


# a = "Hello, World!"
# if "World" not in a:
#     print("No, 'World' is NOT present.")
# else:
#     print("Yes, 'World' is present.")


# Slicing of a String 

# b = "Hello, World!"

# print(b[2:5])
# print(b[:5])
# print(b[2:])

# # Negative Indexing 

# print(b[-5:-2])

# Strip Whitespace Characters from the Beginning or the End of a String
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# Python - Modify Strings

# a = "Hello, World!"
# print(a.upper()) # returns "HELLO, WORLD!"
# print(a.lower()) # returns "hello, world!"

# Strip function removes any whitespace from the beginning or the end:

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# Replace function replaces a string with another string:

# a = "Hello, World!"

# print(a.replace("H","J"))
# Jello, World!

# b = "Hello, World!"
# print(b.replace("Hello","Atharva"))


# Split function splits the string into substrings if it finds instances of the separator:

# a = "Hello@World!"
# print(a.split("@"))
# ['Hello', ' World!']


# Python - String Formatting

# age = 24
# txt = f"My Name is Atharva, and I am of a {age} years old."
# print(txt)


# Placeholders and Modifiers

# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals

# price = 45 
# txt = f"The price is {price:.2f} in dollars."
# print(txt)


#  Operations on a Formatted String 

# txt = f"The Price is {10 * 9} dollars"
# print(txt)


# Escape Character in Formatted Strings

# txt = f"Hello, \nWorld!"
# print(txt)


# txt = f"Hello, \"Atharva\" World!"
# print(txt)
# Hello, "Atharva" World!


# txt = f"Hello\rWorld!"
# print(txt)
# World!


# txt = f"Hello\tWorld!"
# print(txt)

# backspace escape character 

# txt = "Hello \bWorld!"
# print(txt) 
# HelloWorld!

# txt = "\110\145\154\154\157"
# print(txt) 

# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 


# Python - String Methods

# Converts the first character to upper case

# a = " hello, world! "
# print(a.capitalize()) # returns " hello, world! "

# # Converts string into lower case
# a = "Hello, World!"
# print(a.casefold()) # returns "hello, world!"

# # Returns a centered string
# a = "hello"
# print(a.center(20)) # returns "       hello        "

# Returns the number of times a specified value occurs in a string

# a = "hello, world!"
# print(a.count("o"))

# Returns an encoded version of the string

# a = "hello, Ståle!"
# print(a.encode()) # returns b'hello, St\xc3\xa5le!'

# 	Returns true if the string ends with the specified value

# a = "hello, world!"
# print(a.endswith("!"))

# Sets the tab size of the string

# a = "hello\tworld!"
# print(a.expandtabs(tabsize=10))

# Searches the string for a specified value and returns the position of where it was found

# a = "hello, world!"
# print(a.find("world!")) # returns 7

# 	Formats specified values in a string

# a = "Hello, {}. Welcome to {}"
# print(a.format("Atharva","2026"))

# Formats specified values in a string
# a = "Hello, {name}. Welcome to {year}"
# print(a.format_map({'name':"Atharva Deshmukh", 'year':"2026"}))

# 🎯 1. Positional formatting → .format()

# Uses numbers:

# "{0} {1}".format("A", "B")

# 🗺️ 2. Mapping (dictionary) formatting → .format_map()

# Uses keys:

# "{name}".format_map({"name": "Atharva"})


# 	Searches the string for a specified value and returns the position of where it was found

# a = "hello, world!"
# print(a.index("world!")) # returns 7


# 	Returns True if all characters in the string are alphanumeric

# a = "hello123"
# print(a.isalnum())


# Returns True if all characters in the string are in the alphabet

# a = "helloWorld"
# print(a.isalpha())


# 	Returns True if all characters in the string are ascii characters

# a = "helloWorld!"
# print(a.isascii())

# Returns True if all characters in the string are decimals

# a = "12345"
# print(a.isdecimal())

# Returns True if all characters in the string are digits

# a = "12345"
# print(a.isdigit())

# Returns True if the string is an identifier 

# a = "HelloWorld"
# print(a.isidentifier())

# Returns True if all characters in the string are lower case

# a = "hello World"
# print(a.islower())


# Returns True if all characters in the string are numeric

# a = "Welcome to Streets123"
# b = "12345"
# print(a.isnumeric())
# print(b.isnumeric())


# Returns True if all characters in the string are printable

# a = "Hello World!"
# print(a.isprintable())

# 	Returns True if all characters in the string are whitespaces

# a = "        "
# b = "       a"

# print(a.isspace())
# print(b.isspace())

# Returns True if the string follows the rules of a title

# a = "Hello World!"
# print(a.istitle())


# Returns True if all characters in the string are upper case

# a = "HELLO WORLD!"
# print(a.isupper())


# Joins the elements of an iterable to the end of the string

# myTuple = ("Atharva", "Deshmukh", "2026")
# x = " ".join(myTuple)
# print(x)


# Returns a left justified version of the string

# a = "hello"
# print(a.ljust(20)) # returns "hello               "

# 	Converts a string into lower case

# a = "Hello, World!"
# print(a.lower()) # returns "hello, world!"

# Returns a left trim version of the string

# a = "     hello, world!     "
# print(a.lstrip()) # returns "hello, world!     "

# Returns a translation table to be used in translations

# a = 'hello, world!'
# print(a.maketrans("h","H"))
# returns {104: 72}


# Returns a tuple where the string is parted into three parts

# a = "hello, world!"
# print(a.partition(",")) # returns ('hello', ',', ' world!')

# 	Returns a string where a specified value is replaced with a specified value

# a = "hello, world!"
# print(a.replace("h","H")) # returns "Hello, world!"

# 	Searches the string for a specified value and returns the last position of where it was found

# a = "hello, world! world!"
# print(a.rfind("world!"))


# 	Searches the string for a specified value and returns the last position of where it was found

# a = "hello, world! world!"
# print(a.rindex("world!"))  # returns 14

# Returns a right justified version of the string

# a = "hello",
# print(a.rjust(20)) # returns "               hello"

# Returns a tuple where the string is parted into three parts

# a = "hello, world!"
# print(a.rpartition(",")) # returns ('hello,', ',', ' world!')


# Splits the string at the specified separator, and returns a list

# a = "hello@world@welcome@2026"
# print(a.rsplit("@")) # returns ['hello , world', 'welcome', '2026']
# print(a.rsplit("@",2)) # returns ['hello@world', 'welcome', '2026']

# Returns a right trim version of the string

# a = "     hello, world!     "
# print(a.rstrip()) # returns "     hello, world!"

# Splits the string at the specified separator, and returns a list

# a = "hello, world!"
# print(a.split(",")) # returns ['hello', ' world!']

# Splits the string at line breaks and returns a list

# a = "hello\nworld!"
# print(a.splitlines()) # returns ['hello', 'world!']


# Returns true if the string starts with the specified value

# a = "hello, world!"
# print(a.startswith("hello"))

# 	Returns a trimmed version of the string

# a = "     hello, world!     "
# print(a.strip()) # returns "hello, world!"


# Swaps cases, lower case becomes upper case and vice versa

# a = "Hello, World!"
# print(a.swapcase()) # returns "hELLO, wORLD!"


# Converts the first character of each word to upper case

# a = "hello, world!"
# print(a.title()) # returns "Hello, World!"

# Returns a translated string

# a = "hello, world!"
# print(a.translate(a.maketrans("h","H"))) # returns "Hello, world!"

# Converts a string into upper case

# a = "hello, world!"
# print(a.upper()) # returns "HELLO, WORLD!"

# 	Fills the string with a specified number of 0 values at the beginning

# a = "hello, world!"
# print(a.zfill(20)) # returns "0000



# Python Booleans

# print(10 > 9)   # returns True
# print(10 == 9)  # returns False
# print(10 < 9)   # returns False

# Using a If Else Statement

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")


# print(bool(["apple", "banana", "cherry"]))  # returns True
# print(bool([]))  # returns False

# The following values are considered false:
# None
# False
# 0
# 0.0
# ""
# ()
# []
# {}
# set()
# range(0)
# bool(None)



# class MyClass:
#     def __len__(self):
#         return 0

# myobj = MyClass()
# print(bool(myobj))  # returns False


# Functions can Return a Boolean

# def myFunction():
#     return True 

# print(myFunction())  # returns True


# You can execute code based on the Boolean answer of a function

# def myFunction():
#     return True 

# if myFunction():
#     print("YES!")
# else:
#     print("NO!")

# x = True
# print(isinstance(x,int))  # returns True


# The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if (n:= len(numbers)) > 5:
#     print(f"List is too long ({n} elements, expected <= 5)")


# print(x:=10)


# Comparison Operators 

# Chaining Comparison Operators

# Python allows you to chain comparison operators:


# x = 5
# print(1 < x < 10)  # returns True
# print(1 < x and x < 10)  # returns True


# Logical Operators
# Logical operators are used to combine conditional statements:

# x = 5
# print(x > 3 and x < 10)  # returns True
# print(x > 3 or x < 4)
# print(not(x > 3 and x < 10))  # returns False


# Identity Operator 

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# x = ['apple','banana']
# y = ['apple','banana']

# z = x

# print(x is z) 
# print(x is y)
# print(x == y)


# x = ['apple','banana']
# y = ['apple','banana']

# z = x

# print(x is not z)
# print(x is not y)
# print(x != y)


# Membership Operators

# Membership operators are used to test if a sequence is presented in an object:

# fruits = ['apple','banana','cherry']
# print('banana' in fruits)
# print('banana' not in fruits)


# fruits = ['apple','banana','cherry']

# print('pinapple' in fruits)


# Membership in Strings

# The membership operators also work with strings:

# text = "Hello World!"

# print('H' in text)
# print('hello' in text)
# print('z' not in text)



# Bitwise Operators

# And Operator 

# 🟢 AND (&)

# Rule: 1 only if BOTH are 1

# A	B	A & B
# 0	0	0
# 0	1	0
# 1	0	0
# 1	1	1

# Sets each bit to 1 if both bits are 1

# print(6 & 3)  # returns 2


# Or Operator

# 🔵 OR (|)

# Rule: 1 if ANY one is 1

# A	B	A | B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	1


# Sets each bit to 1 if one of two bits is 1

# print(6 | 3)  # returns 7 


# XOR Operator 

# Sets each bit to 1 if only one of two bits is 1

# 🟡 XOR (^)


# Rule: 1 only if DIFFERENT

# A	B	A ^ B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	0

# print(5 ^ 3)  # returns 6


# 🔴 NOT (~)

# Rule: Flip the bit

# A	~A
# 0	1
# 1	0


# Operator Precedence

# Operator precedence describes the order in which operations are performed.

# Pranthises have a higher preicidence so whatever present inside it should be 
# should be executed first 

# print((6 + 3) - (6 + 3))  # returns 0

# Multiplication has a higher precidence then a addition 

# print(100 + 5 * 3) 
# 115 


# Exponential has higher precidence then a substraction 

# print(100 - 3 ** 2)
# 91 

# Bitwise NOT has a higher precedence then a addition 

# print(100 + ~3)  # 96 


#  Operator Precedence ( Priority Wise )

# Highest
#   ()
#   **
#   unary
#   * / // %
#   + -
#   << >>
#   &
#   ^
#   |
#   comparisons
#   not
#   and
#   or
#   =
# Lowest


# Python Lists 

# Lists are used to store multiple items in a single variable.v

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

# thislist = ['apple','banana','cherry']
# print(thislist)



# List Items 

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates

# Since lists are indexed, lists can have items with the same value:

# List

# thislist = ["apple","banana","cherry","apple","cherry"]
# print(thislist)

# To Find a Length of a List 

# thislist = ["apple","banana","cherry","apple","cherry"]

# print(len(thislist))


# List Items - Data Types

# List Items 

# list1 = ["apple","banana","cherry"]
# list2 = [1,5,7,9,3]
# list3 = [True,False,False]

# print(list1)
# print(list2)
# print(list3)


#  The List() Constructor 

# It is also possible to use the list() constructor when creating a new list.

# thislist = list(("apple","banana","cherry"))
# print(thislist)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



# Negative Indexing to Access a Elements in a List 

# myList = ["Apple", "banana","cherry","mango"]

# print(myList[-1])


#  Range of Indexes 

# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# print(thisList[2:5])


# The Search will go from a Index 2 ( Included ) and end at index 5 ( not included )


# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# print(thisList[:4])


# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# print(thisList[2:])



# Negative Indexing accessing a Elements 


# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# print(thisList[-4:-1])

# It will go on searching from a -4 ( Included ) and go till -1 ( Not Included )



# Using a If Condition and a ( in ) Operator 

# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# if "apple" in thisList:
#     print("Yes, 'apple' is in the fruits list")
# else:
#     print("No, 'apple' is not in the fruits list")


# Change Item Value

# To change the value of a specific item, refer to the index number:

# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# thisList[1] = "blackcurrant"

# print(thisList)


#  Change a Range of Item Values 

# To Changes the value of items within a Specified range , define a list with a new values and refer 
# to the range of index numbers where you want to insert the new values 

# thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# thisList[1:3] = ["blackcurrant","watermelon"]

# print(thisList)


# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# thislist = ["apple", "banana", "cherry"]

# thislist[1:2] = ["blackcurrant","watermelon"]

# print(thislist)



# Step 2️⃣ Replace that slice

# You replaced 1 item with 2 items:

# remove:   ["banana"]
# insert:   ["blackcurrant", "watermelon"]

# ['apple', 'blackcurrant', 'watermelon', 'cherry']



#  Insert Items 

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:



# thisList = ["apple","banana","cherry"]

# thisList.insert(2,"watermelon")

# print(thisList)


# Append Items in a List 

# myList = ["apple","banana","cherry"]
# myList.append("orange")
# print(myList)



# Extend List

# To append elements from another list to the current list, use the extend() method.


# thisList = ["apple","banana","cherry"]
# tropical = ["mango","pineapple","papaya"]

# thisList.extend(tropical)

# print(thisList)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# Add Any Iterable

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# thisList = ["apple","banana","cherry"]
# thisTuple = ("kiwi","orange")

# thisList.extend(thisTuple)

# print(thisList)
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']


# Python - Remove List Items

# thisList = ["apple","banana","cherry"]

# thisList.remove("banana")

# print(thisList)



# Remove Specified Index

# The pop() method removes the specified index.

# thisList = ["apple","banana","cherry"]

# thisList.pop(1)

# print(thisList)


# If you do not specify the index, the pop() method removes the last item

# thisList = ["apple","banana","cherry"]

# thisList.pop()

# print(thisList)


# The del keyword also removes the specified index:

# thisList = ["apple","banana","cherry"]

# del thisList[0]

# print(thisList)


# The del keyword can also delete the list completely.


# thisList = ["apple","banana","cherry"]

# del thisList

# print(thisList)


# Traceback (most recent call last):
#   File "d:\CompanyProjects\Devops\Devops\PracticeSet\practice_set.py", line 963, in <module>
#     print(thisList)
#           ^^^^^^^^
# NameError: name 'thisList' is not defined


# Clear the List

# The clear() method empties the list.

# The list still remains, but it has no content.


# thisList = ["apple","banana","cherry"]

# thisList.clear()

# print(thisList)

# []


