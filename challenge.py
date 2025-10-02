#create a python program that simulates a very basic atm. the user starts with a balance of 1000 pesos
#the program should allow deposits, withdrawals, balance checks, and exiting the system.

#variables - stores user balance
#input & print - display menu and get users choice
#if - check which option is selected
#while - keep showing the menu until the user chooses "exit"


balance = 1000  # Starting balance in pesos
event = True  # Controls the main loop

while event:
    print("ATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ₱{balance}")

    elif choice == "2":
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            balance += int(amount)
            print(f"Deposited ₱{amount}. New balance is ₱{balance}")
        else:
            print("Invalid input. Please enter a numeric value.")

    elif choice == "3":
        amount = input("Enter amount to withdraw: ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= balance:
                balance -= amount
                print(f"Withdrew ₱{amount}. New balance is ₱{balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid input. Please enter a numeric value.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        event = False

    else:
        print("Invalid choice. Please select from 1 to 4.")
