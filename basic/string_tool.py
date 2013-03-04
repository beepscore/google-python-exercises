#!/usr/bin/env python3 -tt

"""
Utility methods for strings.
"""

class StringTool:


    def __init__(self):
        pass


    def clean_string(self, a_string):
        """
        Return string with unwanted punctuation removed.
        Currently uses str.replace()
        Could make more efficient using regular expressions re sub.
        # http://pymotw.com/2/re/
        """

        # delete double quote
        string_cleaned = a_string.replace('"', '')

        # delete unusual quote
        string_cleaned = string_cleaned.replace('`', '')

        # delete trailing quote. Use space and other punctuation to help recognize it.
        string_cleaned = string_cleaned.replace("' ", " ")
        string_cleaned = string_cleaned.replace("';", ";")
        string_cleaned = string_cleaned.replace("':", ":")
        string_cleaned = string_cleaned.replace("',", ",")
        string_cleaned = string_cleaned.replace("'.", ".")
        string_cleaned = string_cleaned.replace("'?", "?")
        string_cleaned = string_cleaned.replace("'!", "!")
        string_cleaned = string_cleaned.replace("'\n", "\n")

        # delete leading quote. Use space and other punctuation to help recognize it.
        string_cleaned = string_cleaned.replace(" '", " ")
        string_cleaned = string_cleaned.replace("-'", "-")

        # replace other punctuation with space to avoid accidentally joining words
        string_cleaned = string_cleaned.replace('\n', ' ')
        string_cleaned = string_cleaned.replace('(', ' ')
        string_cleaned = string_cleaned.replace(')', ' ')
        string_cleaned = string_cleaned.replace('-', ' ')
        string_cleaned = string_cleaned.replace('_', ' ')
        string_cleaned = string_cleaned.replace(';', ' ')
        string_cleaned = string_cleaned.replace(':', ' ')
        string_cleaned = string_cleaned.replace(',', ' ')
        string_cleaned = string_cleaned.replace('.', ' ')
        string_cleaned = string_cleaned.replace('?', ' ')
        string_cleaned = string_cleaned.replace('!', ' ')

        return string_cleaned

