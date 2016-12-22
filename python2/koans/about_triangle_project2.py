#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from triangle import *

# You need to finish implementing triangle() in the file 'triangle.py'

# Reminder: How to distinguish what are valid and invalid line lengths to make up a triangle:
# let a = length of shortest line segment
# let b = length of 2nd shortest line segment
# let c = length of longest line segment
# If a + b > c, then you can make a valid triangle out of the three line segments, otherwise you cannot.

class AboutTriangleProject2(Koan):
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        # In the code below, each line calls the specfied method with the arguments passed to it.
        # E.g. this line:
        #   self.assertRaises(TriangleError, triangle, 0, 0, 0)
        # calls triangle(0, 0, 0)
        
        # All sides should be greater than 0
        self.assertRaises(TriangleError, triangle, 0, 0, 0)
        self.assertRaises(TriangleError, triangle, 3, 4, -5)

        # The sum of any two sides should be greater than the third one
        self.assertRaises(TriangleError, triangle, 1, 1, 3)
        self.assertRaises(TriangleError, triangle, 2, 5, 2)
