import sys

import pytest


def test_hello():
    assert 0


@pytest.mark.xfail
def test_hello2():
    assert 0


@pytest.mark.xfail(reason="DE12345, xxx")
def test_hello3():
    assert 0


@pytest.mark.xfail(sys.version_info < (3, 6),
                   reason="api change after 3.6")
def test_function():
    assert 0


