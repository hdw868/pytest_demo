import pytest


@pytest.mark.acceptance
@pytest.mark.regression
def test_send_http():
    pass  # perform some webtest test for your app


@pytest.mark.acceptance
def test_check_http():
    pass  # perform some webtest test for your app


@pytest.mark.regression
def test_something_quick():
    pass


def test_another():
    pass


def test_fail():
    assert 1 == 2


@pytest.mark.regression
class TestClass(object):
    def test_method(self):
        pass

    @pytest.mark.slow
    def test_method_slow(self):
        pass
