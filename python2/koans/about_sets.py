#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']
        
        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(set(['Malcolm', 'Matunas', 'MacLeod', 'Ramirez']), there_can_only_be_only_one)

    def test_sets_are_unordered(self):
        self.assertEqual(set(['1', '3', '2', '5', '4']), set('12345'))
        
    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1','2','3','4','5'], sorted(set('12345')))
        

    # ------------------------------------------------------------------

    def chars_in(self, a_set):
        return ''.join(sorted(a_set))

    def test_set_have_arithmetic_operators(self):
        good_guy = set('macleod')
        bad_guy = set('mutunas')
        
        self.assertEqual('cdelo', self.chars_in( good_guy - bad_guy) )
        self.assertEqual('acdelmnostu', self.chars_in( good_guy | bad_guy ))       
        self.assertEqual('am', self.chars_in( good_guy & bad_guy ))
        self.assertEqual('cdelnostu', self.chars_in( good_guy ^ bad_guy ))

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in set([127, 0, 0, 1]) )
        self.assertEqual(True, 'cow' not in set('apocalypse now') )
        
    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) )
        
        self.assertEqual(False, set('cake') > set('pie'))
