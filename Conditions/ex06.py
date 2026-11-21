# Exercise 6: Day name
# Take a number from 1 to 7 and print the day (1 = Monday … 7 = Sunday). Any other number
# prints “Invalid day”.
# Test: 5 → Friday

day = int(input("Enter a number from 1-7 :"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day")