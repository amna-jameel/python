# Q1. Pass or fail list
# Loop through the list and print each mark with Pass (40 or above) or Fail. At the end, print
# how many students passed.
# Expected: 78 Pass … 33 Fail … and Passed: 5
marks = [78, 45, 92, 33, 67, 88]
count=0
for num in marks:
    if num>=40:
        print(f"{num} Pass")
        count=count+1
    else:
        print(f"{num} Fail")

print(f"Total Passed: {count}")