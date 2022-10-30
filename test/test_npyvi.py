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
