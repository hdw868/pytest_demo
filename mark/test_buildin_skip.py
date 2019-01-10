import pytest
import sys

a = 2
# module-level mark
pytestmark = pytest.mark.skipif(a == 1, reason='may be test data is corrupted!')


def test_a():
    """no skip mark function"""


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    raise NotImplemented


@pytest.mark.skipif(sys.version_info < (3, 6),
                    reason="requires python3.6 or higher")
def test_function():
    """requires python3.6 or higher"""


# class-level mark
@pytest.mark.skipif(sys.platform == 'win32',
                    reason="does not run on windows")
class TestPosixCalls(object):

    def test_function(self):
        """will not be setup or run under 'win32' platform"""
