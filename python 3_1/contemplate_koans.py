#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Acknowledgment:
#
# Python Koans is a port of Ruby Koans originally written by Jim Weirich
# and Joe O'brien of Edgecase. There are some differences and tweaks specific
# to the Python language, but a great deal of it has been copied wholesale.
# So thank guys!
#

import unittest
import sys

if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("\nThis is the Python 3 version of Python Koans, but you are " +
            "running it with Python 2 or older!\n\n"
            "Did you accidentally use the wrong python script? \nTry:\n\n" +
            "    python3 contemplate_koans.py\n")
    else:        
        from runner.mountain import Mountain

        Mountain().walk_the_path(sys.argv)
