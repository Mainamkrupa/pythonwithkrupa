

import time

# Constants
ATM_PIN = 1429

def main():
    # Print a message to insert the card
    print("Please insert Your CARD")

    # Wait for 5 seconds to simulate card processing
    time.sleep(5)

    # Prompt the user to enter their PIN
    pin = int(input("Enter your ATM PIN: "))

    # Initialize the user's account balance
    balance = 100000

    # Check if the provided PIN is valid
    if pin == ATM_PIN:
        # Display the main menu and process the user's transactions
        while True:
            # Display the main menu
            print("""
                1. Check balance
                2. Withdraw
                3. Deposit
                4. Exit
                """)

            try:
                # Prompt the user to enter their choice
                choice = int(input("Please enter your choice: "))
            except:
                print("Please enter a valid option")
                continue

            # Process the user's choice
            if choice == 1:
                # Display the user's balance
                print(f"Your current balance is {balance}")
            elif choice == 2:
                # Withdraw money from the user's account
                withdraw_amount = int(input("Please enter the amount to withdraw: "))
                if withdraw_amount > balance:
                    print("Insufficient funds")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Your updated balance is {balance}")
            elif choice == 3:
                # Deposit money into the user's account
                deposit_amount = int(input("Please enter the amount to deposit: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account")
                print(f"Your updated balance is {balance}")
            elif choice == 4:
                # Exit the system
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        # Print an error message if the PIN is invalid
        print("Wrong PIN. Please try again.")

if __name__ == "__main__":
    main()

