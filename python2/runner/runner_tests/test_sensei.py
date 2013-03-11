#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
import re

from libs.mock import *

from runner.sensei import Sensei
from runner.writeln_decorator import WritelnDecorator
from runner.mockable_test_result import MockableTestResult
from runner import path_to_enlightenment

class AboutParrots:
    pass
class AboutLumberjacks:
    pass
class AboutTennis:
    pass
class AboutTheKnightsWhoSayNi:
    pass
class AboutMrGumby:
    pass
class AboutMessiahs:
    pass
class AboutGiantFeet:
    pass
class AboutTrebuchets:
    pass
class AboutFreemasons:
    pass

error_assertion_with_message = """Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_exploding_trousers.py", line 43, in test_durability
    self.assertEqual("Steel","Lard", "Another fine mess you've got me into Stanley...")
AssertionError: Another fine mess you've got me into Stanley..."""

error_assertion_equals = """

Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_exploding_trousers.py", line 49, in test_math
    self.assertEqual(4,99)
AssertionError: 4 != 99
"""

error_assertion_true = """Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_armories.py", line 25, in test_weoponary
    self.assertTrue("Pen" > "Sword")
AssertionError

"""

error_mess = """
Traceback (most recent call last):
  File "contemplate_koans.py", line 5, in <module>
    from runner.mountain import Mountain
  File "/Users/Greg/hg/python_koans/runner/mountain.py", line 7, in <module>
    import path_to_enlightenment
  File "/Users/Greg/hg/python_koans/runner/path_to_enlightenment.py", line 8, in <module>
    from koans import *
  File "/Users/Greg/hg/python_koans/koans/about_asserts.py", line 20
    self.assertTrue(eoe"Pen" > "Sword", "nhnth")
                           ^
SyntaxError: invalid syntax"""

error_with_list = """Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_armories.py", line 84, in test_weoponary
    self.assertEqual([1, 9], [1, 2])
AssertionError: Lists differ: [1, 9] != [1, 2]

First differing element 1:
9
2

- [1, 9]
?     ^

+ [1, 2]
?     ^

"""

class TestSensei(unittest.TestCase):

    def setUp(self):
        self.sensei = Sensei(WritelnDecorator(sys.stdout))
        self.sensei.stream.writeln = Mock()
        path_to_enlightenment.koans = Mock()
        self.tests = Mock()
        self.tests.countTestCases = Mock()

    def test_that_it_delegates_testing_to_test_cases(self):
        MockableTestResult.startTest = Mock()
        self.sensei.startTest(Mock())
        self.assertTrue(MockableTestResult.startTest.called)

    def test_that_user_is_notified_if_test_involves_a_different_test_class_to_last_time(self):
        MockableTestResult.startTest = Mock()

        self.sensei.prevTestClassName == 'AboutLumberjacks'
        nextTest = AboutParrots()

        self.sensei.startTest(nextTest)
        self.assertTrue(self.sensei.stream.writeln.called)

    def test_that_user_is_not_notified_about_test_class_repeats(self):
        MockableTestResult.startTest = Mock()

        self.sensei.prevTestClassName == 'AboutParrots'
        nextTest = AboutParrots()

        self.sensei.startTest(nextTest)
        self.assertTrue(self.sensei.stream.writeln.called)

    def test_that_cached_classname_updates_after_the_test(self):
        self.assertEqual(None, self.sensei.prevTestClassName)
        self.sensei.startTest(Mock())
        self.assertNotEqual(None, self.sensei.prevTestClassName)

    def test_that_errors_are_diverted_to_the_failures_list(self):
        MockableTestResult.addFailure = Mock()
        self.sensei.addError(Mock(), Mock())
        self.assertTrue(MockableTestResult.addFailure.called)

    def test_that_failures_are_handled_in_the_base_class(self):
        MockableTestResult.addFailure = Mock()
        self.sensei.addFailure(Mock(), Mock())
        self.assertTrue(MockableTestResult.addFailure.called)

    def test_that_it_successes_only_count_if_passes_are_currently_allowed(self):
        self.sensei.passesCount = Mock()
        MockableTestResult.addSuccess = Mock()
        self.sensei.addSuccess(Mock())
        self.assertTrue(self.sensei.passesCount.called)

    def test_that_if_there_are_failures_and_the_prev_class_is_different_successes_are_not_allowed(self):
        self.sensei.failures = [(AboutLumberjacks(), Mock())]
        self.sensei.prevTestClassName = "AboutTheMinitry"
        self.assertFalse(self.sensei.passesCount())

    def test_that_if_there_are_failures_and_the_prev_class_is_the_same_successes_are_allowed(self):
        self.sensei.failures = [(AboutLumberjacks(), Mock())]
        self.sensei.prevTestClassName = "AboutLumberjacks"
        self.assertTrue(self.sensei.passesCount())

    def test_that_if_there_are_no_failures_successes_are_allowed(self):
        self.sensei.failures = None
        self.sensei.prevTestClassName = "AboutLumberjacks"
        self.assertTrue(self.sensei.passesCount())

    def test_that_it_passes_on_add_successes_message(self):
        MockableTestResult.addSuccess = Mock()
        self.sensei.addSuccess(Mock())
        self.assertTrue(MockableTestResult.addSuccess.called)

    def test_that_it_increases_the_passes_on_every_success(self):
        pass_count = self.sensei.pass_count
        MockableTestResult.addSuccess = Mock()
        self.sensei.addSuccess(Mock())
        self.assertEqual(pass_count + 1, self.sensei.pass_count)

    def test_that_it_displays_each_success(self):
        MockableTestResult.addSuccess = Mock()
        self.sensei.addSuccess(Mock())
        self.assertTrue(self.sensei.stream.writeln.called)

    def test_that_nothing_is_returned_as_a_first_result_if_there_are_no_failures(self):
        self.sensei.failures = []
        self.assertEqual(None, self.sensei.firstFailure())

    def test_that_nothing_is_returned_as_sorted_result_if_there_are_no_failures(self):
        self.sensei.failures = []
        self.assertEqual(None, self.sensei.sortFailures("AboutLife"))

    def test_that_nothing_is_returned_as_sorted_result_if_there_are_no_relevent_failures(self):
        self.sensei.failures = [
            (AboutTheKnightsWhoSayNi(),"File 'about_the_knights_whn_say_ni.py', line 24"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 43"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 844")
        ]
        self.assertEqual(None, self.sensei.sortFailures("AboutLife"))

    def test_that_nothing_is_returned_as_sorted_result_if_there_are_3_shuffled_results(self):
        self.sensei.failures = [
            (AboutTennis(),"File 'about_tennis.py', line 299"),
            (AboutTheKnightsWhoSayNi(),"File 'about_the_knights_whn_say_ni.py', line 24"),
            (AboutTennis(),"File 'about_tennis.py', line 30"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 43"),
            (AboutTennis(),"File 'about_tennis.py', line 2"),
            (AboutMrGumby(),"File 'about_mr_gumby.py', line odd"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 844")
        ]

        expected = [
            (AboutTennis(),"File 'about_tennis.py', line 2"),
            (AboutTennis(),"File 'about_tennis.py', line 30"),
            (AboutTennis(),"File 'about_tennis.py', line 299")
        ]

        results = self.sensei.sortFailures("AboutTennis")
        self.assertEqual(3, len(results))
        self.assertEqual(2, results[0][0])
        self.assertEqual(30, results[1][0])
        self.assertEqual(299, results[2][0])

    def test_that_it_will_choose_not_find_anything_with_non_standard_error_trace_string(self):
        self.sensei.failures = [
            (AboutMrGumby(),"File 'about_mr_gumby.py', line MISSING"),
        ]
        self.assertEqual(None, self.sensei.sortFailures("AboutMrGumby"))


    def test_that_it_will_choose_correct_first_result_with_lines_9_and_27(self):
        self.sensei.failures = [
            (AboutTrebuchets(),"File 'about_trebuchets.py', line 27"),
            (AboutTrebuchets(),"File 'about_trebuchets.py', line 9"),
            (AboutTrebuchets(),"File 'about_trebuchets.py', line 73v")
        ]
        self.assertEqual("File 'about_trebuchets.py', line 9", self.sensei.firstFailure()[1])

    def test_that_it_will_choose_correct_first_result_with_multiline_test_classes(self):
        self.sensei.failures = [
            (AboutGiantFeet(),"File 'about_giant_feet.py', line 999"),
            (AboutGiantFeet(),"File 'about_giant_feet.py', line 44"),
            (AboutFreemasons(),"File 'about_freemasons.py', line 1"),
            (AboutFreemasons(),"File 'about_freemasons.py', line 11")
        ]
        self.assertEqual("File 'about_giant_feet.py', line 44", self.sensei.firstFailure()[1])

    def test_that_end_report_displays_something(self):
        self.sensei.learn()
        self.assertTrue(self.sensei.stream.writeln.called)

    def test_that_end_report_shows_student_progress(self):
        self.sensei.errorReport = Mock()
        self.sensei.total_lessons = Mock()
        self.sensei.total_koans = Mock()

        self.sensei.learn()
        self.assertTrue(self.sensei.total_lessons.called)
        self.assertTrue(self.sensei.total_koans.called)

    def test_that_end_report_shows_the_failure_report(self):
        self.sensei.errorReport = Mock()
        self.sensei.learn()
        self.assertTrue(self.sensei.errorReport.called)

    def test_that_end_report_should_have_something_zenlike_on_it(self):
        self.sensei.say_something_zenlike = Mock()
        self.sensei.learn()
        self.assertTrue(self.sensei.say_something_zenlike.called)

    def test_that_error_report_shows_something_if_there_is_a_failure(self):
        self.sensei.firstFailure = Mock()
        self.sensei.firstFailure.return_value = (Mock(), "FAILED Parrot is breathing, Line 42")
        self.sensei.errorReport()
        self.assertTrue(self.sensei.stream.writeln.called)

    def test_that_error_report_does_not_show_anything_if_there_is_no_failure(self):
        self.sensei.firstFailure = Mock()
        self.sensei.firstFailure.return_value = None
        self.sensei.errorReport()
        self.assertFalse(self.sensei.stream.writeln.called)

    def test_that_error_report_features_the_assertion_error(self):
        self.sensei.scrapeAssertionError = Mock()
        self.sensei.firstFailure = Mock()
        self.sensei.firstFailure.return_value = (Mock(), "FAILED")
        self.sensei.errorReport()
        self.assertTrue(self.sensei.scrapeAssertionError.called)

    def test_that_error_report_features_a_stack_dump(self):
        self.sensei.scrapeInterestingStackDump = Mock()
        self.sensei.firstFailure = Mock()
        self.sensei.firstFailure.return_value = (Mock(), "FAILED")
        self.sensei.errorReport()
        self.assertTrue(self.sensei.scrapeInterestingStackDump.called)

    def test_that_scraping_the_assertion_error_with_nothing_gives_you_a_blank_back(self):
        self.assertEqual("", self.sensei.scrapeAssertionError(None))

    def test_that_scraping_the_assertion_error_with_messaged_assert(self):
        self.assertEqual("  AssertionError: Another fine mess you've got me into Stanley...",
            self.sensei.scrapeAssertionError(error_assertion_with_message))

    def test_that_scraping_the_assertion_error_with_assert_equals(self):
        self.assertEqual("  AssertionError: 4 != 99",
            self.sensei.scrapeAssertionError(error_assertion_equals))

    def test_that_scraping_the_assertion_error_with_assert_true(self):
        self.assertEqual("  AssertionError",
            self.sensei.scrapeAssertionError(error_assertion_true))

    def test_that_scraping_the_assertion_error_with_syntax_error(self):
        self.assertEqual("  SyntaxError: invalid syntax",
            self.sensei.scrapeAssertionError(error_mess))

    def test_that_scraping_the_assertion_error_with_list_error(self):
        self.assertEqual("""  AssertionError: Lists differ: [1, 9] != [1, 2]

  First differing element 1:
  9
  2

  - [1, 9]
  ?     ^

  + [1, 2]
  ?     ^""",
            self.sensei.scrapeAssertionError(error_with_list))

    def test_that_scraping_a_non_existent_stack_dump_gives_you_nothing(self):
        self.assertEqual("", self.sensei.scrapeInterestingStackDump(None))

    def test_that_scraping_the_stack_dump_only_shows_interesting_lines_for_messaged_assert(self):
        expected = """  File "/Users/Greg/hg/python_koans/koans/about_exploding_trousers.py", line 43, in test_durability
    self.assertEqual("Steel","Lard", "Another fine mess you've got me into Stanley...")"""
        self.assertEqual(expected,
            self.sensei.scrapeInterestingStackDump(error_assertion_with_message))

    def test_that_scraping_the_stack_dump_only_shows_interesting_lines_for_assert_equals(self):
        expected = """  File "/Users/Greg/hg/python_koans/koans/about_exploding_trousers.py", line 49, in test_math
    self.assertEqual(4,99)"""
        self.assertEqual(expected,
            self.sensei.scrapeInterestingStackDump(error_assertion_equals))

    def test_that_scraping_the_stack_dump_only_shows_interesting_lines_for_assert_true(self):
        expected = """  File "/Users/Greg/hg/python_koans/koans/about_armories.py", line 25, in test_weoponary
    self.assertTrue("Pen" > "Sword")"""
        self.assertEqual(expected,
            self.sensei.scrapeInterestingStackDump(error_assertion_true))

    def test_that_scraping_the_stack_dump_only_shows_interesting_lines_for_syntax_error(self):
        expected = """  File "/Users/Greg/hg/python_koans/koans/about_asserts.py", line 20
    self.assertTrue(eoe"Pen" > "Sword", "nhnth")"""
        self.assertEqual(expected,
            self.sensei.scrapeInterestingStackDump(error_mess))

    def test_that_if_there_are_no_failures_say_the_final_zenlike_remark(self):
        self.sensei.failures = None
        words = self.sensei.say_something_zenlike()

        m = re.search("Spanish Inquisition", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_are_0_successes_it_will_say_the_first_zen_of_python_koans(self):
        self.sensei.pass_count = 0
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()

        m = re.search("Beautiful is better than ugly", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_is_1_successes_it_will_say_the_second_zen_of_python_koans(self):
        self.sensei.pass_count = 1
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()

        m = re.search("Explicit is better than implicit", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_is_10_successes_it_will_say_the_sixth_zen_of_python_koans(self):
        self.sensei.pass_count = 10
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()

        m = re.search("Sparse is better than dense", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_is_36_successes_it_will_say_the_final_zen_of_python_koans(self):
        self.sensei.pass_count = 36
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()

        m = re.search("Namespaces are one honking great idea", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_is_37_successes_it_will_say_the_first_zen_of_python_koans_again(self):
        self.sensei.pass_count = 37
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()

        m = re.search("Beautiful is better than ugly", words)
        self.assertTrue(m and m.group(0))

    def test_that_total_lessons_return_7_if_there_are_7_lessons(self):
        self.sensei.filter_all_lessons = Mock()
        self.sensei.filter_all_lessons.return_value = [1,2,3,4,5,6,7]

        self.assertEqual(7, self.sensei.total_lessons())

    def test_that_total_lessons_return_0_if_all_lessons_is_none(self):
        self.sensei.filter_all_lessons = Mock()
        self.sensei.filter_all_lessons.return_value = None

        self.assertEqual(0, self.sensei.total_lessons())

    def test_total_koans_return_43_if_there_are_43_test_cases(self):
        self.sensei.tests.countTestCases = Mock()
        self.sensei.tests.countTestCases.return_value = 43

        self.assertEqual(43, self.sensei.total_koans())

    def test_filter_all_lessons_will_discover_test_classes_if_none_have_been_discovered_yet(self):
        self.sensei.all_lessons = 0
        self.assertTrue(len(self.sensei.filter_all_lessons()) > 10)
        self.assertTrue(len(self.sensei.all_lessons) > 10)
