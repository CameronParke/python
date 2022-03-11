class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = 0

    def deposit(self, amount):	
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self 

    def display_account_info(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self 

    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount
        print(f"{self.name} transferred ${amount} to {user.name}.")
        self.display_account_info()
        user.display_account_info()
        return self

quentin = User("Quentin Tarantino", 0)
sergio = User("Sergio Leone", 0)
sidney = User("Sidney Lumet", 0)

quentin.deposit(100).deposit(100).deposit(100).withdrawal(50).display_account_info()

sergio.deposit(100).deposit(100).withdrawal(50).withdrawal(50).display_account_info()

sidney.deposit(100).withdrawal(25).withdrawal(25).withdrawal(25).display_account_info()

quentin.transfer_money(50, sidney)