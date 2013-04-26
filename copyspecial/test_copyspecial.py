#!/usr/bin/env python3

# References
# http://docs.python.org/3.3/library/unittest.html

import unittest
import copyspecial
import os

class TestCopySpecial(unittest.TestCase):

    def setUp(self):
        pass


    def get_paths(self, a_dir):
        """
        return a list of the absolute paths of the files in the given directory
        """

        filenames = os.listdir(a_dir)
        file_list = []
        for filename in filenames:
            a_path = os.path.join(a_dir, filename)
            absolute_path = os.path.abspath(a_path)
            file_list.append(absolute_path)
        return file_list


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

        test_dir = '.'
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


    def test_get_special_paths_in_dirs(self):
        """
        TODO: Test 2 directories with repeated files
        """
        test_dirs = ['/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial',
                     '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/test_from_dir']
        result = copyspecial.get_special_paths_in_dirs(test_dirs)

        expected_result = [
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/__pycache__',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/xyz__hello__.txt',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/zz__something__.jpg',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/test_from_dir/anotherxyz__hello__.txt',
        ]

        self.assertEqual(len(expected_result), len(result),
                         'get_special_paths_in_dirs({}) expected {} but got {}'.format(test_dirs,
                                                                                       len(expected_result),
                                                                                       len(result)))
        self.assertEqual(expected_result, result,
                         'get_special_paths_in_dirs({}) expected {} but got {}'.format(test_dirs,
                                                                                       expected_result,
                                                                                       result))


    def test_is_special_path(self):

        test_path_index = 0
        expected_result_index = 1

        test_datas = [
            ['', False],
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


    def test_copy_to(self):
        paths = [
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/__pycache__',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/xyz__hello__.txt',
            '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/zz__something__.jpg'
        ]
        test_to_dir = '/Users/stevebaker/Documents/projects/pythonProjects/google-python-exercises/copyspecial/test_to_dir'
        copyspecial.copy_to(paths, test_to_dir)
        #TODO: assert directory contents, then delete directory contents for next test


if __name__ == "__main__": unittest.main()
