class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self 

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self 

    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        print(f"{self.name} transferred ${amount} to {user.name}.")
        self.display_user_balance()
        user.display_user_balance()
        return self

quentin = User("Quentin Tarantino", 0)
sergio = User("Sergio Leone", 0)
sidney = User("Sidney Lumet", 0)

quentin.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

sergio.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()

sidney.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()

quentin.transfer_money(50, sidney)