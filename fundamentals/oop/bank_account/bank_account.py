class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        

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
        
    @classmethod
    def display_all_instances(cls):
        for account in cls.accounts:
            account.display_account_info()

accountX = BankAccount(0.01, 0)
accountY = BankAccount(0.01, 0)

accountX.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()
accountY.deposit(500).deposit(500).withdrawal(200).withdrawal(100).withdrawal(150).withdrawal(50).yield_interest().display_account_info()

BankAccount.display_all_instances()