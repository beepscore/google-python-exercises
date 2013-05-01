#!/usr/bin/env python3

# References
# http://docs.python.org/3.3/library/unittest.html

import unittest
import logpuzzle

class TestCopySpecial(unittest.TestCase):

    def setUp(self):
        pass

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
        ]

        for test_data in test_datas:
            test_string = test_data[test_string_index]
            result = logpuzzle.number_from_file_name(test_string)
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                                'hostname({}) expected {} but got {}'.format(test_string,
                                                                                    expected_result,
                                                                                    result))


    def test_download_images(self):

        img_urls = logpuzzle.read_urls('animal_code.google.com')
        dest_dir = './puzzle_images'
        logpuzzle.download_images(img_urls, dest_dir)


if __name__ == "__main__": unittest.main()
