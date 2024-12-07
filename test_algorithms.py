import unittest
from main import Algorithms

class TestAlgorithms(unittest.TestCase):
    # Тести для find_min_positive
    def test_find_min_positive(self):
        self.assertEqual(Algorithms.find_min_positive([3, -1, 5, 7]), 3)
        self.assertEqual(Algorithms.find_min_positive([10, 15, 2, 8]), 2)
        with self.assertRaises(ValueError):
            Algorithms.find_min_positive([-1, -5, -10])

    # Тести для sum_negative
    def test_sum_negative(self):
        self.assertEqual(Algorithms.sum_negative([-3, -5, 7, -2]), -10)
        self.assertEqual(Algorithms.sum_negative([3, 5, 7]), 0)
        self.assertEqual(Algorithms.sum_negative([-1, -2, -3]), -6)

    # Тести для fibonacci
    def test_fibonacci(self):
        self.assertEqual(Algorithms.fibonacci(0), 0)
        self.assertEqual(Algorithms.fibonacci(1), 1)
        self.assertEqual(Algorithms.fibonacci(5), 5)
        self.assertEqual(Algorithms.fibonacci(10), 55)
        with self.assertRaises(ValueError):
            Algorithms.fibonacci(-1)

    # Тести для calculate_current
    def test_calculate_current(self):
        self.assertAlmostEqual(Algorithms.calculate_current(10, 2), 5.0)
        self.assertAlmostEqual(Algorithms.calculate_current(0, 2), 0.0)
        with self.assertRaises(ValueError):
            Algorithms.calculate_current(10, 0)

if __name__ == "__main__":
    unittest.main()