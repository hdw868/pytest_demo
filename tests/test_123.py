import pytest


def test_1():
    assert 1


@pytest.mark.xfail()
def test_2():
    assert 0


@pytest.mark.xfail()
def test_3():
    assert 3


@pytest.mark.skip()
def test_4():
    assert 4
