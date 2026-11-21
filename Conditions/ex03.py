# Exercise 3: Pass or fail
# Take a student’s marks out of 100. 40 or above is Pass; below 40 is Fail.
# Test: 38 → Fail
marks = int(input("Enter your marks:"))
while marks>100 or marks<0 :
    print("INVALID INPUT ! Please enter marks from 1-100")
    marks = int(input("Enter your marks again:"))

if marks>=40 :
    print("Pass!")
else :
    print("Fail!")