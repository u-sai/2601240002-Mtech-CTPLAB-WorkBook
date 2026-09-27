from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BankAccount(ABC):
    account_number: int
    holder_name: str
    balance: float = 0.0

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self) -> None:
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


@dataclass
class SavingsAccount(BankAccount):
    interest_rate: float = 4.0

    def calculate_interest(self) -> float:
        return self.balance * self.interest_rate / 100


@dataclass
class CurrentAccount(BankAccount):
    interest_rate: float = 2.0

    def calculate_interest(self) -> float:
        return self.balance * self.interest_rate / 100


savings = SavingsAccount(101, "Raasi", 10000)

savings.deposit(2000)
savings.withdraw(1000)

print("Savings Account")
savings.display()
print("Interest:", savings.calculate_interest())


current = CurrentAccount(102, "Priya", 15000)

print("\nCurrent Account")
current.display()
print("Interest:", current.calculate_interest())