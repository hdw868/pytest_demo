import pytest


class DB(object):
    """Base class"""

    def connect(self):
        print('\n\t{}connected'.format(self.__class__.__name__))

    def close(self):
        print('\n\t{}disconnected'.format(self.__class__.__name__))


class DB1(DB):
    """one database object"""


class DB2(DB):
    """alternative database object"""


@pytest.fixture(scope='session', params=['db1',
                                         'db2'])
def db(request):
    if request.param == "db1":
        db = DB1()
        db.connect()
        yield
        db.close()
    elif request.param == "db2":
        db = DB2()
        db.connect()
        yield
        db.close()

    else:
        raise ValueError("invalid internal test config")


def test_pass(db):
    assert 1


def test_fail(db):
    assert 0


def test_exception(db):
    a = 1 / 0
    assert a
