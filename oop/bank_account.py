class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('입금액 오류')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('잔액 부족')
        self.balance -= amount
