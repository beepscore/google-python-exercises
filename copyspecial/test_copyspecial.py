#!/usr/bin/env python3

import unittest
import copyspecial

class TestCopySpecial(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_special_paths(self):
        test_dir = '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial'
        result = copyspecial.get_special_paths(test_dir)

        expected_result = [
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/__pycache__',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/xyz__hello__.txt',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/zz__something__.jpg'
        ]

        self.assertEqual(len(expected_result), len(result),
                         'get_special_paths({}) expected {} but got {}'.format(test_dir,
                                                                               len(expected_result),
                                                                               len(result)))
        self.assertEqual(expected_result, result,
                         'get_special_paths({}) expected {} but got {}'.format(test_dir,
                                                                               expected_result,
                                                                               result))


    def test_is_special_path(self):

        test_path_index = 0
        expected_result_index = 1

        test_datas = [
            ['abc', False],
            ['__bar', False],
            ['____', False],
            ['/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/copyspecial.py', False],
            ['__foo__', True],
            ['/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/xyz__hello__.txt', True],
        ]

        for test_data in test_datas:
            test_path = test_data[test_path_index]
            result = copyspecial.is_special_path(test_path)
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                            'is_special_path({}) expected {} but got {}'.format(test_path,
                                                                                expected_result,
                                                                                result))


if __name__ == "__main__": unittest.main()
