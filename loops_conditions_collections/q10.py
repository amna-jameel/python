# Q10. Shopping cart menu
# Use while True to show a menu: 1. Add item, 2. View cart, 3. Checkout.
# Add item: ask for the name and price, and store them in a dictionary
# View cart: print every item and the total
# Checkout: print the total; if it is over Rs 5000, give 10% off. Then break

cart = {}

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. View cart")
    print("3. Checkout")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        product = input("Enter product name: ")
        price = int(input("Enter product price: "))

        cart[product] = price
        print("Item added successfully!")

    elif choice == 2:
        print("\nYour Shopping Cart:")

        total = 0
        for key, value in cart.items():
            print(key, ":", value)
            total += value

        print("Total:", total)

    elif choice == 3:
        total = 0

        for key, value in cart.items():
            total += value

        print("\nCheckout")
        print("Original Total:", total)

        if total > 5000:
            discount = total * 0.10
            print("10% Discount:", discount)
            total = total - discount
        else:
            print("No Discount Applied")

        print("Final Bill:", total)
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Please select 1, 2 or 3.")
