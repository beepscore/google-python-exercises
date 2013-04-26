#!/usr/bin/env python3

import unittest
import copyspecial

class TestCopySpecial(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_special_paths(self):
        test_dir = '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial'
        result = copyspecial.get_special_paths(test_dir)
        print('special_paths', result)
        # TODO: change expected_result to contain only special paths
        expected_result = [
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/.DS_Store',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/__pycache__',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/copyspecial.py',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/copyspecial.pyc',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/solution',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/test_copyspecial.py',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/test_to_dir',
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


if __name__ == "__main__": unittest.main()
