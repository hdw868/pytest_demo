import sys

import pytest

a = 2
# module-level mark
pytestmark = pytest.mark.skipif(a == 1, reason='may be test data is corrupted!')


def test_normal_case():
    """no skip mark function"""
    pass


@pytest.mark.skip(reason="not implemented yet")
def test_in_the_future():
    raise NotImplemented


# class-level mark
@pytest.mark.skipif(sys.platform == 'win32',
                    reason="not  applicable on windows x86")
class TestPosixCalls(object):

    def test_only_available_in_linux(self):
        """will not be setup or run under 'win32' platform"""
