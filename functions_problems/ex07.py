# Exercise 7: Average of any number of marks (*args)
# Write average(*marks) that returns the average of all marks given. If no marks are given,
# return 0.
# Test: average(80, 90, 70) → 80.0 · average(55, 65) → 60.0 · average() → 0

def average (*numbers):
    total=0
    if len(numbers)==0:
        return 0
    else:
        for n in numbers:
             total= total+n
        aver=total/len(numbers)

    
    return aver

print(average(2,3,4,5))
print(average())