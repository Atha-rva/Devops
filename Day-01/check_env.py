# Get the Environment Information from a User and print it 

# env = int(input("Please enter your environment (dev/staging/prod): "))
# print(f"You have selected the {env} environment.")

# i = 0
# for i in range(2):

#     env = input("Deploy which environment (dev/staging/prod): ")
#     day = input("Deployment day (weekdays/Friday): ")

#     if env == 'dev':
#         print(f"You have selected the {env} environment.")
#         if day == 'Friday':
#             print("You can deploy the Dev environment.")
#         else:
#             print("You can deploy the Dev environment.")
#     elif env == 'staging':
#         print(f"You have selected the {env} environment.")
#         if day == 'Friday':
#             print("You can deploy the Staging environment.")
#         else:
#             print("you can deploy the Staging environment.")
#     elif env == 'prod':
#         print(f"You have selected the {env} environment.")
#         if day == 'Friday':
#             print("You cannot deploy the Prod environment on Fridays.")
#         else:
#             print("You can deploy the Prod environment.")
#     else:
#         print("Invalid environment selected.")


# a = int(input("Enter a Number: "))

# i = 1
# for i in range(11):
#     print(f"{a} * {i} = {a*i}")




# def check_sum(num1 , num2):
#     num3 = num1 + num2;
#     print(f"The sum of {num1} and {num2} is: {num3}")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# check_sum(num1 , num2)


# apko kaam karna hai ki user se CPU threshold lo
# current cpu usage pata karo
# agar cpu usage threshold se zyada hua, email kar do

# cpu_threshold = int(input("Enter CPU threshold percentage: "))
# current_cpu_usage = int(input("Enter current CPU usage percentage: "))

# if current_cpu_usage > cpu_threshold:
#     print("CPU usage is above the threshold! Sending email alert...")
# else:
#     print("CPU usage is within the threshold.")


# def send_email_alert():
#     cpu_threshold = int(input("Enter CPU threshold percentage: "))
#     current_cpu_usage = int(input("Enter current CPU usage percentage: "))
#     if current_cpu_usage > cpu_threshold:
#         print("CPU usage is above the threshold! Sending email alert...")
#     else:
#         print("CPU usage is within the threshold.")
        
# send_email_alert()

import psutil

def check_cpu_usage(threshold):
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > threshold:
        print(f"CPU usage is {cpu_usage}%. Sending email alert...")
    else:
        print(f"CPU usage is {cpu_usage}%. CPU usage is within the threshold.")
cpu_threshold = int(input("Enter CPU threshold percentage: "))
check_cpu_usage(cpu_threshold)