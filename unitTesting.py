import sys
import unittest
import io

class Calculator:

    def add(self, first_operator, second_operator):
        try:
            return (first_operator + second_operator)
        except TypeError:
             print("Use only numeric values")

class TestCalculator(unittest.TestCase):
    calculator = Calculator()

    def test_two_numbers_are_added(self):
        self.assertEqual(self.calculator.add(1,2), 3)

    def test_at_least_one_input_is_non_numeric(self):
        capture_output = io.StringIO()
        sys.stdout = capture_output
        self.calculator.add(1,"r")
        sys.stdout = sys.__stdout__
        self.assertEqual("Use only numeric values", capture_output.getValue())


if __name__== '__main__':
    unittest.main()