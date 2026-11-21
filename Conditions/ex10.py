# Exercise 10: Mobile package
# Take the balance and the package price. If the balance is enough, print “Package
# activated” and the remaining balance. Otherwise, print how much more is needed.
# Test: balance 300, price 450 → Insufficient balance, need Rs 150 more

balance = int(input("Enter your balance: "))
price = int(input("Enter package price: "))
remaining=0
if balance>=price :
    remaining = balance-price
    print(f"Package activated! and the remaining balance is {remaining}")
else :
    remaining = price-balance
    print(f"{remaining} is needed to activate packg")
