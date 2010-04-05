#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

__ = "-=> FILL ME IN! <=-"

class ___(Exception):
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    def assertMatch(self, pattern, string, msg=None):
        """
        Throw an exception if the regular expresson pattern is matched
        """
        # Not part of unittest, but convenient for some koans tests
        m = re.search(pattern, string)
        if not m or not m.group(0):
            raise self.failureException, \
                (msg or '{0!r} does not match {1!r}'.format(pattern, string))

    def assertNoMatch(self, pattern, string, msg=None):
        """
        Throw an exception if the regular expresson pattern is not matched
        """
        m = re.search(pattern, string)
        if m and m.group(0):
            raise self.failureException, \
                (msg or '{0!r} matches {1!r}'.format(pattern, string))
