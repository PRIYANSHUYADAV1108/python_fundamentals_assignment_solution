class BankAccount:
    def __init__(self,account_number,owner_name,balance):
       self.account_number = account_number
       self.owner_name = owner_name
       self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"The Amount is Successfully deposite{amount}")
    def withdraw(self,amount):
        if amount <= self.balance:
           self.balance -= amount
           print(f"the withdram amount is{amount}")
        else:
           print("insuffient balance")

    def check_balance(self):
        print(f"balance is {self.balance}")
acc1 = BankAccount(123456789,"priyanshu kumar", 10000)

acc1.deposite(20000)
acc1.withdraw(1500)
acc1.check_balance()
       
