import pandas as pd
import pytest


class Report(object):
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def switch(self):
        self.df = self.df.T

    def sort(self, by):
        self.df = self.df.sort_values(by=by)

    def __str__(self):
        return str(self.df)


@pytest.fixture()
def my_report():
    sample_data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                   'year': [2000, 2001, 2002, 2001, 2002, 2003],
                   'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    return Report(sample_data)


def test_2string(my_report):
    assert str(my_report) == """    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2"""


def test_switch(my_report):
    my_report.switch()
    assert str(my_report) == """          0     1     2       3       4       5
state  Ohio  Ohio  Ohio  Nevada  Nevada  Nevada
year   2000  2001  2002    2001    2002    2003
pop     1.5   1.7   3.6     2.4     2.9     3.2"""


def test_sort(my_report):
    my_report.sort(by='year')
    assert str(my_report) == """    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
3  Nevada  2001  2.4
2    Ohio  2002  3.6
4  Nevada  2002  2.9
5  Nevada  2003  3.2"""
