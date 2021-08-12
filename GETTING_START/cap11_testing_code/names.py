#test procedure to test the functions get_formatted_name in name_function
from logging import Formatter
from name_function import get_formatted_name

##we shoudl import the unittest library
import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Test if names with first and last works"""
        form_name = get_formatted_name('pamela', 'pasinato')
        self.assertEqual(form_name, 'Pamela Pasinato')

    def test_first_middle_last_name(self):
        """Test if a name with middle name works"""
        form_name = get_formatted_name('jardiel', 'cunha', 'freitas')
        self.assertEqual(form_name, 'Jardiel Freitas Cunha')

unittest.main()