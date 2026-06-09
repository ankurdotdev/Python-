class Account:
    def __init__(self, balance, accNo):
        # Initialize account with balance and account number
        self.balance = balance
        self.accNo = accNo
        
    def debit(self, amt):
        # Deduct amount from balance
        self.balance = self.balance - amt
        print("Rs.", amt, "was debited")
        
        # Show updated balance using a method (abstraction of data access)
        print("Total balance =", self.get_balance())
        
    def credit(self, amt):
        # Add amount to balance
        self.balance = self.balance + amt
        print("Rs.", amt, "was credited")
        
        # Show updated balance using a method
        print("Total balance =", self.get_balance())
        
    def get_balance(self):
        # Method to safely access balance (encapsulation)
        return self.balance   


# Create account object with initial balance and account number
acc1 = Account(21000, 2589746)

# Debit money from account
acc1.debit(5000)

# Credit money to account
acc1.credit(30000)