import time

import pytest


def test_1():
    assert 1


# @pytest.mark.repeat(3)
def test_2():
    assert 1


def test_3():
    assert 1


def test_4():
    assert 0


def test_5():
    time.sleep(30)
    assert 1
