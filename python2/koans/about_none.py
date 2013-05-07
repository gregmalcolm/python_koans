#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *


class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(__, isinstance(None, object))

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(__, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the
        block below.

        Don't worry about what 'try' and 'except' do, we'll talk about
        this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            # What exception has been caught?
            #
            # Need a recap on how to evaluate __class__ attributes?
            #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

            self.assertEqual(__, ex.__class__)

            # What message was attached to the exception?
            # (HINT: replace __ with part of the error message.)
            self.assertMatch(__, ex.args[0])

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(____, None is not 0)
        self.assertEqual(____, None is not False)
