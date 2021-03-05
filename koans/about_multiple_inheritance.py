#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Slightly based on AboutModules in the Ruby Koans
#

from runner.koan import *

class AboutMultipleInheritance(Koan):
    class Nameable:
        def __init__(self):
            self._name = None

        def set_name(self, new_name):
            self._name = new_name

        def here(self):
            return "In Nameable class"

    class Animal:
        def legs(self):
            return 4

        def can_climb_walls(self):
            return False

        def here(self):
            return "In Animal class"

    class Pig(Animal):
        def __init__(self):
            super().__init__()
            self._name = "Jasper"

        @property
        def name(self):
            return self._name

        def speak(self):
            return "OINK"

        def color(self):
            return 'pink'

        def here(self):
            return "In Pig class"

    class Spider(Animal):
        def __init__(self):
            super().__init__()
            self._name = "Boris"

        def can_climb_walls(self):
            return True

        def legs(self):
            return 8

        def color(self):
            return 'black'

        def here(self):
            return "In Spider class"

    class Spiderpig(Pig, Spider, Nameable):
        def __init__(self):
            super(AboutMultipleInheritance.Pig, self).__init__()
            super(AboutMultipleInheritance.Nameable, self).__init__()
            self._name = "Jeff"

        def speak(self):
            return "This looks like a job for Spiderpig!"

        def here(self):
            return "In Spiderpig class"

    #
    # Hierarchy:
    #               Animal
    #              /     \
    #            Pig   Spider  Nameable
    #              \      |      /
    #                 Spiderpig
    #
    # ------------------------------------------------------------------

    def test_normal_methods_are_available_in_the_object(self):
        jeff = self.Spiderpig()
        self.assertRegex(jeff.speak(), __)

    def test_base_class_methods_are_also_available_in_the_object(self):
        jeff = self.Spiderpig()
        try:
            jeff.set_name("Rover")
        except:
            self.fail("This should not happen")
        self.assertEqual(__, jeff.can_climb_walls())

    def test_base_class_methods_can_affect_instance_variables_in_the_object(self):
        jeff = self.Spiderpig()
        self.assertEqual(__, jeff.name)

        jeff.set_name("Rover")
        self.assertEqual(__, jeff.name)

    def test_left_hand_side_inheritance_tends_to_be_higher_priority(self):
        jeff = self.Spiderpig()
        self.assertEqual(__, jeff.color())

    def test_super_class_methods_are_higher_priority_than_super_super_classes(self):
        jeff = self.Spiderpig()
        self.assertEqual(__, jeff.legs())

    def test_we_can_inspect_the_method_resolution_order(self):
        #
        # MRO = Method Resolution Order
        #
        mro = type(self.Spiderpig()).mro()
        self.assertEqual('Spiderpig', mro[0].__name__)
        self.assertEqual('Pig', mro[1].__name__)
        self.assertEqual(__, mro[2].__name__)
        self.assertEqual(__, mro[3].__name__)
        self.assertEqual(__, mro[4].__name__)
        self.assertEqual(__, mro[5].__name__)

    def test_confirm_the_mro_controls_the_calling_order(self):
        jeff = self.Spiderpig()
        self.assertRegex(jeff.here(), 'Spiderpig')

        next = super(AboutMultipleInheritance.Spiderpig, jeff)
        self.assertRegex(next.here(), 'Pig')

        next = super(AboutMultipleInheritance.Pig, jeff)
        self.assertRegex(next.here(), __)

        # Hang on a minute?!? That last class name might be a super class of
        # the 'jeff' object, but its hardly a superclass of Pig, is it?
        #
        # To avoid confusion it may help to think of super() as next_mro().
