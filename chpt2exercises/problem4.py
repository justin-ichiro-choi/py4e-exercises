"""
Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature
"""

celsius = input("What temperature (in celsius) would you like to convert? ")
fahrenheit = int(celsius) * 9 / 5 + 32
print("The temperature in fahrenheit is " + str(fahrenheit) + "!")
