import pytest


@pytest.fixture
def f1():
    pass


def test_foo(f1, f, s, m):
    pass


def test_foo2(f1, f, s, m):
    pass


class TestClass(object):
    def test_method1(self, f1, m, c, s):
        pass

    def test_method2(self, f1, m, c, s):
        pass
