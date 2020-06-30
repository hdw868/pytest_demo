import pytest


@pytest.fixture()
def db():
    print(1 / 0)
    yield


def test1():
    print(1)
    assert 0


def test2():
    print(2)
    assert 0


@pytest.mark.skip()
def test3():
    print(3)
    pass


def test4(db):
    pass
