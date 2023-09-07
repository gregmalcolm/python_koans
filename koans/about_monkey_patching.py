#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Related to AboutOpenClasses in the Ruby Koans
#

from runner.koan import *

class AboutMonkeyPatching(Koan):
    class Dog:
        def bark(self):
            return "WOOF"

    def test_as_defined_dogs_do_bark(self):
        fido = self.Dog()
        self.assertEqual("WOOF", fido.bark())

    # ------------------------------------------------------------------

    # Add a new method to an existing class.
    def test_after_patching_dogs_can_both_wag_and_bark(self):
        def wag(self): return "HAPPY"
        self.Dog.wag = wag

        fido = self.Dog()
        self.assertEqual("HAPPY", fido.wag())
        self.assertEqual("WOOF", fido.bark())

    # ------------------------------------------------------------------

    def test_most_built_in_classes_cannot_be_monkey_patched(self):
        try:
            int.is_even = lambda self: (self % 2) == 0
        except Exception as ex:
            err_msg = ex.args[0]

        self.assertRegex(err_msg, "can't set attributes")

    # ------------------------------------------------------------------

    class MyInt(int): pass

    def test_subclasses_of_built_in_classes_can_be_be_monkey_patched(self):
        self.MyInt.is_even = lambda self: (self % 2) == 0

        self.assertEqual(False, self.MyInt(1).is_even())
        self.assertEqual(True, self.MyInt(2).is_even())
