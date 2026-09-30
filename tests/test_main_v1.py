import pytest

from my_app import main_v1
#import unittest

# class TestMain(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(main_v1.add(1, 2), 3)
#         self.assertEqual(main_v1.add(-1, 1), 0)
#         self.assertEqual(main_v1.add(4, 1), 5)

def test_add():
    assert main_v1.add(1, 3) == 4

def test_add_2():
    assert main_v1.add(1, -1) == 0

def test_add_3():
    assert main_v1.add(5, 4) == 9


# if __name__ == '__main__':
#     unittest.main()