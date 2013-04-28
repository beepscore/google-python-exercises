#!/usr/bin/env python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# References:
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# https://developers.google.com/edu/python/exercises/copy-special

# http://docs.python.org/3.3/library/argparse.html?highlight=argparse#argparse
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import sys
import re
import os
import shutil
import subprocess
import argparse
from argparse import RawTextHelpFormatter

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def is_special_path(a_path):
    """
    a_path may be a file or a directory
    if path is not special, return false
    if path is special, return true
    """
    # match may return None. None evaluates to False
    match = re.search(r'__\w+__', a_path)
    if not match:
        is_special = False
    else:
        is_special = True
    return is_special


def get_special_paths(a_dir):
    """
    return a list of the absolute paths of the special files in the given directory
    """
    filenames = os.listdir(a_dir)
    file_list = []
    for filename in filenames:
        if ((not os.path.isdir(filename)) and is_special_path(filename)):
            a_path = os.path.join(a_dir, filename)
            absolute_path = os.path.abspath(a_path)
            file_list.append(absolute_path)
    return file_list


def get_special_paths_in_dirs(a_dirs):
    """
    return a list of the absolute paths of the special files in a list of directories
    """
    file_list = []
    for dirname in a_dirs:
        files_in_dirname = get_special_paths(dirname)
        # extend, not append
        file_list.extend(files_in_dirname)
    return file_list


def copy_to(paths, a_dir):
    """
    given a list of paths, copies those files into the given directory
    specification says use shutil
    """
    for path in paths:
        # copytree will copy a directory, not a file
        #shutil.copytree(path, a_dir)
        # copy2 will copy a file, not a directory
        shutil.copy2(path, a_dir)


def zip_to(paths, zippath):
    """
    given a list of paths, zip those files up into the given zipfile
    """
    ziplist = ['zip', '-j', zippath]
    ziplist.extend(paths)
    subprocess.call(ziplist)


def main():
    """
        Read arguments from command line or from a file.
    """

    parser = argparse.ArgumentParser(description='''    For help, use argument -h
    $ ./copyspecial.py -h
    To specify an argument, prefix with --
    $ python3 copyspecial.py --fromdir "." --todir "./test_to_dir" --tozip "test.zip"''',
                                    formatter_class=RawTextHelpFormatter,
                                    )

    parser.add_argument('--fromdir', action="store", dest="fromdir",
                        help = 'directory to search for file names containing "__\w__"')
    parser.add_argument('--todir', action="store", dest="todir",
                        help = 'directory to copy files to')
    parser.add_argument('--tozip', action="store", dest="tozip",
                        help = 'zip file to write files to e.g. "test.zip"')

    arguments = parser.parse_args()
    print(arguments)
    print(arguments.fromdir)
    print(arguments.todir)
    print(arguments.tozip)

    # Call your functions
    file_list = get_special_paths_in_dirs(arguments.fromdir)

    if (not arguments.todir) and (not arguments.tozip):
        print('File list')
        for filename in file_list:
            print(filename)
        sys.exit(1)

    if arguments.todir:
        copy_to(file_list, arguments.todir)
    if arguments.tozip:
        zip_to(file_list, arguments.tozip)

if __name__ == "__main__":
    main()
