import pytest

from wallet import Wallet, InsufficientAmount

# Exercise 1: Read and revise the tests.
# you can add additional tests you see fit.


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash_190():
    wallet = Wallet(100)
    wallet.add_cash(90)
    assert wallet.balance == 190


def test_wallet_add_cash_0():
    wallet = Wallet(100)
    wallet.add_cash(0)
    assert wallet.balance == 100


def test_wallet_spend_cash_10():
    wallet = Wallet(100)
    wallet.spend_cash(10)
    assert wallet.balance == 90


def test_wallet_spend_cash_1():
    wallet = Wallet(100)
    wallet.spend_cash(1)
    assert wallet.balance == 99


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    wallet.spend_cash(100)
