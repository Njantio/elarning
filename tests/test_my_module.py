import unittest
from src.my_module import some_function

class TestMyModule(unittest.TestCase):
    def test_some_function(self):
        self.assertEqual(some_function(3, 4), 7)
