import unittest


class TestAssert(unittest.TestCase):
    def test_assert_in(self):
        a = 1
        b = [2, 3, 4]
        self.assertIn(a, b)


if __name__ == '__main__':
    unittest.main()
