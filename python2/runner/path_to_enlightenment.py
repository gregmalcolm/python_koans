#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enlightenment starts with the following:

import unittest

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

def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(AboutAsserts))
    suite.addTests(loader.loadTestsFromTestCase(AboutStrings))
    suite.addTests(loader.loadTestsFromTestCase(AboutNone))
    suite.addTests(loader.loadTestsFromTestCase(AboutLists))
    suite.addTests(loader.loadTestsFromTestCase(AboutListAssignments))
    suite.addTests(loader.loadTestsFromTestCase(AboutDictionaries))
    suite.addTests(loader.loadTestsFromTestCase(AboutStringManipulation))
    suite.addTests(loader.loadTestsFromTestCase(AboutTuples))
    suite.addTests(loader.loadTestsFromTestCase(AboutMethods))
    suite.addTests(loader.loadTestsFromTestCase(AboutControlStatements))
    suite.addTests(loader.loadTestsFromTestCase(AboutTrueAndFalse))
    suite.addTests(loader.loadTestsFromTestCase(AboutSets))
    suite.addTests(loader.loadTestsFromTestCase(AboutTriangleProject))
    suite.addTests(loader.loadTestsFromTestCase(AboutExceptions))
    suite.addTests(loader.loadTestsFromTestCase(AboutTriangleProject2))
    suite.addTests(loader.loadTestsFromTestCase(AboutIteration))
    suite.addTests(loader.loadTestsFromTestCase(AboutComprehension))
    suite.addTests(loader.loadTestsFromTestCase(AboutGenerators))
    suite.addTests(loader.loadTestsFromTestCase(AboutLambdas))
    suite.addTests(loader.loadTestsFromTestCase(AboutScoringProject))
    suite.addTests(loader.loadTestsFromTestCase(AboutClasses))
    suite.addTests(loader.loadTestsFromTestCase(AboutNewStyleClasses))
    suite.addTests(loader.loadTestsFromTestCase(AboutWithStatements))
    suite.addTests(loader.loadTestsFromTestCase(AboutMonkeyPatching))
    suite.addTests(loader.loadTestsFromTestCase(AboutDiceProject))
    suite.addTests(loader.loadTestsFromTestCase(AboutMethodBindings))
    suite.addTests(loader.loadTestsFromTestCase(AboutDecoratingWithFunctions))
    suite.addTests(loader.loadTestsFromTestCase(AboutDecoratingWithClasses))
    suite.addTests(loader.loadTestsFromTestCase(AboutInheritance))
    suite.addTests(loader.loadTestsFromTestCase(AboutMultipleInheritance))
    suite.addTests(loader.loadTestsFromTestCase(AboutScope))
    suite.addTests(loader.loadTestsFromTestCase(AboutModules))
    suite.addTests(loader.loadTestsFromTestCase(AboutPackages))
    suite.addTests(loader.loadTestsFromTestCase(AboutClassAttributes))
    suite.addTests(loader.loadTestsFromTestCase(AboutAttributeAccess))
    suite.addTests(loader.loadTestsFromTestCase(AboutDeletingObjects))
    suite.addTests(loader.loadTestsFromTestCase(AboutProxyObjectProject))
    suite.addTests(loader.loadTestsFromTestCase(TelevisionTest))
    suite.addTests(loader.loadTestsFromTestCase(AboutExtraCredit))

    return suite
