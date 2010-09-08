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
            
        self.assertMatch(__, err_msg)

    # ------------------------------------------------------------------

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]
   
        mapped_seq = map(self.add_ten, seq)
        self.assertEqual(__, mapped_seq)
        
    def test_filter_selects_certain_items_from_a_list(self):
        def is_even(item): return (item % 2) == 0

        seq = [1, 2, 3, 4, 5, 6]
   
        even_numbers = filter(is_even, seq)
        self.assertEqual(__, even_numbers)
    
    def test_just_return_first_item_found(self):
        def is_big_name(item): return len(item) > 4
        
        names = ["Jim", "Bill", "Clarence", "Doug", "Eli"]
    
        # NOTE This still iterates through the whole names, so not particularly
        # efficient
        self.assertEqual([__], filter(is_big_name, names)[:1])
        
        # Boring but effective
        for item in names:
            if is_big_name(item):
                self.assertEqual(__, item)
                break

    # ------------------------------------------------------------------

    def add(self, accum, item):
        return accum + item

    def multiply(self, accum, item):
        return accum * item
        
    def test_reduce_will_blow_your_mind(self):        
        result = reduce(self.add, [2, 3, 4]) 
        self.assertEqual(__, result)
    
        result2 = reduce(self.multiply, [2, 3, 4], 1) 
        self.assertEqual(__, result2)
    
        # Extra Credit:
        # Describe in your own words what reduce does.
    
    # ------------------------------------------------------------------

    def test_creating_lists_with_list_comprehensions(self):        
        feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
        
        comprehension = [delicacy.capitalize() for delicacy in feast]
        
        self.assertEqual(__, comprehension[0])
        self.assertEqual(__, comprehension[2])
        
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
            # Files act like a collection of lines
            file = open("example_file.txt")
    
            def make_upcase(line) : return line.strip().upper()
            upcase_lines = map(make_upcase, file.readlines())
            self.assertEqual(__, list(upcase_lines))
            
            # NOTE: You can create your own collections that work with each,
            # map, select, etc.
        finally:
            # Arg, this is ugly.
            # We will figure out how to fix this later.
            if file: file.close()
