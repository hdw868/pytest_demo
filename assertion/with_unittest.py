import unittest


def foo():
    return 1


class TestAssert(unittest.TestCase):
    def test_simple_case(self):
        b = [2, 3, 4]
        self.assertIn(foo(), b)


if __name__ == '__main__':
    unittest.main()
