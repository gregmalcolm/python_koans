#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(0, len(empty_dict))

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(2, len(babel_fish))

    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual('uno', babel_fish['one'])
        self.assertEqual('dos', babel_fish['two'])

    def test_changing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        expected = { 'two': 'dos', 'one': 'eins' }
        self.assertDictEqual(expected, babel_fish)

    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(True, dict1 == dict2)


    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys()))
        self.assertEqual(2, len(babel_fish.values()))
        self.assertEqual(True, 'one' in babel_fish.keys())
        self.assertEqual(False, 'two' in babel_fish.values())
        self.assertEqual(False, 'uno' in babel_fish.keys())
        self.assertEqual(True, 'dos' in babel_fish.values())

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards))
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])
