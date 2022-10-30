import unittest
from npyvi import npvi


class NpyviUnitTest(unittest.TestCase):
    def test_toussaint_array_A(self):
        """Test array A from Toussaint (2012), p. 1001"""
        actual = npvi(2, 5, 1, 3)
        expected = 106.3
        self.assertAlmostEqual(actual, expected, places=1)

    def test_toussaint_array_B(self):
        """Test array B from Toussaint (2012), p. 1001"""
        actual = npvi(1, 3, 6, 2, 5)
        expected = 88.1
        self.assertAlmostEqual(actual, expected, places=1)

    def test_livingstone_array(self):
        """Test multidimensional array from Livingstone (2011) documentation"""
        actual = npvi([1, 2, 3], [3, 3, 6], [4, 6, 8], [4, 7, 7])
        expected = [53.3333, 33.3333, 34.2857, 27.2727]
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e, places=4)

    def test_invalid_arguments(self):
        """Test that we throw an error when both individual values and an array of values are provided as arguments"""
        self.assertRaises(TypeError, npvi, 1, 2, 3, [3, 2, 1])

    def test_no_arguments(self):
        """Test that we receive a value of -0.0 if no arguments were passed"""
        actual = npvi()
        expected = -0.0
        self.assertEqual(actual, expected)

    def test_ignore_non_numeric_args(self):
        """Test that we ignore non-numeric arguments when passed in an iterable"""
        i_am_a_string = 'I am a string!'
        and_i_am_a_function = lambda _: _
        actual = npvi([1, i_am_a_string, 2, 3], [1, 2, and_i_am_a_function, 3])
        expected = [53.333333333333336, 53.333333333333336]
        self.assertEqual(actual, expected)

    def test_divide_by_zero_error(self):
        """Test that we raise a ZeroDivisionError when passing in at least two successive arguments that equal 0"""
        self.assertRaises(ZeroDivisionError, npvi, 0, 0, 1, 2)
