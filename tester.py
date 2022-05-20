import unittest
from validator import Validator
class PlotterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.v = Validator()
        return super().setUp()
    ## unwanted char tests

    def test_unwanted_false(self):
        self.v.polynomial = '2*x^3 - 3'
        actual = self.v.is_unwanted_chars()
        self.assertFalse(actual)

    def test_unwanted_true(self):
        self.v.polynomial = '2*x^3 - 3*y'
        actual = self.v.is_unwanted_chars()
        self.assertTrue(actual)

    ## double operator test
    def test_double_operator_false(self):
        self.v.polynomial = "2*x^3 - 3"
        self.assertFalse(self.v.is_double_operators())

    def test_double_operator_true(self):
        self.v.polynomial = "2*/x^3 - 3"
        self.assertTrue(self.v.is_double_operators())

    ## leading operator test
    def test_leading_operator_false(self):
        self.v.polynomial = "2*x^3 - 3"
        self.assertFalse(self.v.is_leading_operators())

    def test_leading_operator_true(self):
        self.v.polynomial = "/2/x^3 - 3"
        self.assertTrue(self.v.is_leading_operators())

    ## trailing operator test
    def test_leading_operator_false(self):
        self.v.polynomial = "2*x^3 - 3"
        self.assertFalse(self.v.is_trailing_operators())

    def test_leading_operator_true(self):
        self.v.polynomial = "2/x^3 - 3-"
        self.assertTrue(self.v.is_trailing_operators())

    ## bracket
    def test_brackets_false(self):
        self.v.polynomial = "2*((3*x+1))"
        self.assertFalse(self.v.is_unbalanced_brackets())

    def test_brackets_true(self):
        self.v.polynomial = "2*((3*x+1)"
        self.assertTrue(self.v.is_unbalanced_brackets())

    ## range
    def test_range_false(self):
        self.v.min = "-13.7"
        self.v.max = "100"
        self.assertFalse(self.v.is_invalid_range())
        
    def test_range_true(self):
        self.v.min = "-13.7a"
        self.v.max = "100"
        self.assertTrue(self.v.is_invalid_range())

    ## evaluation
    def test_evaluation_false(self):
        self.v.polynomial = "2*x"
        self.assertFalse(self.v.is_invalid_expression())

    def test_evaluation_true(self):
        self.v.polynomial = "2.0.0*x"
        self.assertTrue(self.v.is_invalid_expression())

    ## total
    def test_total_error(self):
        polynomial = "2*x"
        min = "13"
        max = "100"
        actual = self.v.validate_expression(polynomial, min, max)
        expected = "Success"
        self.assertEqual(actual, expected)

    ## total
    def test_total_error(self):
        polynomial = "2*x+"
        min = "13"
        max = "100"
        actual = self.v.validate_expression(polynomial, min, max)
        expected = "Invalid Input!\nTrailing Operators Not Allowed"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()