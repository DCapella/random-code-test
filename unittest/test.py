import unittest

import math

class MathTests(unittest.TestCase):
    def setUp(self):
        self.temp = math.sum_list([1, 2, 3])
        self.result = 6

    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3

    def test_equal(self):
        self.assertEqual(self.temp, self.result)
    #     temp = math.sum_list([1, 2, 3])
    #     result = 6
    #     self.assertEqual(temp, result)

    def test_not_equal(self):
        self.assertNotEqual(self.temp, 0)

    def test_greater(self):
        self.assertGreater(self.temp, 0)

    def test_less(self):
        self.assertLess(self.temp, 7)

if __name__ == '__main__':
    unittest.main()
