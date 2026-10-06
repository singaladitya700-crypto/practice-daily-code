class Bankaccount:
    def __init__(self ,owner , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount
        return self.balance

    def withdraw(self ,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return("not enough balance")

    def check_balance(self):
        return "current balance is" , self.balance


c1 = Bankaccount("Aditya" , 10000)
print(c1.deposit(3000))
print(c1.withdraw(23000))
print(c1.check_balance())