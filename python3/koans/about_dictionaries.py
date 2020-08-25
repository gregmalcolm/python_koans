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
        self.assertEqual(len(empty_dict), len(empty_dict))

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(len(babel_fish), len(babel_fish))

    def test_accessing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(babel_fish['one'], babel_fish['one'])
        self.assertEqual(babel_fish['two'], babel_fish['two'])

    def test_changing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'dos'

        expected = {'two': 'dos', 'one': 'dos'}
        self.assertDictEqual(expected, babel_fish)

    def test_dictionary_is_unordered(self):
        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}

        self.assertEqual(dict1 == dict2, dict1 == dict2)

    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(len(babel_fish.keys()), len(babel_fish.keys()))
        self.assertEqual(len(babel_fish.values()), len(babel_fish.values()))
        self.assertEqual('one' in babel_fish.keys(),
                         'one' in babel_fish.keys())
        self.assertEqual('two' in babel_fish.values(),
                         'two' in babel_fish.values())
        self.assertEqual('uno' in babel_fish.keys(),
                         'uno' in babel_fish.keys())
        self.assertEqual('dos' in babel_fish.values(),
                         'dos' in babel_fish.values())

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie',
                             'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(len(cards), len(cards))
        self.assertEqual(cards['green elf'], cards['green elf'])
        self.assertEqual(cards['yellow dwarf'], cards['yellow dwarf'])
