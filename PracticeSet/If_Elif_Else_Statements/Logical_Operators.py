# Python Logical Operators

# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# a = 5
# b = 10
# c = 15

# if a < b and b < c:
#     print("All conditions are true")
# else:
#     print("At least one condition is false")
# # All conditions are true


# OR Statment 

# a = 33
# b = 200

# if b > a or a > b:
#   print("At least one of the conditions is True")
# At least one of the conditions is True

# a = 33 
# b = 200

# if not a > b:
#     print("a is not greater than b")
# a is not greater than b


# Combining Multiple Operators

# You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.

# age = 25 
# is_student = True 
# has_discounted_code = True 

# if (age < 18 or age > 65 ) and not is_student or has_discounted_code:
#     print("You are eligible for a discount")
    # You are eligible for a discount