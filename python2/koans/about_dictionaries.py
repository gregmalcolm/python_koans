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
        self.assertEqual(dict(), empty_dict)
        self.assertEqual(__, len(empty_dict))

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, len(babel_fish))

    def test_accessing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, babel_fish['one'])
        self.assertEqual(__, babel_fish['two'])

    def test_changing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'eins'

        expected = {'two': 'dos', 'one': __}
        self.assertEqual(expected, babel_fish)

    def test_dictionary_is_unordered(self):
        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}

        self.assertEqual(____, dict1 == dict2)

    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, len(babel_fish.keys()))
        self.assertEqual(__, len(babel_fish.values()))
        self.assertEqual(__, 'one' in babel_fish.keys())
        self.assertEqual(__, 'two' in babel_fish.values())
        self.assertEqual(__, 'uno' in babel_fish.keys())
        self.assertEqual(__, 'dos' in babel_fish.values())

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(
            ('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf',
             'confused looking zebra'),
            42)

        self.assertEqual(__, len(cards))
        self.assertEqual(__, cards['green elf'])
        self.assertEqual(__, cards['yellow dwarf'])
