#!/usr/bin/env python3

from mimic import Mimic
import unittest

class TestMimic(unittest.TestCase):


    def setUp(self):
        pass


    def test_mimic_dict(self):
        self.mimic = Mimic('alice.txt')

        result = self.mimic.mimic_dict()['crown'][0]
        self.assertEqual('William', result)

        result = self.mimic.mimic_dict()['play'][3]
        self.assertEqual('croquet', result)

if __name__ == "__main__": unittest.main()
