class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "is debited")
        print("Total Balance is", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credited")
        print("Total Balance is", self.get_balance())
        
    def get_balance(self):
        return self.balance
        
acc1 = Account(50000, 129876)
acc1.debit(1000)
acc1.credit(2500)