class BankAccount:
    _money = 0

    def deposit(self, money, password):
        if self.authenticate(password):
            self._money += money

    def withdraw(self, money, password):
        if self.authenticate(password):
            self._money -= money

    def getBalance(self, password):
        if self.authenticate(password):
            return self._money
        else:
            return "ACCESS DENIED"

    def authenticate(self, password):
        if password in ["mellon", "qwerty", "1234"]: # This would normally be encrypted on a database
            return True
        else:
            return False
        
myAccount = BankAccount()

myAccount.deposit(1000, "mellon")
myAccount.withdraw(50, "qwerty")
print(myAccount.getBalance("mellon"))

