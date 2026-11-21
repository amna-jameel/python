# Exercise 2: Voting eligibility
# Take a person’s age. At 18 or above, print “Eligible to vote”. Otherwise, print how many
# years are left.
# Test: 15 → Not eligible, wait 3 more years

age= int(input("Enter your age: "))
remaining = 0
if age>=18 :
    print("Eligible to vote")
else:
     remaining=18-age
     print(f"Not eligible , {remaining} years are left")