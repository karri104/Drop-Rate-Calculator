import unittest
from calculations import *

class TestCalculations(unittest.TestCase):
    def test_calc_fac(self):
        self.assertEqual(3628800, calc_fac(10)[10])
        self.assertEqual(1, calc_fac(0)[0])

    def test_pmf(self):
        #Tests that the calculated partial pmf is within 10^-9 of expected value
        self.assertTrue(10 ** (-9) > abs(0.04827976227 - pmf([1, 16], 5, 1)))

    def test_bc(self):
        self.assertEqual(5, bc(5, 1, calc_fac(5)))

    def test_calc_single(self):
        #Tests that the probability of a single event is within 10^-8 of expected value
        self.assertTrue(10 ** (-8) > abs(24.13988113 - calc_single([1, 16], 5, 1)))

    def test_calc_probabilities(self):
        pass

    def test_main(self):
        pass