#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import unittest

from runner import path_to_enlightenment as pte


# REMOVE THESE!  They're only needed for initial test of the new loader.
from koans.about_asserts import AboutAsserts
from koans.about_strings import AboutStrings
from koans.about_none import AboutNone
from koans.about_lists import AboutLists
from koans.about_list_assignments import AboutListAssignments
from koans.about_dictionaries import AboutDictionaries
from koans.about_string_manipulation import AboutStringManipulation
from koans.about_tuples import AboutTuples
from koans.about_methods import AboutMethods
from koans.about_control_statements import AboutControlStatements
from koans.about_true_and_false import AboutTrueAndFalse
from koans.about_sets import AboutSets
from koans.about_triangle_project import AboutTriangleProject
from koans.about_exceptions import AboutExceptions
from koans.about_triangle_project2 import AboutTriangleProject2
from koans.about_iteration import AboutIteration
from koans.about_comprehension import AboutComprehension
from koans.about_generators import AboutGenerators
from koans.about_lambdas import AboutLambdas
from koans.about_scoring_project import AboutScoringProject
from koans.about_classes import AboutClasses
from koans.about_new_style_classes import AboutNewStyleClasses
from koans.about_with_statements import AboutWithStatements
from koans.about_monkey_patching import AboutMonkeyPatching
from koans.about_dice_project import AboutDiceProject
from koans.about_method_bindings import AboutMethodBindings
from koans.about_decorating_with_functions import AboutDecoratingWithFunctions
from koans.about_decorating_with_classes import AboutDecoratingWithClasses
from koans.about_inheritance import AboutInheritance
from koans.about_multiple_inheritance import AboutMultipleInheritance
from koans.about_regex import AboutRegex
from koans.about_scope import AboutScope
from koans.about_modules import AboutModules
from koans.about_packages import AboutPackages
from koans.about_class_attributes import AboutClassAttributes
from koans.about_attribute_access import AboutAttributeAccess
from koans.about_deleting_objects import AboutDeletingObjects
from koans.about_proxy_object_project import *
from koans.about_extra_credit import AboutExtraCredit


def original_test_suite():
    loader = unittest.TestLoader()
    original_suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    original_suite.addTests(loader.loadTestsFromTestCase(AboutAsserts))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutStrings))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutNone))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutLists))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutListAssignments))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutDictionaries))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutStringManipulation))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutTuples))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutMethods))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutControlStatements))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutTrueAndFalse))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutSets))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutTriangleProject))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutExceptions))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutTriangleProject2))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutIteration))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutComprehension))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutGenerators))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutLambdas))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutScoringProject))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutClasses))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutNewStyleClasses))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutWithStatements))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutMonkeyPatching))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutDiceProject))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutMethodBindings))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutDecoratingWithFunctions))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutDecoratingWithClasses))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutInheritance))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutMultipleInheritance))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutScope))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutModules))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutPackages))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutClassAttributes))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutAttributeAccess))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutDeletingObjects))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutProxyObjectProject))
    original_suite.addTests(loader.loadTestsFromTestCase(TelevisionTest))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutExtraCredit))
    original_suite.addTests(loader.loadTestsFromTestCase(AboutRegex))
    return original_suite


class TestPathToEnlightenment(unittest.TestCase):

    def test_koans_kjc_should_equal_koans_orig(self):
        'TEMPORARY:  New loader should load the same tests as the original.'
        # FIXME:  Find a better way to test this.
        expected = list(original_test_suite())
        received = list(pte.koans())
        self.assertListEqual(expected, received)
        return


class TestFilterKoanNames(unittest.TestCase):

    def test_empty_input_produces_empty_output(self):
        infile = io.StringIO(u'')
        expected = []
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def test_names_yielded_match_names_in_file(self):
        names = [
          u'this.is.a.test',
          u'this.is.only.a.test',
          ]
        infile = io.StringIO(u'\n'.join(names))
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(names, received)
        return

    def test_whitespace_is_stripped(self):
        names = [
          u'this.is.a.test',
          u'    white.space.should.be.stripped',
          u'this.is.only.a.test',
          u'white.space.should.be.stripped    ',
          ]
        infile = io.StringIO(u'\n'.join(names))
        expected = [
          u'this.is.a.test',
          u'white.space.should.be.stripped',
          u'this.is.only.a.test',
          u'white.space.should.be.stripped',
          ]
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def test_commented_out_names_are_excluded(self):
        names = [
          u'this.is.a.test',
          u'#this.is.a.comment',
          u'this.is.only.a.test',
          u'    #    this.is.also a.comment    ',
          ]
        infile = io.StringIO(u'\n'.join(names))
        expected = [
          u'this.is.a.test',
          u'this.is.only.a.test',
          ]
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def all_blank_or_comment_lines_produce_empty_output(self):
        names = [
          u' ',
          u'# This is a comment.',
          u'\t',
          u'    # This is also a comment.',
          ]
        infile = io.StringIO(u'\n'.join(names))
        expected = []
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return


class TestKoansSuite(unittest.TestCase):

    def test_empty_input_produces_empty_testsuite(self):
        names = []
        suite = pte.koans_suite(names)
        self.assertIsInstance(suite, unittest.TestSuite)
        expected = []
        received = list(suite)
        self.assertListEqual(expected, received)
        return

    def test_testcase_names_appear_in_testsuite(self):
        names = [
          'koans.about_asserts.AboutAsserts',
          'koans.about_none.AboutNone',
          'koans.about_strings.AboutStrings',
          ]
        suite = pte.koans_suite(names)
        self.assertIsInstance(suite, unittest.TestSuite)
        expected = [
          'AboutAsserts',
          'AboutNone',
          'AboutStrings',
          ]
        received = sorted(set(test.__class__.__name__ for test in suite))
        self.assertListEqual(expected, received)
        return
