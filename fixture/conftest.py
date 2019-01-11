import pytest


@pytest.fixture(scope="session")
def s():
    pass


@pytest.fixture(scope="module")
def m():
    pass


@pytest.fixture(scope='class')
def c():
    pass


@pytest.fixture
def f():
    pass

