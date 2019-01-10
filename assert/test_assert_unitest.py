import unittest


def f(a, b):
    return a + b


class TestAssert(unittest.TestCase):
    def test_assert_in(self):
        a = 1
        b = [2, 3, 4]
        self.assertIn(a, b)

    def test_function(self):
        assert f(3, 4) == 8

    def test_eq_list(self):
        long_list = [0, 1, 2] * 100
        a = long_list + [0, 1, 2]
        b = long_list + [0, 2, 1]
        assert a == b


if __name__ == '__main__':
    unittest.main()
