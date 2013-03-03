#!/usr/bin/env python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Mimic pyquick exercise -- optional extra exercise.
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


class Mimic:


    def __init__(self, filename):
        self._filename = filename


    def mimic_dict(self):
        """
        Returns mimic dict mapping each word to list of words which follow it.
        """

        file_input = open(self._filename, 'r')
        string_input = file_input.read()
        words_input = re.split('\W+', string_input)
        # Make a new list, skipping any empty words.
        # Note small.txt yieds words_input with last element ''.
        # list comprehension
        # http://stackoverflow.com/questions/1450111/delete-many-elements-of-list-python
        words_cleaned = [ item for item in words_input if (item is not '') ]
        output_dict = {}

        for index in range(0, len(words_cleaned)):
            current_word = words_cleaned[index]

            if ((len(words_cleaned) - 1) == index):
                # current_word is the last word, no next word.
                # if current_word is in keys, do nothing
                # if current_word isn't in keys, add it as a key with an empty list
                if (not current_word in output_dict.keys()):
                    output_dict[current_word] = []

            else:
                # we aren't on the last word, so it's safe to reference next word
                next_word = words_cleaned[index + 1]

                if current_word in output_dict.keys():
                    # append to existing list
                    output_dict[current_word].append(next_word)
                else:
                    # add new key-value pair, use trailing comma to define new list
                    current_list = [next_word,]
                    output_dict[current_word] = current_list

        print('output_dict')
        print(output_dict)
        print()
        return output_dict


    def random_key_from_dict(self, a_dict):
        """Return a random key from dict"""
        # In Python 3, keys() is not a list
        # https://7chan.org/pr/src/OReilly_Learning_Python_4th_Edition_Oct_2009.pdf
        # pg 219
        a_dict_keys = list(a_dict.keys())
        random_key = random.choice(a_dict_keys)
        #print('random_key: {}'.format(random_key))
        #print()
        return random_key


    def random_value_from_dict(self, a_dict):
        """Return a random value from a_dict"""
        random_key = self.random_key_from_dict(a_dict)
        random_value = a_dict[random_key]
        return random_value


    def random_element_from_dict_value_list(self, a_dict_with_value_list, a_key):
        """
        a_dict_with_value_list is a dictionary with each value a list
        a_key is the key used to look up the value list
        Return a random element from value list
        Return None if key isn't in dict or if list is empty
        """

        if (a_key not in a_dict_with_value_list):
            random_element = None

        else:
            value_list = a_dict_with_value_list[a_key]
            if [] == value_list:
                # list is empty, avoid random.choice() IndexError
                random_element = None

            else:
                random_element = random.choice(value_list)

        return random_element


    def print_mimic(self, mimic_dict, word):
        """
        Given mimic dict and start word, prints 200 random words.
        """

        print('print_mimic word', word)

        if not (word in mimic_dict):
            current_word = self.random_key_from_dict(mimic_dict)
        else:
            current_word = word

        for index in range(0, 200):
            print(current_word)
            proposed_word = self.random_element_from_dict_value_list(mimic_dict, current_word)
            if (proposed_word is None):
                current_word = self.random_key_from_dict(mimic_dict)
            else:
                current_word = proposed_word

        return


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

mimic = Mimic(sys.argv[1])
mapped_dict = mimic.mimic_dict()
mimic.print_mimic(mapped_dict, '')


if __name__ == '__main__':
    main()
