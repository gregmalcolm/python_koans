    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutDeletingObjects(Koan):
    def test_del_can_remove_slices(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums[1]
        del lottery_nums[2:4]

        self.assertEqual(__, lottery_nums)

    def test_del_can_remove_entire_lists(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums
        try:
            win = lottery_nums
        except Exception as e:
            pass
        self.assertMatch(__, e[0])

    # --------------------------------------------------------------------

    class ClosingSale(object):
        def __init__(self):
            self.hamsters = 7
            self.zebras = 84

        def cameras(self):
            return 34

        def toilet_brushes(self):
            return 48

        def jellies(self):
            return 5

    def test_del_can_remove_attributes(self):
        crazy_discounts = self.ClosingSale()
        del self.ClosingSale.toilet_brushes
        del crazy_discounts.hamsters

        try:
            still_available = crazy_discounts.toilet_brushes()
        except AttributeError as e:
            err_msg1 = e.args[0]

        try:
            still_available = crazy_discounts.hamsters
        except AttributeError as e:
            err_msg2 = e.args[0]

        self.assertMatch(__, err_msg1)
        self.assertMatch(__, err_msg2)

    # --------------------------------------------------------------------

    class ClintEastwood(object):
        def __init__(self):
            self._name = None

        def get_name(self):
            try:
                return self._name
            except:
                return "The man with no name"

        def set_name(self, name):
            self._name = name

        def del_name(self):
            del self._name

        name = property(get_name, set_name, del_name, \
            "Mr Eastwood's current alias")

    def test_del_works_with_properties(self):
        cowboy = self.ClintEastwood()
        cowboy.name = 'Senor Ninguno'
        self.assertEqual('Senor Ninguno', cowboy.name)

        del cowboy.name
        self.assertEqual(__, cowboy.name)

    # --------------------------------------------------------------------

    class Prisoner(object):
        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        @name.deleter
        def name(self):
            self._name = 'Number Six'

    def test_another_way_to_make_a_deletable_property(self):
        citizen = self.Prisoner()
        citizen.name = "Patrick"
        self.assertEqual('Patrick', citizen.name)

        del citizen.name
        self.assertEqual(__, citizen.name)

    # --------------------------------------------------------------------

    class MoreOrganisedClosingSale(ClosingSale):
        def __init__(self):
            self.last_deletion = None
            super(AboutDeletingObjects.ClosingSale, self).__init__()

        def __delattr__(self, attr_name):
            self.last_deletion = attr_name

    def tests_del_can_be_overriden(self):
        sale = self.MoreOrganisedClosingSale()
        self.assertEqual(5, sale.jellies())
        del sale.jellies
        self.assertEqual(__, sale.last_deletion)
