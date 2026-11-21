# Exercise 5: Weather advice
# Take the temperature in °C and print the advice.
# Test: 38 → Very hot, stay hydrated

temp = int(input("Enter your temperature: "))
if temp<10 :
    print("Cold, wear a jacket")
elif temp>=10 and temp<=25:
    print("Pleasant")
elif temp>=26 and temp<=35 :
    print("Warm")
else :
    print("Very hot, stay hydrated")