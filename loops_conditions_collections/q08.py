# Q8. Unique values and the most frequent
# Python Assignment: Loops, Conditions & Collections
# Page 2 of 4
# Use a dictionary to count how many times each number appears. Then print the unique
# numbers and the one that appears most.
# Expected: unique [3, 5, 8, 9] · most frequent 3 (3 times)
nums = [3, 5, 3, 8, 5, 3, 9]

unique = []
frequency = {}

for n in nums:
    if n not in unique:
        unique.append(n)

    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1
most_frequent = max(frequency, key=frequency.get)
print("Unique:", unique)
print("Most frequent:", most_frequent, f"({frequency[most_frequent]} times)")