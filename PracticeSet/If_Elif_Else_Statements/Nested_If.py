# Nested If Statements

# You can have if statements inside if statements. This is called nested if statements.

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
# Above ten, and also above 20!


# age = 25
# has_license = True

# if age >= 18:
#   if has_license:
#     print("You can drive")
#   else:
#     print("You need a license")
# else:
#   print("You are too young to drive")


# score = 85
# attendance = 90
# submitted = True

# if score >= 60:
#   if attendance >= 80:
#     if submitted:
#       print("Pass with good standing")
#     else:
#       print("Pass but missing assignment")
#   else:
#     print("Pass but low attendance")
# else:
#   print("Fail")
# Pass with good standing



# Nested If vs Logical Operators 

# temperature = 25
# is_sunny = True

# if temperature > 20:
#   if is_sunny:
#     print("Perfect beach weather!")


# temperature = 25
# is_sunny = True

# if temperature > 20 and is_sunny:
#   print("Perfect beach weather!")



# username = "Atharva"
# password = "Atharva@1234"
# is_active = True 

# if username:
#     if password:
#         if is_active:
#             print(f"Welcome to Streets {username}")
#         else:
#             print("Your account is not active")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid Username")
# # Welcome to Streets Atharva