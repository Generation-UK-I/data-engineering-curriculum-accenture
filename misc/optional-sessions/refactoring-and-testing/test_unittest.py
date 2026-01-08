import unittest
from functions import *

class TestMathMethods(unittest.TestCase):

    def test_add_two_numbers(self):
    # Assemble
        a = 2
        b = 3
        expected = 5
    # Act
        actual = add_two_numbers(a,b)
    # Assert
        self.assertEqual(expected, actual)

    def test_minus_two_numbers(self):
    # Assemble
        a = 5
        b = 3
        expected = 0
    # Act
        actual = minus_two_numbers(a,b)
    # Assert
        # assert expected == actual
        self.assertNotEqual(expected, actual)

    # def add_mix_two_numbers(a,b):
    #     return add_two_numbers(a, b) + mix_two_numbers(a, b)

    def test_add_mix_two_numbers(self):
    # Assemble
        a = 2
        b = 3
        expected = 13
    # Act
        actual = add_mix_two_numbers(a,b)
    # Assert
        self.assertEqual(expected, actual)


    def test_math_operation(self):

    # Assemble
        a = 6
        b = 15
        result = 10 
        test = "minus"
        expected = 1

    # Act
        actual = math_operation(a, b, result, test)

    # Assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
