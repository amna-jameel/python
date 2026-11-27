# Exercise 3: Total price Write total_price(price, quantity=1) that returns price × quantity. Test: total_price(250, 4) → 1000 · total_price(250) → 250

def total_price(price, quantity=1):
    return price*quantity

print(total_price(250,4))
print(total_price(250))