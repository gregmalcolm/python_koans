#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(__, names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual(__, title)
        self.assertEqual(__, first_names)
        self.assertEqual(__, last_name)

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        self.assertEqual(__, title)
        self.assertEqual(__, first_names)
        self.assertEqual(__, last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

