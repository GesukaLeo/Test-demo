import unittest
from app import *
class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)
    def test_add_Two_Numbers(self):
        self.assertEqual(add_Two_Numbers(3.5),8)

if __name__ == "__main__":
    unittest.main()