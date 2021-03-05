#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMessagePassing in the Ruby Koans
#

from runner.koan import *

class AboutAttributeAccess(Koan):

    class TypicalObject:
        pass

    def test_calling_undefined_functions_normally_results_in_errors(self):
        typical = self.TypicalObject()

        with self.assertRaises(___): typical.foobar()

    def test_calling_getattribute_causes_an_attribute_error(self):
        typical = self.TypicalObject()

        with self.assertRaises(___): typical.__getattribute__('foobar')

        # THINK ABOUT IT:
        #
        # If the method __getattribute__() causes the AttributeError, then
        # what would happen if we redefine __getattribute__()?

    # ------------------------------------------------------------------

    class CatchAllAttributeReads:
        def __getattribute__(self, attr_name):
            return "Someone called '" + attr_name + "' and it could not be found"

    def test_all_attribute_reads_are_caught(self):
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(catcher.foobar, __)

    def test_intercepting_return_values_can_disrupt_the_call_chain(self):
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(catcher.foobaz, __) # This is fine

        try:
            catcher.foobaz(1)
        except TypeError as ex:
            err_msg = ex.args[0]

        self.assertRegex(err_msg, __)

        # foobaz returns a string. What happens to the '(1)' part?
        # Try entering this into a python console to reproduce the issue:
        #
        #     "foobaz"(1)
        #

    def test_changes_to_the_getattribute_implementation_affects_getattr_function(self):
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(getattr(catcher, 'any_attribute'), __)

    # ------------------------------------------------------------------

    class WellBehavedFooCatcher:
        def __getattribute__(self, attr_name):
            if attr_name[:3] == "foo":
                return "Foo to you too"
            else:
                return super().__getattribute__(attr_name)

    def test_foo_attributes_are_caught(self):
        catcher = self.WellBehavedFooCatcher()

        self.assertEqual(__, catcher.foo_bar)
        self.assertEqual(__, catcher.foo_baz)

    def test_non_foo_messages_are_treated_normally(self):
        catcher = self.WellBehavedFooCatcher()

        with self.assertRaises(___): catcher.normal_undefined_attribute

    # ------------------------------------------------------------------

    global stack_depth
    stack_depth = 0

    class RecursiveCatcher:
        def __init__(self):
            global stack_depth
            stack_depth = 0
            self.no_of_getattribute_calls = 0

        def __getattribute__(self, attr_name):
            # We need something that is outside the scope of this class:
            global stack_depth
            stack_depth += 1

            if stack_depth<=10: # to prevent a stack overflow
                self.no_of_getattribute_calls += 1
                # Oops! We just accessed an attribute (no_of_getattribute_calls)
                # Guess what happens when self.no_of_getattribute_calls is
                # accessed?

            # Using 'object' directly because using super() here will also
            # trigger a __getattribute__() call.
            return object.__getattribute__(self, attr_name)

        def my_method(self):
            pass

    def test_getattribute_is_a_bit_overzealous_sometimes(self):
        catcher = self.RecursiveCatcher()
        catcher.my_method()
        global stack_depth
        self.assertEqual(__, stack_depth)

    # ------------------------------------------------------------------

    class MinimalCatcher:
        class DuffObject: pass

        def __init__(self):
            self.no_of_getattr_calls = 0

        def __getattr__(self, attr_name):
            self.no_of_getattr_calls += 1
            return self.DuffObject

        def my_method(self):
            pass

    def test_getattr_ignores_known_attributes(self):
        catcher = self.MinimalCatcher()
        catcher.my_method()

        self.assertEqual(__, catcher.no_of_getattr_calls)

    def test_getattr_only_catches_unknown_attributes(self):
        catcher = self.MinimalCatcher()
        catcher.purple_flamingos()
        catcher.free_pie()

        self.assertEqual(__,
            type(catcher.give_me_duff_or_give_me_death()).__name__)

        self.assertEqual(__, catcher.no_of_getattr_calls)

    # ------------------------------------------------------------------

    class PossessiveSetter(object):
        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[-5:] == 'comic':
                new_attr_name = "my_" + new_attr_name
            elif attr_name[-3:] == 'pie':
                new_attr_name = "a_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    def test_setattr_intercepts_attribute_assignments(self):
        fanboy = self.PossessiveSetter()

        fanboy.comic = 'The Laminator, issue #1'
        fanboy.pie = 'blueberry'

        self.assertEqual(__, fanboy.a_pie)

        #
        # NOTE: Change the prefix to make this next assert pass
        #

        prefix = '__'
        self.assertEqual("The Laminator, issue #1", getattr(fanboy, prefix + '_comic'))

    # ------------------------------------------------------------------

    class ScarySetter:
        def __init__(self):
            self.num_of_coconuts = 9
            self._num_of_private_coconuts = 2

        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[0] != '_':
                new_attr_name = "altered_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    def test_it_modifies_external_attribute_as_expected(self):
        setter = self.ScarySetter()
        setter.e = "mc hammer"

        self.assertEqual(__, setter.altered_e)

    def test_it_mangles_some_internal_attributes(self):
        setter = self.ScarySetter()

        try:
            coconuts = setter.num_of_coconuts
        except AttributeError:
            self.assertEqual(__, setter.altered_num_of_coconuts)

    def test_in_this_case_private_attributes_remain_unmangled(self):
        setter = self.ScarySetter()

        self.assertEqual(__, setter._num_of_private_coconuts)
