# Q4. Even multiples of 7
# Use a loop to go through the table of 7 (7 to 70) and print only the even results.
# Expected: 14 28 42 56 70

for i in range(1,11):
    table = i*7
    if table%2==0 :
        print(table)
    