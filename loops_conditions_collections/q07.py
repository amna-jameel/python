# Q7. Stock check with tuples

# Each tuple is (name, price, quantity). Unpack each tuple in the loop, then:
# print the items that are out of stock (quantity 0)
# print the total stock value (price × quantity, added up)
# print the items with low stock (1 to 4)
# Expected: out of stock Mouse · low stock Laptop, Monitor · total 600000

products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),
("Keyboard", 5000, 12), ("Monitor", 45000, 2)]
products= list(products)
out=[]
low=[]
total=0

for product, price , quantity in products:
    total+= quantity*price
    if quantity==0:
     out.append(product)
    elif quantity>=1 and quantity<=4:
      low.append(product)


print(f"Out of stock: {out}")
print(f"Low stock: {low}")
print(f"Total stock: {total}")
