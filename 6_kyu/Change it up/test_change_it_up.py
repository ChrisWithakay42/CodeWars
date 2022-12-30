import unittest
from change_it_up import changer


class TestChanger(unittest.TestCase):

    def test_chars_shifted_by_one(self):
        self.assertEqual(changer('Cat30'), 'Dbu30')
