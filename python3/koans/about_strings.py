#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):
    
    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(__, isinstance(string, str))
    
    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(__, isinstance(string, str))
    
    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(__, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(__, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(__, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual(__, string)
  
    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual(__, string)
    
    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(__, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(__, len(string))
        
    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(__, len(string))
    
    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(__, (a == b))
    
    def but_you_still_have_to_be_careful_at_the_end_of_a_triple_quoted_string(self):
        string = """Hello "world\""""
    
    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual(__, string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "World"
        self.assertEqual(__, string)
        
    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual(__, hi)
        self.assertEqual(__, there)
    
    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual(__, hi)
    
    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual(__, original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(__, len(string))
    
    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual(__, string)

    def test_formatted_values_con_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual(__, string)
    
    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions
        
        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), \
            decimal_places)
        self.assertEqual(__, string)
    
    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual(__, string[7:10])
    
    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual(__, string[1])
    
    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(__, ord('a'))      
        self.assertEqual(__, ord('b') == (ord('a') + 1))
    
    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual([__, __, __], words)
    
    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library
        
        string = "the,rain;in,spain"
        pattern = re.compile(',|;')
        
        words = pattern.split(string)
        
        self.assertListEqual([__, __, __, __], words)
        
        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual(__, string)
        self.assertEqual(__, len(string))

        # Useful in regular expressions, file paths, URLs, etc.   
      
    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual(__, ' '.join(words))

    def test_strings_can_change_case(self):
        self.assertEqual(__, 'guido'.capitalize())
        self.assertEqual(__, 'guido'.upper())
        self.assertEqual(__, 'TimBot'.lower())
        self.assertEqual(__, 'guido van rossum'.title())
        self.assertEqual(__, 'ToTaLlY aWeSoMe'.swapcase())
