#!/usr/bin/env python3

from mimic import Mimic
import unittest

class TestMimic(unittest.TestCase):

    key_index = 0
    value_index = 1
    expected_result_index = 2

    test_datas = [
        ['crown',0,"William's"],
        ['play',3,'croquet'],
    ]


    def setUp(self):
        pass


    def test_mimic_dict(self):
        self.mimic = Mimic('alice.txt')

        for test_data in self.test_datas:
            result = self.mimic.mimic_dict()[test_data[self.key_index]][test_data[self.value_index]]
            expected_result = test_data[self.expected_result_index]
            self.assertEqual(expected_result, result,
                             'mimic_dict()[{}][{}] expected {} but got {}'.format(test_data[self.key_index],
                                                                              test_data[self.value_index],
                                                                              expected_result,
                                                                              result))


    def test_mimic_dict_keys(self):
        self.mimic = Mimic('alice.txt')

        self.assertTrue('mustard' in self.mimic.mimic_dict())
        self.assertTrue('we' in self.mimic.mimic_dict())

        # test contracted words have been escaped
        self.assertTrue('I\'ve' in self.mimic.mimic_dict())
        self.assertTrue('we\'ve' in self.mimic.mimic_dict())


if __name__ == "__main__": unittest.main()
