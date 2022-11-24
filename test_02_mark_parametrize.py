import pytest

from wallet import Wallet, InsufficientAmount

# Exercise2: Use @pytest.mark.parametrize to parametrize the tests with the same implementation.


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash1():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_wallet_add_cash2():
    wallet = Wallet(10)
    wallet.add_cash(0)
    assert wallet.balance == 10


def test_wallet_spend_cash1():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash2():
    wallet = Wallet(100)
    wallet.spend_cash(1)
    assert wallet.balance == 99


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    wallet.spend_cash(100)
