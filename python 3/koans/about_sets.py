#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']
        
        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual(__, {1, 2, 3})
        self.assertEqual(__, set())

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Sets have only started using braces since Python 3

        self.assertEqual(__, type({1, 2, 3}).__name__)
        self.assertEqual(__, type({'one': 1, 'two': 2}).__name__)
        
        self.assertEqual(__, type({}).__name__)

    def test_creating_sets_using_strings(self):
        self.assertEqual(__, {'12345'})
        self.assertEqual(__, set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(__, sorted(set('12345')))
        
    # ------------------------------------------------------------------

    def chars_in(self, a_set):
        return ''.join(sorted(a_set))

    def test_set_have_arithmetic_operators(self):
        good_guy = set('macleod')
        bad_guy = set('mutunas')
        
        self.assertEqual(__, self.chars_in( good_guy - bad_guy) )
        self.assertEqual(__, self.chars_in( good_guy | bad_guy ))       
        self.assertEqual(__, self.chars_in( good_guy & bad_guy ))
        self.assertEqual(__, self.chars_in( good_guy ^ bad_guy ))

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(__, 127 in {127, 0, 0, 1} )
        self.assertEqual(__, 'cow' not in set('apocalypse now') )
        
    def test_we_can_compare_subsets(self):
        self.assertEqual(__, set('cake') <= set('cherry cake'))
        self.assertEqual(__, set('cake').issubset(set('cherry cake')) )
        
        self.assertEqual(__, set('cake') > set('pie'))
