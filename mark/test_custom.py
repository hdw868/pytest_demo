"""Try:
test discovery:
pytest -m "webtest" -v
pytest -m "not webtest" -v
pytest --lf -v
pytest --ff -v
pytest test_custom.py::TestClass::test_method -v
pytest -k "http" -v
"""

import pytest


@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


def test_something_quick():
    pass


def test_another():
    pass


def test_fail():
    assert 1 == 2


class TestClass(object):
    def test_method(self):
        pass
