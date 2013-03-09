#!/usr/bin/env python3 -tt

# http://docs.python.org/3/library/html.parser.html
import html.parser
from html.entities import name2codepoint


class BabyParser(html.parser.HTMLParser):
    """
    Parse a babyfile_string

    Here's what the html looks like in the baby.html files

    <h3 align="center">Popularity in 1990</h3>

    <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
    <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
    <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
    """

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)


    def handle_endtag(self, tag):
        print("End tag  :", tag)


    def handle_data(self, data):
        print("Data     :", data)


    def handle_comment(self, data):
        print("Comment  :", data)


    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)


    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)


    def handle_decl(self, data):
        print("Decl     :", data)

