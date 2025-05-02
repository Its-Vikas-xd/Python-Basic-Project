class Account:
    
    # Constructor to initialize account balance and account number
    def __init__(self, bal, acc):
        self.balance = bal  # Store initial balance
        self.account_no = acc  # Store account number

    # Method to withdraw money (debit)
    def debit(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance! Transaction failed.")
        else:
            self.balance -= amount  # Deduct amount from balance
            print("\nRs.", amount, "was debited.")
            print("Total balance =", self.get_balance())

    # Method to deposit money (credit)
    def credit(self, amount):
        self.balance += amount  # Add amount to balance
        print("\nRs.", amount, "was credited.")
        print("Total balance =", self.get_balance())

    # Method to check current balance
    def get_balance(self):  # Returns the current balance
        return self.balance


# Taking user input to create an account
initial_balance = float(input("Enter initial balance: "))  # Get initial balance from user
account_number = input("Enter account number: ")  # Get account number from user

# Creating an account object with user input values
acc1 = Account(initial_balance, account_number)

# Infinite loop to keep the transaction menu running until user exits
while True:
    print("\nChoose a transaction:")
    print("1. Debit")  # Option to withdraw money
    print("2. Credit")  # Option to deposit money
    print("3. Check Balance")  # Option to check account balance
    print("4. Exit")  # Option to exit the program

    choice = input("Enter your choice (1/2/3/4): ")  # Get user choice

    if choice == "1":
        amount = float(input("Enter amount to debit: "))  # Get debit amount from user
        acc1.debit(amount)  # Call debit method
    elif choice == "2":
        amount = float(input("Enter amount to credit: "))  # Get credit amount from user
        acc1.credit(amount)  # Call credit method
    elif choice == "3":
        print("\nYour current balance is:", acc1.get_balance())  # Display current balance
    elif choice == "4":
        print("\nThank you! Have a nice day.")  # Exit message
        break  # Exit loop
    else:
        print("\nInvalid choice! Please enter a valid option.")  # Handle invalid input




