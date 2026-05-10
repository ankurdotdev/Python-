class Account:
    def __init__(self,balance, accNo):
        self.balance = balance
        self.accNo = accNo
        
    def debit(self, amt):
        self.balance = self.balance - amt
        print("Rs.", amt,"was debited")
        print("total balance = ", self.get_balance())
        
    def credit(self, amt):
        self.balance = self.balance + amt
        print("Rs.", amt,"was credit")
        print("total balance = ", self.get_balance())
        
    def get_balance(self):
         return self.balance   


acc1 = Account(21000,2589746)
acc1.debit(5000)
acc1.credit(30000)     