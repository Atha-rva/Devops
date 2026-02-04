# Else Statements

# The else keyword catches anything which isn't caught by the preceding conditions.

# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a is greater than b



# Else Without Elif

# You can also have an else without the elif:

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
# b is not greater than a

# Note: The else statement must come last. You cannot have an elif after an else.

# number = 7

# if number % 2 == 0:
#   print("The number is even")
# else:
#   print("The number is odd")


# Else as Fallback

# The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.

# username = "Atharva"

# if len(username) > 3 :
#     print(f"Welcome to Streets {username}")
# else:
#     print("Invalid Username")
# Welcome to Streets Atharva


