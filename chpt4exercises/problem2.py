
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay 
# which takes two parameters (hours and rate).

def timePaid(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print("This is wrong")
        exit()
    rate = hours * rate

    if(hours > 40):
        rate = 1.5 * rate

    return rate

query = input("Enter hours worked: ")
query2 = input("Enter pay grade: ")

final = str(round(timePaid(query, query2),2))
print("Your total = $" + final)