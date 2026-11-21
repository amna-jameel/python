# Exercise 4: Divisible by 5 and 11
# Check whether a number is divisible by both 5 and 11. Use % and and.
# Test: 55 → Yes · 25 → No
num = int(input("Enter a number: "))
if num%5==0 and num%11==0 :
    print(f"Yes, {num} is divisible by both 5 and 11.")
else :
    print(f"Not, {num} is not divisible by both 5 and 11.")