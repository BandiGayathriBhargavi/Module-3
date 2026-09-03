import random # This line is required for the usage in line - 7 
from datetime import datetime
class BankAccount:
    def __init__(self, owner_name, initial_deposit):
        self.account_number = str(random.randint(100000, 999999)) # The Line - 1 module random is used here
        self.owner_name = owner_name
        self.balance = float(initial_deposit)
        self.transaction_history = [] # Python List dedicated to storing the chronological ledger of financial movements for that specific account.
        # Log the initial account opening transaction
        self._add_transaction("Account Created", initial_deposit)
    def _add_transaction(self, type_of_action, amount): # The single underscore is a standard Python naming convention indicating that a method is private 
                                                        # and intended for internal use only
        """To log transactions with timestamps."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # The strftime = string format time.
        self.transaction_history.append({ # self.transaction_history is the empty storage list initialized when the account was first created.
            "timestamp": timestamp, # Gets the input form Line - 14
            "type": type_of_action, # type_of_action: Records whether this specific event was a "Deposit", "Withdrawal", or "Account Created".
            "amount": float(amount), # float(amount): Stores the exact money value involved, converting it to a floating-point decimal to ensure math consistency.
            "resulting_balance": self.balance # self.balance: what the account balance became immediately after this specific action was completed.
        })
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.") # If we try to deposit a negative amount or zero, the system will reject it and inform the user.
            return False
        self.balance += amount # Here, the account's balance is increased by the deposited amount, reflecting the new total funds available.
        self._add_transaction("Deposit", amount)
        print(f"Successful deposit of ₹{amount:,.2f}. New Balance: ₹{self.balance:,.2f}")
        return True
    def withdraw(self, amount):
        # Why can't we use elif here?
        # You cannot use elif here because these two checks are completely unrelated, independent tests that evaluate two different problems.
        if amount <= 0:
            print("Withdrawal amount must be positive.") # If we try to withdraw a negative amount or zero, the system will reject it and inform the user.
            return False
        if amount > self.balance:
            print(f"Insufficient funds. Available balance is ₹{self.balance:,.2f}")
            return False
        self.balance -= amount # Here, the account's balance is decreased by the withdrawn amount, reflecting the updated total funds available after the transaction.
        self._add_transaction("Withdrawal", amount)
        print(f"Successful withdrawal of ₹{amount:,.2f}. New Balance: ₹{self.balance:,.2f}")
        return True
    def display_statement(self):
        """Prints a ledger."""
        print(f"\n--- TRANSACTION HISTORY FOR ACC #{self.account_number} ---")
        print(f"Holder: {self.owner_name} | Current Balance: ₹{self.balance:,.2f}\n")
        print(f"{'Timestamp':<20} | {'Type':<15} | {'Amount':<12} | {'Balance Available':<15}")
        print("-" * 70)
        for tx in self.transaction_history:
            print(f"{tx['timestamp']:<20} | {tx['type']:<15} | ₹{tx['amount']:<11,.2f} | ₹{tx['resulting_balance']:<14,.2f}")
        print("-" * 70)
class BankSystem:
    """Manages system-level operations and user interface routing."""
    def __init__(self):
        self.accounts = {}
    def create_account(self):
        """Collects metrics to spin up a new BankAccount entity."""
        print("\n--- Create a New Account ---")
        name = input("Enter account holder's full name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        try:
            initial_deposit = float(input("Enter initial deposit amount: ₹"))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative.")
                return
        except ValueError:
            print("Invalid amount typed. Numbers only.")
            return
        new_acc = BankAccount(name, initial_deposit)
        self.accounts[new_acc.account_number] = new_acc
        print(f"\nSuccess! Account generated for {name}.")
        print(f"YOUR ASSIGNED ACCOUNT NUMBER IS: {new_acc.account_number}")
    def get_account(self):
        """Helper to safely fetch an account from state dictionary."""
        acc_num = input("Enter your 12-digit account number: ").strip()
        account = self.accounts.get(acc_num)
        if not account:
            print("Account number not recognized.")
            return None
        return account
    def run(self):
        while True:
            print("\n==============================")
            print("     CANARA DIGITAL BANKING     ")
            print("==============================")
            print("1. Create New Bank Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transaction History")
            print("5. Exit System")
            choice = input("\nSelect an option (1-5): ").strip()
            if choice == "1":
                self.create_account()
            elif choice == "2":
                account = self.get_account()
                if account:
                    try:
                        amt = float(input("Enter deposit amount: ₹"))
                        account.deposit(amt)
                    except ValueError:
                        print("Invalid amount.")
            elif choice == "3":
                account = self.get_account()
                if account:
                    try:
                        amt = float(input("Enter withdrawal amount: ₹"))
                        account.withdraw(amt)
                    except ValueError:
                        print("Invalid amount.")
            elif choice == "4":
                account = self.get_account()
                if account:
                    account.display_statement()
            elif choice == "5":
                print("\nThank you for banking with us!")
                break
            else:
                print("Invalid entry. Pick a number from 1 to 5.")
if __name__ == "__main__":
    bank = BankSystem()
    bank.run()
