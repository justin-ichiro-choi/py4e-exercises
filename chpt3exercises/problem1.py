# Exercise 1: Write a program to prompt the user for hours and
# rate per hour to compute gross pay.
# ADDITION: Rewrite you pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = hours * rate

# Conditional placed for hours worked above 40 hours
if hours > 40.0:
    pay = 1.5 * hours * rate

print("Pay: " + str(round(pay,2)))
