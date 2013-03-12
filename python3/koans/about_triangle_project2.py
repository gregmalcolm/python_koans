#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject2(Koan):
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        with self.assertRaises(TriangleError):
            triangle(0, 0, 0)

        with self.assertRaises(TriangleError):
            triangle(3, 4, -5)

        with self.assertRaises(TriangleError):
            triangle(1, 1, 3)

        with self.assertRaises(TriangleError):
            triangle(2, 4, 2)


