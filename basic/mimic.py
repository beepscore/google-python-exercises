#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import re
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""

    file_input = open(filename, 'r')
    string_input = file_input.read()
    words_input = re.split('\W+', string_input)
    dict = {}

    # stop at next to last word, so we don't try to access following word out of bounds.
    for index in range(0, len(words_input)-1):
        current_word = words_input[index].lower()
        next_word = words_input[index + 1].lower()
        if ( '' == current_word or
             '' == next_word ):
            break
        if current_word in dict.keys():
            # append to existing list
            dict[current_word].append(next_word)
        else:
            # add new key-value pair, use trailing comma to define new list
            current_list = [next_word,]
            #print('current_list {}'.format(current_list))
            dict[current_word] = current_list
    print(dict)
    return dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    # +++your code here+++
    return


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: ./mimic.py file-to-read'
        sys.exit(1)

dict = mimic_dict(sys.argv[1])
print_mimic(dict, '')


if __name__ == '__main__':
    main()
