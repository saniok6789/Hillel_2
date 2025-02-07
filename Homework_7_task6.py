import pytest

class BankAccount:
    """Банковский счет."""

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Недостаточно средств!")
        self.balance -= amount

    def get_balance(self):
        return self.balance

@pytest.fixture
def bank_account():
    account = BankAccount()
    account.deposit(100)
    return account

@pytest.mark.parametrize("deposit_amount,expected", [(50, 150), (25, 125)])
def test_deposit(bank_account, deposit_amount, expected):
    bank_account.deposit(deposit_amount)
    assert bank_account.get_balance() == expected

@pytest.mark.skip(reason="Пропуск теста снятия, если счет пуст")
def test_withdraw_empty_account():
    empty_account = BankAccount()
    with pytest.raises(ValueError):
        empty_account.withdraw(10)
