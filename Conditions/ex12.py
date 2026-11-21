# Exercise 12: Ride fare calculator
# Fare = Rs 100 base + Rs 40 per km. At night (hour 22 or later, or before 6), add 20%. Take
# the km and the hour (0–23) and print the final fare.
# Test: 10 km at hour 23 → Fare: Rs 600.0
km = int(input("Enter distance in km: "))
while km<=0:
    print("invalid! please Enter valid distance")
    km = int(input("Enter distance in km: "))
hours= int(input("Choose timing from 0-23: "))
while hours>23 or hours<0 :
    print("invalid! please choose timing from 0-23")
    hours= int(input("Choose timing from 0-23: "))
total_fare = (100 + (40*km))
if hours>=22 or hours<6 :
    fare= (total_fare*20)/100
    fare = fare+total_fare
    print(f"fare is {fare}! 20% extra charges are implemented bcz of night. ")
else:
    print(f"fare for {km} and {hours} is {total_fare}")