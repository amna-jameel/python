# Exercise 1: Temperature converter Write celsius_to_fahrenheit(c) that returns the temperature in °F. Formula: F = C × 9/5 + 32. Test: celsius_to_fahrenheit(37) → 98.6 · celsius_to_fahrenheit(100) → 212.0

def celsius_to_fahrenheit(C):
    F = C * 9/5 + 32
    return F
    

temp = celsius_to_fahrenheit(37)
print(f"Temperature from celsius to fahrenheit is {temp}")
