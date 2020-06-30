import time

import pytest


@pytest.fixture()
def db():
    """simulate db connection failure"""
    raise TimeoutError


def test_normal_cases_which_should_all_pass():
    assert 1


def test_connect_db_to_query(db):
    """The result is error since db setup failed"""
    assert 1


def test_normal_case_failed():
    assert 0


@pytest.mark.xfail(reason='DE12345')
def test_case_expected_to_fail():
    assert 0


@pytest.mark.skip(reason='Long run task')
def test_long_run_case_that_we_want_to_skip():
    """simulate long run test case"""
    time.sleep(30)
    assert 0


@pytest.mark.regression
class TestLogin:
    def test_auth_pass(self):
        assert True

    def test_auth_fail(self):
        assert False
