# Exercise 6: Smallest and largest(return two values)
# Write min_max(numbers) that returns the smallest and largest number as two values. Use
# a loop, not min() or max().
# Test: low, high = min_max([45, 12, 89, 33]) → low = 12, high = 89
def min_max(li):
  
    low = li[0]
    high = li[0]
    
    for l in li:
        if l > high:
            high = l
        if l < low:
            low = l

    return low, high

low, high = min_max([45, 12, 89, 33])
print(f"low = {low}, high = {high}") 

print(min_max([24,3,4,5,666,0,-3]))