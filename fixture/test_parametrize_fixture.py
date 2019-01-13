import pytest


class Session(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data_dir = 'tmp/{}'.format(username)


@pytest.fixture(params=[('user1', 'pwd1'),
                        ('user2', 'pwd2'),
                        ('user3', 'pwd3'),
                        ('user4', 'pwd4'),
                        ])
def session(request):
    return Session(*request.param)


def test_f1(session):
    assert session.data_dir == '', 'for demo'
