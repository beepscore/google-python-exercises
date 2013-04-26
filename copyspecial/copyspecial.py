#!/usr/bin/env python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# https://developers.google.com/edu/python/exercises/copy-special

import sys
import re
import os
import shutil
import subprocess
import re

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def is_special_path(a_path):
    """
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
        if is_special_path(filename):
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


def copy_to(paths, dir):
    """
    given a list of paths, copies those files into the given directory
    """


def zip_to(paths, zippath):
    """
    given a list of paths, zip those files up into the given zipfile
    """


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.
    # ./copyspecial.py --todir . .

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    file_list = get_special_paths_in_dirs(args)
    print(str(file_list))

if __name__ == "__main__":
    main()
