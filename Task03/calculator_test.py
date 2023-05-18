import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        del cls.calc

    # setUp and tearDown
    # def setUp(self):
    #    self.calc = Calculator()

    # def tearDown(self):
    #   del self.calc

    def testAddPositive(self):
        a = 5
        b = 6
        expected = 11

        actual = self.calc.add(a, b)

        self.assertEqual(expected, actual)

    def testSubPositive(self):
        a = 5
        b = 6
        expected = -1

        actual = self.calc.sub(a, b)

        self.assertEqual(expected, actual)

    def testMulPositive(self):
        a = 5
        b = 6
        expected = 30

        actual = self.calc.mul(a, b)

        self.assertEqual(expected, actual)

    def testDivPositive(self):
        a = 6
        b = 2
        expected = 3

        actual = self.calc.div(a, b)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
