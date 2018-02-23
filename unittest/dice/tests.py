import unittest

import dice


class DiceTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        self.hand3 = dice.Roll('3d6')

    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            dice.Die(1)

    def test_adding(self):
        self.assertEqual(self.hand1+self.hand3,
                        sum(self.hand1.results)+sum(self.hand3.results))

if __name__ == '__main__':
    unittest.main()
