import unittest
from main import main_test


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(0.99, main_test())


if __name__ == '__main__':
    unittest.main()
