# Code By: ChatGPT

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance
    
    def transfer(self, other_account, amount: float):
        if self is other_account:
            raise ValueError("Cannot transfer to the same account.")
        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance, other_account.balance
    
    def get_balance(self) -> float:
        return self.balance
    
    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance})"
