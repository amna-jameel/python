# Exercise 1: Positive, negative or zero
# Take a number and print whether it is Positive, Negative or Zero.
# Test: -7 → Negative

num = int(input("Enter a Number"))
if num>0 :
    print(f"{num} is Positive.")
elif num<0 :
    print(f"{num} is Negative.")
else :
    print(f"{num} is Zero.")