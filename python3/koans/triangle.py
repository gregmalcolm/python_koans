#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
# a + b + c > 2c
def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise TriangleError(AttributeError('Negative edge is not allowed'))
    if a + b + c <= 2 * max(a, b, c):
        raise TriangleError(AttributeError('largest side should be smaller than sum of 2 other sides'))
    if a == b == c:
        return 'equilateral'
    elif a == b or b == c or c == a:
        return 'isosceles'
    return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass