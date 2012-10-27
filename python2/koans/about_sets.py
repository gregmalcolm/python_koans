#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)

    def test_sets_are_unordered(self):
        self.assertEqual(set([__, __, __, __, __]), set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(__, sorted(set('13245')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = set(['MacLeod', 'Wallace', 'Willie'])
        warriors = set(['MacLeod', 'Wallace', 'Leonidas'])

        self.assertEqual(__, scotsmen - warriors)
        self.assertEqual(__, scotsmen | warriors)
        self.assertEqual(__, scotsmen & warriors)
        self.assertEqual(__, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(__, 127 in set([127, 0, 0, 1]))
        self.assertEqual(__, 'cow' not in set('apocalypse now'))

    def test_we_can_compare_subsets(self):
        self.assertEqual(__, set('cake') <= set('cherry cake'))
        self.assertEqual(__, set('cake').issubset(set('cherry cake')))

        self.assertEqual(__, set('cake') > set('pie'))
