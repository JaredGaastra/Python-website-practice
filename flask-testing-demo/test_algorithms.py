from unittest import TestCase
from algorithms import reverse_str, factorial, is_palindrome

class AlgorithmsTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str('hello'),'olleh')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_factorial(self):
        self.assertEqual(factorial(5), 121)
        self.assertRaises(ValueError, factorial, -5)