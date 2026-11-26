# Q11. Simple ATM
# Start with balance = 10000 and an empty list history = []. Use while True with the options
# Deposit, Withdraw, Check balance and Exit.
# Don’t allow a withdrawal bigger than the balance; print “Insufficient balance”
# Save every deposit and withdrawal in history
# On Exit, print the whole history, then break

balance = 10000
history = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit = int(input("Enter the amount to deposit: "))

        balance = balance + deposit
        history.append(f"Deposited Rs. {deposit}")

        print(f"Updated balance is {balance}")

    elif choice == 2:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance = balance - withdraw
            history.append(f"Withdrawal Rs. {withdraw}")
            print(f"Updated balance is {balance}")

    elif choice == 3:
        print(f"Your current balance is Rs. {balance}")

    elif choice == 4:
        print("\nTransaction History")

        for his in history:
            print(his)

        break

    else:
        print("Invalid choice! Please try again.")
