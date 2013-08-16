#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    def test_iterators_are_a_type(self):
        it = iter(range(1,6))

        fib = 0

        for num in it:
            fib += num

        self.assertEqual(__ , fib)

    def test_iterating_with_next(self):
        stages = iter(['alpha','beta','gamma'])

        try:
            self.assertEqual(__, next(stages))
            next(stages)
            self.assertEqual(__, next(stages))
            next(stages)
        except StopIteration as ex:
            err_msg = 'Ran out of iterations'

        self.assertRegexpMatches(err_msg, __)

    # ------------------------------------------------------------------

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]
        mapped_seq = list()

        mapping = map(self.add_ten, seq)

        self.assertNotEqual(list, mapping.__class__)
        self.assertEqual(__, mapping.__class__)
        # In Python 3 built in iterator funcs return iteratable view objects
        # instead of lists

        for item in mapping:
            mapped_seq.append(item)

        self.assertEqual(__, mapped_seq)

        # None, iterator methods actually return objects of iter type in
        # python 3. In python 2 map() would give you a list.

    def test_filter_selects_certain_items_from_a_list(self):
        def is_even(item):
            return (item % 2) == 0

        seq = [1, 2, 3, 4, 5, 6]
        even_numbers = list()

        for item in filter(is_even, seq):
            even_numbers.append(item)

        self.assertEqual(__, even_numbers)

    def test_just_return_first_item_found(self):
        def is_big_name(item):
            return len(item) > 4

        names = ["Jim", "Bill", "Clarence", "Doug", "Eli"]
        name = None

        iterator = filter(is_big_name, names)
        try:
            name = next(iterator)
        except StopIteration:
            msg = 'Ran out of big names'

        self.assertEqual(__, name)


    # ------------------------------------------------------------------

    def add(self,accum,item):
        return accum + item

    def multiply(self,accum,item):
        return accum * item

    def test_reduce_will_blow_your_mind(self):
        import functools
        # As of Python 3 reduce() has been demoted from a builtin function
        # to the functools module.

        result = functools.reduce(self.add, [2, 3, 4])
        self.assertEqual(__, result.__class__)
        # Reduce() syntax is same as Python 2

        self.assertEqual(__, result)

        result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
        self.assertEqual(__, result2)

        # Extra Credit:
        # Describe in your own words what reduce does.

    # ------------------------------------------------------------------

    def test_use_pass_for_iterations_with_no_body(self):
        for num in range(1,5):
            pass

        self.assertEqual(__, num)

    # ------------------------------------------------------------------

    def test_all_iteration_methods_work_on_any_sequence_not_just_lists(self):
        # Ranges are an iteratable sequence
        result = map(self.add_ten, range(1,4))
        self.assertEqual(__, list(result))

        try:
            file = open("example_file.txt")

            try:
                def make_upcase(line):
                    return line.strip().upper()
                upcase_lines = map(make_upcase, file.readlines())
                self.assertEqual(__, list(upcase_lines))
            finally:
                # Arg, this is ugly.
                # We will figure out how to fix this later.
                file.close()
        except IOError:
            # should never happen
            self.fail()
