# Short Hand If

# If you have only one statement to execute, you can put it on the same line as the if statement.


# a = 5
# b = 10

# if a < b: print("a is less than b")

# a is less than b

# Note: You still need the colon : after the condition.


# a = 2
# b = 330
# print("A") if a > b else print("B")


# Assign a Value With If ... Else

# You can also use a one-line if/else to choose a value and assign it to a variable:

# a = 10
# b = 20

# bigger = a if a > b else b

# print(bigger)
# # 20

# Syntax :- 
# variable = value_if_true if condition else value_if_false


# Multiple Conditions on One Line

# You can chain conditional expressions, but keep it short so it stays readable:

# a = 330
# b = 300

# print("A") if a > b else print("=") if a == b else print("B")


# username = ""

# display_name = username if username else "Guest"

# print(display_name)
# # Guest


# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions. For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.

