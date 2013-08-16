#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutComprehension(Koan):


    def test_creating_lists_with_list_comprehensions(self):
        feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

        comprehension = [delicacy.capitalize() for delicacy in feast]

        #self.assertEqual(__, comprehension[0])
        #self.assertEqual(__, comprehension[2])

    def test_filtering_lists_with_list_comprehensions(self):
        feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

        comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

        self.assertEqual(__, len(feast))
        self.assertEqual(__, len(comprehension))

    def test_unpacking_tuples_in_list_comprehensions(self):
        list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
        comprehension = [ skit * number for number, skit in list_of_tuples ]

        self.assertEqual(__, comprehension[0])
        self.assertEqual(__, len(comprehension[2]))

    def test_double_list_comprehention(self):
        list_of_eggs = ['poached egg', 'fried egg']
        list_of_meats = ['lite spam', 'ham spam', 'fried spam']


        comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]


        self.assertEqual(__, len(comprehension))
        self.assertEqual(__, comprehension[0])

    def test_creating_a_set_with_set_comprehention(self):
        comprehension = { x for x in 'aabbbcccc'}

        self.assertequal(__, len(comprehension))  # remeber that set members are unique

    def test_creating_a_dictionary_with_dictionary_comprehention(self):
        dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                           'third':'ruthless efficiency', 'forth':'fanatical devotion', 'fifth': None}

        dict_comprehention = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

        self.assertEqual(__, 'first' in dict_comprehention)
        self.assertEqual(__, 'FIRST' in dict_comprehention)
        self.assertEqual(__, len(dict_of_weapons))
        self.assertEqual(__, len(dict_comprehention))
