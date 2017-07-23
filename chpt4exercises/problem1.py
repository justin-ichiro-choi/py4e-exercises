"""
Exercise 7: Rewrite the grade program from the previous
chapter using a function called computegrade that takes
a score as its parameter and returns a grade as a string
"""
score = input("What sort of grade would you like?")
def computegrade(score):
    try:
        score = float(score)
    except:
        print("Bad score")
        exit()
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
    return(grade)

print(computegrade(score))