import pytest


def test_eq_list():
    long_list = [0, 1, 2] * 100
    a = long_list + [3, 4, 5]
    b = long_list + [4, 4, 5]
    assert a == b


def test_eq_long_text():
    a = "1" * 100 + "a" + "2" * 100
    b = "1" * 100 + "b" + "2" * 100
    assert a == b


class Response(object):
    def __init__(self, code, body):
        self.code = code
        self.body = body


def test_assert_with_additional_info():
    resp = Response(403, '{"msg": "Forbidden"}')
    # no msg is printed if the assertion passed
    assert resp.code == 403, 'body: ' + resp.body
    # msg is printed if the assertion failed
    assert resp.code == 200, 'body: ' + resp.body


# pytest function approx to test float
def test_assert_with_approx():
    from pytest import approx
    assert 0.123456789 == approx(0.123456788)


# using with pytest.raises to test exceptions
def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        1 / 0
