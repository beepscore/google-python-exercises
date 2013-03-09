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
    """
    return year as a string
    """
    print('year_from_babyfile_string')
    match = re.search(r'Popularity in \w\w\w\w', babyfile_string)
    if match:
        print('found {}', match.group())
        year_int = match.group()[-4:]
        year = str(year_int)
    else:
        year = None
    print(year)
    return year


def baby_names_table_rows_from_babyfile_string(babyfile_string):
    """
    sample html
    <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
    <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
    <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
    """
    print('baby_names_table_rows')
    babyfile_lines = babyfile_string.split('\n')

    table_rows = []
    for line in babyfile_lines:
        match = re.search(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
        if match:
            rank = match.group(1)
            name_boy = match.group(2)
            name_girl = match.group(3)
            row = {'rank' : rank, 'name_boy' : name_boy, 'name_girl' : name_girl}
            table_rows.append(row)

    #print(table_rows)
    return table_rows


def baby_names_list_from_table_rows(a_table_rows):
    """
    reorganize list into dictionary
    """
    print('baby_names_list_from_table_rows')

    baby_names_list = []
    for row in a_table_rows:
        baby_names_list.append([row['name_boy'], row['rank']])
        baby_names_list.append([row['name_girl'], row['rank']])

    def sort_key_from_array(an_array):
        """
        return key for sorted()
        """
        return an_array[0]

    baby_names_list = sorted(baby_names_list, key=sort_key_from_array)

    #print(baby_names_list)
    return baby_names_list


def baby_names_collapsed_from_list(a_baby_names_list):
    """
    Collapse inner array to a string
    """
    print('baby_names_collapsed_from_list')

    baby_names_collapsed = []
    for baby_element in a_baby_names_list:
        baby_names_collapsed.append('{} {}'.format(baby_element[0], baby_element[1]))

    #print(baby_names_collapsed)
    return baby_names_collapsed


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
    #baby_names(babyfile_string)
    baby_names_table_rows = baby_names_table_rows_from_babyfile_string(babyfile_string)
    baby_names_list = baby_names_list_from_table_rows(baby_names_table_rows)
    baby_names_collapsed = baby_names_collapsed_from_list(baby_names_list)
    baby_names_collapsed.insert(0, year)
    #print(baby_names_collapsed)
    return baby_names_collapsed


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
        baby_names_extracted = extract_names(filename)
        print(baby_names_extracted)

if __name__ == '__main__':
    main()
