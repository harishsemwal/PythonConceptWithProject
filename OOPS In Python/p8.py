class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def get_balance(self):
        return self.balance
        
    # debit method
    def debit(self, ammount):
        self.balance -= ammount
        print("Rs.", ammount, "was debited")
        print("Total Balance: ", self.get_balance())
    
    def cradit(self, ammount):
        self.balance += ammount
        print("Rs.", ammount, "was cradited")
        print("Total Balance: ", self.get_balance())
        
        
acc = Account(10000, 12345)
print(acc.balance)
print(acc.account_no)

acc.cradit(500)
