#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Functions to load the test cases ("koans") that make up the
Path to Enlightenment.
'''

import io
import unittest


# The path to enlightenment starts with the following:
KOANS_FILENAME = 'koans.txt'


def filter_koan_names(lines):
    '''
    Strips leading and trailing whitespace, then filters out blank
    lines and comment lines.
    '''
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            continue
        if line:
            yield line
    return


def names_from_file(filename):
    '''
    Opens the given ``filename`` and yields the fully-qualified names
    of TestCases found inside (one per line).
    '''
    with io.open(filename, 'rt', encoding='utf8') as names_file:
        for name in filter_koan_names(names_file):
            yield name
    return


def koans_suite(names):
    '''
    Returns a ``TestSuite`` loaded with all tests found in the given
    ``names``, preserving the order in which they are found.
    '''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    for name in names:
        tests = loader.loadTestsFromName(name)
        suite.addTests(tests)
    return suite


def koans(filename=KOANS_FILENAME):
    '''
    Returns a ``TestSuite`` loaded with all the koans (``TestCase``s)
    listed in ``filename``.
    '''
    names = names_from_file(filename)
    return koans_suite(names)
