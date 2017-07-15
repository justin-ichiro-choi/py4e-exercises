# Exercise 1: Write a program to prompt the user for hours and
# rate per hour to compute gross pay.

# ADDITION: Rewrite you pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

# 2ND ADDITION: Add try/except conditions to gracefully handle invalid input

try:
    hours = input("Enter Hours: ")
    rate = input("Enter Rate:")
    pay = float(hours) * float(rate)
except:
    print("Invalid input detected: Please enter a number")
    # Exits the program after
    exit()

pay = hours * rate

# Conditional placed for hours worked above 40 hours
if hours > 40.0:
    pay = 1.5 * hours * rate

print("Pay: " + str(round(pay,2)))
