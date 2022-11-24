import pytest

from .wallet import Wallet, InsufficientAmount


def pytest_addoption(parser):
    # parser.addoption(
    ...


def pytest_configure(config):
    ...


def pytest_generate_tests(metafunc):
    ...


def pytest_collection_modifyitems(items):
    ...


@pytest.fixture
def wallet():
    ...
