import copy

import pytest


def test_assert_in():
    a = 1
    b = [2, 3, 4]
    assert a in b


def test_eq_list():
    long_list = [0, 1, 2] * 100
    a = long_list + [0, 1, 2]
    b = long_list + [0, 2, 1]
    assert a == b


def test_eq_long_text():
    a = "1" * 100 + "a" + "2" * 100
    b = "1" * 100 + "b" + "2" * 100
    assert a == b


def test_assert_with_additional_info():
    class SomeThing(object):
        def __init__(self, c):
            self.c = c * 2

        def __repr__(self):
            return "<SomeThing object c: {}>".format(self.c)

    a = SomeThing(1)

    assert a.c == 3, a


# pytest function approx to test float
def test_assert_with_approx():
    from pytest import approx
    assert 0.123456789 == approx(0.123456788)


# using with pytest.raises to test exceptions
def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        1 / 0
