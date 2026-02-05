# The match statement is used to perform different actions based on different conditions.

# The Python Match Statement

# Instead of writing many if..else statements, you can use the match statement.

# day = 4

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")



# Default Value

# Use the underscore character _ as the last case value if you want a code block to execute when there are
#  not other matches:


# day = 5

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid Case")


# Combine Values

# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:


# day = 4

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("It is a Weekday")
#     case 6 | 7:
#         print("I love Weekends")


# month = 5
# day = 4 


# match day:
#     case 1 | 2 | 3 | 4 if month == 4:
#         print("Today is Weekday in April")
#     case 1 | 2 | 3 | 4 if month == 5:
#         print("Today is Weekday in May")
#     case _:
#         print("Invalid Case")


