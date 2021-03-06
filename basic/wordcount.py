#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
from string_tool import StringTool

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def count_words(filename):
    string_tool = StringTool()
    words_file = open(filename, 'r')
    word_counts = {}
    for line in words_file:
        cleaned_string = string_tool.clean_string(line)
        # split on whitespace
        line_list = cleaned_string.split()
        for word in line_list:
            word_lower = word.lower()
            if not (word_lower in word_counts):
                word_counts[word_lower] = 1
            else:
                word_counts[word_lower] += 1

    words_file.close()
    return word_counts


def print_words(filename):
    word_counts = count_words(filename)
    words = sorted(word_counts.keys())
    for word in words:
        print word, word_counts[word]


def print_top(filename):
    """
    print the top 20 most common words sorted
    so the most common word is first, then the next most common, and so on.
    Sorts dictionary keys list ordered by corresponding value, highest value first
    """
    word_counts = count_words(filename)
    words = sorted(word_counts.keys(), key=lambda word_key: word_counts[word_key], reverse=True)

    # if top end of range is greater than length, will use entire list
    words_top = words[:20]
    for word in words_top:
        print word, word_counts[word]


def print_top_items(filename):
    """
    print the top 20 most common words sorted
    so the most common word is first, then the next most common, and so on.
    Alternative implementation of print_top.
    Sorts dictionary items (i.e. (key, value) tuples) into a list ordered by item value, highest value first
    In Python 3, items are a view and can be iterated over.
    http://docs.python.org/3.3/library/stdtypes.html#dict-views
    """
    word_counts = count_words(filename)
    # key:item[0], value:item[1]
    items_sorted = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    # if top end of range is greater than length, will use entire list
    items_top = items_sorted[:20]
    for item in items_top:
        print item[0], item[1]


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
        print_top_items(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()
