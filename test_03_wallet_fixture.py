import pytest

from wallet import Wallet, InsufficientAmount

# Exercise 3: Fixtures
#   * Copy tests from exercise 2
#   * In conftest.py implement two fixtures:
#     * empty_wallet - return Wallet with 0 balance
#     * wallet - return Wallet with balance set to 100
#   * Update the tests so they use the fixtures.
