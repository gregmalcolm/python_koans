#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(len(empty_list), len(empty_list))

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(noms[0], noms[0])
        self.assertEqual(noms[3], noms[3])
        self.assertEqual(noms[-1], noms[-1])
        self.assertEqual(noms[-3], noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(noms[0:1], noms[0:1])
        self.assertEqual(noms[0:2], noms[0:2])
        self.assertEqual(noms[2:2], noms[2:2])
        self.assertEqual(noms[2:20], noms[2:20])
        self.assertEqual(noms[4:0], noms[4:0])
        self.assertEqual(noms[4:100], noms[4:100])
        self.assertEqual(noms[5:0], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(noms[2:], noms[2:])
        self.assertEqual(noms[:2], noms[:2])

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual(list(range(5)), list(range(5)))
        self.assertEqual(list(range(5, 9)), list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual(list(range(5, 3, -1)), list(range(5, 3, -1)))
        self.assertEqual(list(range(0, 8, 2)), list(range(0, 8, 2)))
        self.assertEqual(list(range(1, 8, 3)), list(range(1, 8, 3)))
        self.assertEqual(list(range(5, -7, -4)), list(range(5, -7, -4)))
        self.assertEqual(list(range(5, -8, -4)), list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(knight, knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(knight, knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual(stack, stack)

        popped_value = stack.pop()
        self.assertEqual(popped_value, popped_value)
        self.assertEqual(stack, stack)

        popped_value = stack.pop(1)
        self.assertEqual(popped_value, popped_value)
        self.assertEqual(stack, stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual(queue, queue)

        popped_value = queue.pop(0)
        self.assertEqual(popped_value, popped_value)
        self.assertEqual(queue, queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.
