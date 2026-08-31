class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # This is a private attribute because of the double leading underscore (__) placed at the very beginning of the name __balance.
    # Getter method to access private data safely
    def get_balance(self):
        return self.__balance
    # Setter method to modify private data with validation
    def deposit(self, amount): # amount = how much money to add.
        if amount > 0: # You cannot deposit zero or a negative amount of money.
            self.__balance += amount
            print(f"Successfully deposited ₹{amount}.")
        else:
            print("Error: Deposit amount must be positive!")
    # Method to withdraw money with safety checks
    def withdraw(self, amount): # withdraw: The name of the action.
        if 0 < amount <= self.__balance:  # Validates positive amount and sufficient funds
            self.__balance -= amount
            print(f"Successfully withdrew ₹{amount}.")
        else:
            print("Error: Invalid withdrawal amount or insufficient funds!")
# 1. Create a bank account object
account = BankAccount("Gayathri bhargavi", 30000)
print(f"Account Owner: {account.owner}")
# 2. Check the initial balance using the getter
print(f"Starting Balance: {account.get_balance()}") 
print("-" * 30) # for printing 30 dashes in a row to separate the output for better readability.
# 3. Make a valid deposit
account.deposit(10)
print(f"Balance after deposit: ₹{account.get_balance()}")
print("-" * 30)
# 4. Try an invalid deposit (Should trigger validation error)
account.deposit(0)
print("-" * 30)
# 5. Make a valid withdrawal
account.withdraw(200)
print(f"Final Balance: ₹{account.get_balance()}")
