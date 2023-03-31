import unittest

from basics.functions import calculate_fuel


class MyTestCase(unittest.TestCase):

    def test_mass_12(self):
        self.assertEqual(2, calculate_fuel(12))

    def test_mass_100756(self):
        self.assertEqual(33583, calculate_fuel(100756))

    def test_mass_negative(self):
        self.assertEqual(None, calculate_fuel(-1))

    def test_string(self):
        self.assertEqual(None, calculate_fuel("test"))

    def test_zero(self):
        self.assertEqual(None, calculate_fuel(0))

    def test_min_positive_mass(self):
        self.assertEqual(1, calculate_fuel(1))


if __name__ == '__main__':
    unittest.main()
