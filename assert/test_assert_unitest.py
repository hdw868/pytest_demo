import unittest


class TestAssert(unittest.TestCase):
    def test_assert_info(self):
        a = 1
        b = [2, 3, 4]
        self.assertIn(a, b)


if __name__ == '__main__':
    unittest.main()
