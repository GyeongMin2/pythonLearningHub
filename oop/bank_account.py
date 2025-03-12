"""간단한 은행 계좌 예제 (상속 포함)"""
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

    def __str__(self):
        return f'{self.owner} 잔액 {self.balance:,}원'

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = int(self.balance * self.rate)
        self.deposit(interest)
        return interest

def transfer(src: BankAccount, dst: BankAccount, amount):
    src.withdraw(amount)
    dst.deposit(amount)

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, fee=100):
        super().__init__(owner, balance)
        self.fee = fee

    def withdraw(self, amount):
        super().withdraw(amount + self.fee)
        return amount

def print_history(accounts):
    for acc in accounts:
        print('-', acc)

if __name__ == '__main__':
    acc = SavingsAccount('김학생', 10000)
    acc.deposit(5000)
    chk = CheckingAccount('김학생', 3000)
    try:
        transfer(acc, chk, 2000)
    except ValueError as err:
        print('이체 실패', err)
    print_history([acc, chk])
    print('이자', acc.add_interest())
