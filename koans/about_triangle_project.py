#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to write the triangle method in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject(Koan):
    def test_equilateral_triangles_have_equal_sides(self):
        self.assertEqual('equilateral', triangle(2, 2, 2))
        self.assertEqual('equilateral', triangle(10, 10, 10))

    def test_isosceles_triangles_have_exactly_two_sides_equal(self):
        self.assertEqual('isosceles', triangle(3, 4, 4))
        self.assertEqual('isosceles', triangle(4, 3, 4))
        self.assertEqual('isosceles', triangle(4, 4, 3))
        self.assertEqual('isosceles', triangle(10, 10, 2))

    def test_scalene_triangles_have_no_equal_sides(self):
        self.assertEqual('scalene', triangle(3, 4, 5))
        self.assertEqual('scalene', triangle(10, 11, 12))
        self.assertEqual('scalene', triangle(5, 4, 2))
