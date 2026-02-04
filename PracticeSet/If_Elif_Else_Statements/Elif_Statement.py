# Elif Statements

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# Multiple Elif Statements

# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

# score = 75 

# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# elif score >= 60:
#     print("Grade D")
# else:
#     print("Grade F")
# Grade B


# How Elif Works

# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.


# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

# age = 25

# if age >= 18:
#     print("You are an adult")
#     print("You can vote")
# elif age >= 13:
#     print("You are a teenager")
#     print("You can play a game")
# else:
#     print("You are a child")
#     print("You cannot do anything")
# You are an adult
# You can vote



# When to Use Elif

# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")
# Wednesday