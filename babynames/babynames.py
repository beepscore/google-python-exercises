#!/usr/bin/env python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import baby_parser

"""
Baby Names exercise

Define the extract_names() function below and change main()
to call it.

Suggested milestones for incremental development
-Extract the year and print it
-Extract the names and rank numbers and just print them
-Get the names data into a dict and print it
-Build the [year, 'name rank', ... ] list and print it
-Fix main() to use the extract_names list
"""

def year_from_babyfile_string(babyfile_string):
    print('year_from_babyfile_string')
    match = re.search(r'Popularity in \w\w\w\w', babyfile_string)
    if match:
        print('found {}', match.group())
        year = match.group()[-4:]
    else:
        year = None
    print(year)
    return year


def baby_names(babyfile_string):
    parser = baby_parser.BabyParser()
    parser.feed(babyfile_string)


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    print('extract_names')
    print(filename)
    babyfile = open(filename, 'r')
    babyfile_string = babyfile.read()
    babyfile.close()
    year = year_from_babyfile_string(babyfile_string)
    baby_names(babyfile_string)

    return


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    print(args)

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in args:
        extract_names(filename)

if __name__ == '__main__':
    main()
