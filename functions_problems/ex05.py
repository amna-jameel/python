# Exercise 5: Discount with lambda Write a lambda named discount that returns the price after 10% off. Test: discount(2000) → 1800.0

discount = lambda price :price - (price*10)/100

print(discount(2000))