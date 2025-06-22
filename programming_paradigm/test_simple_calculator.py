import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)
        
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertEqual(self.calc.subtract(-2.7, 1.3), -4.0)
        
        # Test same numbers (should result in zero)
        self.assertEqual(self.calc.subtract(7, 7), 0)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-5, -6), 30)
        self.assertEqual(self.calc.multiply(8, -2), -16)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(1, 15), 15)
        self.assertEqual(self.calc.multiply(23, 1), 23)
        
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(20, 4), 5.0)
        
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)
        
        # Test division resulting in decimal
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(5, 4), 1.25)
        
        # Test division with decimal numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(10.0, 4.0), 2.5)
        
        # Test division by one
        self.assertEqual(self.calc.divide(42, 1), 42.0)
        self.assertEqual(self.calc.divide(-17, 1), -17.0)
        
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        # Test division by zero with positive numerator
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(5, 0))
        
        # Test division by zero with negative numerator
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(-7, 0))
        
        # Test zero divided by zero
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test decimal number divided by zero
        self.assertIsNone(self.calc.divide(3.14, 0))
        self.assertIsNone(self.calc.divide(-2.5, 0))

    def test_edge_cases(self):
        """Test additional edge cases and boundary conditions."""
        # Test very large numbers
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, large_num), 2 * large_num)
        self.assertEqual(self.calc.multiply(large_num, 2), 2 * large_num)
        
        # Test very small decimal numbers
        small_num = 0.000001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2 * small_num, places=7)
        
        # Test operations that should result in zero
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.multiply(0, 999999), 0)
        self.assertEqual(self.calc.divide(0, 1), 0.0)

if __name__ == '__main__':
    unittest.main()