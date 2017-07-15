""" Exercise 3:Write a program to prompt for a score between 0.0 and 1.0
If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:

Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F
~~~
"""

query = input("Enter a score between 0.0 and 1.0 ")

# Seeing if input is a floating point number
try:
    score = float(query)
except:
    # Not sure how to reduce reduncancy if number is > than 1.0
    print("Bad score")
    exit()

grade = "F"

# Grading scale implemented to determine grade
if score > 1.0:
    print("Bad score")
    exit()
elif score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"

# Prints grade for user
print(grade)
