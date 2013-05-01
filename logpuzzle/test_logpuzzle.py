#!/usr/bin/env python3

# References
# http://docs.python.org/3.3/library/unittest.html

import unittest
import logpuzzle
import shutil
import os
import difflib

class TestCopySpecial(unittest.TestCase):

    def setUp(self):
        pass


    def clean_up_image_dir(self):
        # for safety against accidentally deleting a valuable directory, hardcode path
        image_dir = './puzzle_images'
        print('removing directory', image_dir)
        input('Press Return key to remove. Press Ctrl-C to exit.')
        shutil.rmtree(image_dir)


    def test_path_from_string(self):

        test_string_index = 0
        expected_result_index = 1

        test_datas = [
            ['10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"',
             '/~foo/puzzle-bar-aaab.jpg'],
            ['GET /~foo/puzzle-bar-aaab.jpg HTTP', '/~foo/puzzle-bar-aaab.jpg'],
            ['GET    /~foo/puzzle-bar-aaab.jpg    HTTP', '/~foo/puzzle-bar-aaab.jpg'],
            ['GET  xx    HTTP', 'xx'],
            ['', None],
            ['GET     HTTP', None],
            [' /~foo/puzzle-bar-aaab.jpg ', None],
        ]

        for test_data in test_datas:
            test_string = test_data[test_string_index]
            result = logpuzzle.path_from_string(test_string)
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'path_from_string({}) expected {} but got {}'.format(test_string,
                                                                                 expected_result,
                                                                                 result))


    def test_hostname(self):

        test_string_index = 0
        expected_result_index = 1

        test_datas = [
            ['', None],
            ['_', None],
            ['_ ', ' '],
            ['_x', 'x'],
            ['a_x', 'x'],
            ['code.google.com', None],
            ['animal_code.google.com', 'code.google.com'],
            ['_code.google.com', 'code.google.com'],
        ]

        for test_data in test_datas:
            test_string = test_data[test_string_index]
            result = logpuzzle.hostname(test_string)
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'hostname({}) expected {} but got {}'.format(test_string,
                                                                                 expected_result,
                                                                                 result))


    def test_image_path(self):

        test_image_dir_index = 0
        test_img_url_index = 1
        test_index_index = 2
        expected_result_index = 3

        test_datas = [
            ['./puzzle_images', '/~foo/puzzle-bar-aaab.jpg', 0, './puzzle_images/img0.jpg'],
            ['moe', 'larry.jpg', 2, 'moe/img2.jpg'],
            ['a', 'b.png', 5, 'a/img5.png'],
        ]

        for test_data in test_datas:
            result = logpuzzle.image_path(test_data[test_image_dir_index],
                                          test_data[test_img_url_index],
                                          test_data[test_index_index])
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'test_image_path() expected {} but got {}'.format(expected_result, result))


    def test_is_puzzle_url(self):

        test_string_index = 0
        expected_result_index = 1

        test_datas = [
            ['', False],
            ['GET  xx    HTTP', False],
            ['GET     HTTP', False],
            [' /~foo/puzzle-bar-aaab.jpg ', False],
            ['10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"', True],
            ['GET /~foo/puzzle-bar-aaab.jpg HTTP', True],
            ['GET    /~foo/puzzle-bar-aaab.jpg    HTTP', True],
        ]

        for test_data in test_datas:
            test_string = test_data[test_string_index]
            result = logpuzzle.is_puzzle_url(test_string)
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'is_puzzle_url({}) expected {} but got {}'.format(test_string,
                                                                                 expected_result,
                                                                                 result))


    def test_read_urls(self):

        results = logpuzzle.read_urls('animal_code.google.com')

        expected_result = 20
        self.assertEqual(expected_result, len(results),
                         'expected {} but got {}'.format(
                             expected_result,
                             len(results)))

        test_index = 0
        expected_result_index = 1

        test_datas = [
            [0, 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg'],
            [19, 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babj.jpg'],
        ]

        for test_data in test_datas:
            result = results[test_data[test_index]]
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'read_urls()[{}] expected {} but got {}'.format(test_index,
                                                                                 expected_result,
                                                                                 result))


    def test_number_from_file_name(self):
        test_string_index = 0
        expected_result_index = 1

        test_datas = [
            ['img0.jpg', 0],
            ['img2.jpg', 2],
            ['img19.jpg', 19],
            ['19.jpg', 19],
            ['img.jpg', None],
            ['', None],
        ]

        for test_data in test_datas:
            test_string = test_data[test_string_index]
            result = logpuzzle.number_from_file_name(test_string)
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'number_from_file_name({}) expected {} but got {}'.format(test_string,
                                                                                       expected_result,
                                                                                       result))


    def test_write_index_file(self):
        """
        http://stackoverflow.com/questions/977491/comparing-2-txt-files-using-difflib-in-python
        http://doughellmann.com/2007/10/pymotw-difflib.html
        """
        img_urls = logpuzzle.read_urls('animal_code.google.com')
        dest_dir = './puzzle_images'
        logpuzzle.download_images(img_urls, dest_dir)

        logpuzzle.write_index_file(dest_dir)

        index_file = open('./index.html', 'r')
        result_lines = index_file.readlines()
        index_file.close()

        index_expected_file = open('./index_expected.html', 'r')
        expected_result_lines = index_expected_file.readlines()
        index_expected_file.close()

        # put expected_result_lines first, to make diff +- clearer
        diff_unified = difflib.unified_diff(expected_result_lines, result_lines, lineterm='')
        result = ('\n'.join(list(diff_unified)))
        expected_result = ''
        self.assertEqual(expected_result, result,
                             'write_index_file() expected {} but got {}'.format(expected_result, result))
        self.clean_up_image_dir()


    def test_z_download_images(self):
        """ Choose test name alphabetically after test_write_index_file to run after it.
        """
        img_urls = logpuzzle.read_urls('animal_code.google.com')
        dest_dir = './puzzle_images'
        logpuzzle.download_images(img_urls, dest_dir)

        result = os.listdir(dest_dir)
        expected_result = ['img0.jpg', 'img1.jpg', 'img10.jpg', 'img11.jpg', 'img12.jpg', 'img13.jpg', 'img14.jpg', 'img15.jpg', 'img16.jpg', 'img17.jpg', 'img18.jpg', 'img19.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg', 'img6.jpg', 'img7.jpg', 'img8.jpg', 'img9.jpg']
        self.assertEqual(expected_result, result,
                             'write_index_file() expected {} but got {}'.format(expected_result, result))


if __name__ == "__main__": unittest.main()
