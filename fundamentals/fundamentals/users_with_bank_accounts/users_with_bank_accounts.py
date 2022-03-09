class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0.01, 0)

    def deposit(self, amount):	
        self.account += amount
        return self

    def withdrawal(self, amount):
        self.account -= amount
        return self 

    def display_account_info(self):
        print(f"User: {self.name}, Balance: ${self.account}")
        return self 

    def transfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        print(f"{self.name} transferred ${amount} to {user.name}.")
        self.display_account_info()
        user.display_account_info()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate + 1)
            return self

quentin = BankAccount(0.01, 0)
sidney = BankAccount(0.01, 0)

quentin.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()
sidney.deposit(500).deposit(500).withdrawal(200).withdrawal(100).withdrawal(150).withdrawal(50).yield_interest().display_account_info()


quentin = User("Quentin Tarantino")
sergio = User("Sergio Leone")
sidney = User("Sidney Lumet")
