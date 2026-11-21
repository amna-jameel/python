# Exercise 9: Triangle checker
# Take three sides. If any two sides add up to no more than the third, print “Not a valid
# triangle”. Otherwise print its type: Equilateral (all equal), Isosceles (two equal) or Scalene
# (none equal).
# Test: 3, 4, 5 → Scalene · 5, 5, 8 → Isosceles · 1, 2, 10 → Not a valid triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
while a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
if a==b and b==c :
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else :
    print("Scalene")

