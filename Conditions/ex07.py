# Exercise 7: Shop discount
# Take the bill amount and print the discount and the final amount.
# Test: 3000 → Discount: 150.0, Pay: 2850.0

amount = int(input("Enter your bill amount: "))
discount=0
pay=0
if amount>=5000 :
    discount = (amount*10)/100
    pay=amount-discount
    print(f"Discount: {discount}\n Pay: {pay}")
elif amount>=2000 and amount<=4999:
    discount = (amount*5)/100
    pay=amount-discount
    print(f"Discount: {discount}\n Pay: {pay}")
else :
    print(f"No discount available! Pay: {amount}")