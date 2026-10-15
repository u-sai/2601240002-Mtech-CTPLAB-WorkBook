def deposit(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero")

    return balance + amount


def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


def test_deposit() -> None:
    assert deposit(1000.0, 500.0) == 1500.0


def test_withdraw() -> None:
    assert withdraw(1000.0, 300.0) == 700.0


def test_invalid_deposit() -> None:
    try:
        deposit(1000.0, -100.0)
        assert False
    except ValueError:
        assert True


def test_invalid_withdraw() -> None:
    try:
        withdraw(500.0, 700.0)
        assert False
    except ValueError:
        assert True


def main() -> None:
    balance = 1000.0

    print("Initial Balance:", balance)

    balance = deposit(balance, 500.0)
    print("After Deposit:", balance)

    balance = withdraw(balance, 300.0)
    print("After Withdrawal:", balance)

    test_deposit()
    test_withdraw()
    test_invalid_deposit()
    test_invalid_withdraw()

    print("All tests passed")


if __name__ == "__main__":
    main()