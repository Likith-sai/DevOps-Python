import unittest
import sys
import os

# Add the parent directory to the system path so `main.py` can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import generate_password 
class TestPasswordGenerator(unittest.TestCase):
    
    def test_valid_password_length(self):
        """Test if the password is generated with the correct length."""
        passlen = 10
        password = generate_password(passlen)
        self.assertEqual(len(password), passlen)

    def test_zero_length_password(self):
        """Test if the function returns an empty string for length 0."""
        passlen = 0
        password = generate_password(passlen)
        self.assertEqual(password, "")

    def test_negative_length_password(self):
        """Test if the function returns an empty string for negative length."""
        passlen = -5
        password = generate_password(passlen)
        self.assertEqual(password, "")

    def test_password_length_exceeds_charset(self):
        """Test if the function handles length greater than the character set size."""
        passlen = 100
        password = generate_password(passlen)
        self.assertEqual(password, "Password length exceeds character set size.")

    def test_password_characters(self):
        """Test if the password contains only valid characters from the character set."""
        passlen = 8
        password = generate_password(passlen)
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        for char in password:
            self.assertIn(char, s)

# Run the tests
if __name__ == "__main__":
    unittest.main()
