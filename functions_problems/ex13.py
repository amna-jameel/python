# Exercise 13: Sum of digits (recursion)
# Write sum_digits(n) recursively. Hint: the last digit is n % 10 and the rest is n // 10. Stop
# when n is a single digit.
# Test: sum_digits(1234) → 10 · sum_digits(9875) → 29

def sum_digits(n):
    total_sum = 0  
    
    while n > 0:
        last_digit = n % 10         
        total_sum = total_sum + last_digit  
        n = n // 10                 
        
    
    return total_sum

print(sum_digits(123))  
print(sum_digits(45))   