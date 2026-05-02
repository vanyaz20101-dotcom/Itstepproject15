import unittest
from itstepprojectivan6test1 import *


class TestCalc(unittest.TestCase):
    def test_arg(self):
        self.assertEqual(add(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(add(x=3, y=6), 9)

    def test_mixed(self):
        self.assertEqual(add(1, 2, x=3), 6)

    def test_diff(self):
        num1 = 1
        num2 = 0
        self.assertEqual(add(0, -5, num1, a=num2), -4)

    def test_wrong_datatype(self):
        self.assertEqual(add('5', "abc", 4), 9)


if __name__ == '__main__':
    unittest.main()

