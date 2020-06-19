import pytest


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


@pytest.fixture()
def db():
    print(1 / 0)
    yield


@pytest.mark.slacker(mail='dhong', msg='test result generated!')
def test4(db):
    pass
