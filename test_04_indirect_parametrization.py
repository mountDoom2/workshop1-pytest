import pytest

from wallet import Wallet, InsufficientAmount

# Exercise 4: Indirect parametrization
#   * Copy tests from exercise 3
#   * In conftest.py, extend 'wallet' fixture, so the initial balance can be parametrized from test using @pytest.mark.parametrize
#   * Update the tests so they use the fixtures with indirect parametrization.
