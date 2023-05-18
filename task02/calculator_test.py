import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    # Arrange
    # Act
    # Assert

    def testAddPositive(self):
        a = 5
        b = 6
        expected = 11

        actual = Calculator.add(a, b)

        self.assertEqual(expected, actual)

    def testSubPositive(self):
        a = 5
        b = 6
        expected = -1

        actual = Calculator.sub(a, b)

        self.assertEqual(expected, actual)

    def testMulPositive(self):
        a = 5
        b = 6
        expected = 30

        actual = Calculator.mul(a, b)

        self.assertEqual(expected, actual)

    def testDivPositive(self):
        a = 6
        b = 2
        expected = 3

        actual = Calculator.div(a, b)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
