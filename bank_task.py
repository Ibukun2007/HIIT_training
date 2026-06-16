"""



#Simple Banking System
#----------------------
#A basic console program that lets a user check their balance,
#recharge (deposit) money, and transfer money out of their account.


# Default starting balance
balance = 1000.0


def show_balance():
    print(f"\nYour current balance is: {balance:.2f}")


def recharge():
    global balance
    try:
        amount = float(input("Enter amount to recharge: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        balance += amount
        print(f"Recharge successful! New balance: {balance:.2f}")
    except ValueError:
        print("Invalid amount entered. Please enter a number.")


def transfer():
    global balance
    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > balance:
            print("Insufficient balance for this transfer.")
            return
        recipient = input("Enter recipient's name/account number: ")
        balance -= amount
        print(f"Transfer of {amount:.2f} to {recipient} successful!")
        print(f"New balance: {balance:.2f}")
    except ValueError:
        print("Invalid amount entered. Please enter a number.")


def main():
    print("=" * 40)
    print("      WELCOME TO PYTHON BANK")
    print("=" * 40)

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Recharge")
        print("3. Transfer")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            show_balance()
        elif choice == "2":
            recharge()
        elif choice == "3":
            transfer()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

        # Ask if the user wants to perform another transaction
        again = input("\nDo you want to perform another transaction? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using Python Bank. Goodbye!")
            break


if __name__ == "__main__":
    main()


"""


balance = 50000

while True:
    print("\nBANK MENU")
    print("1. Check Balance")
    print("2. Recharge Airtime")
    print("3. Transfer Money")

    option = int(input("Select an option: "))

    if option == 1:
        print(f"Your balance is: ₦{balance}")

    elif option == 2:
        recharge_amount = float(input("Enter recharge amount: ₦"))

        if recharge_amount <= balance:
            balance -= recharge_amount
            print("Recharge successful!")
            print(f"Remaining balance: ₦{balance}")
        else:
            print("Insufficient balance!")

    elif option == 3:
        transfer_amount = float(input("Enter transfer amount: ₦"))

        if transfer_amount <= balance:
            balance -= transfer_amount
            print("Transfer successful!")
            print(f"Remaining balance: ₦{balance}")
        else:
            print("Insufficient balance!")

    else:
        print("Invalid option!")

    choice = input("\nDo you want to perform another transaction? (Y/N): ")

    if choice.lower() != "y":
        print("Thank you for banking with us!")
    break