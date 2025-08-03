# test_aiconverter.py
"""
Tests for AIConverter module.
"""

import unittest
from aiconverter import AIConverter

class TestAIConverter(unittest.TestCase):
    """Test cases for AIConverter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AIConverter()
        self.assertIsInstance(instance, AIConverter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AIConverter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
