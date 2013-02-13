#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """
        self.assertTrue(True)  # This should be true

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        self.assertTrue(True, "This should be true -- Please fix this")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(2, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against
        reality.
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Knowing how things really work is half the battle
        """

        # This throws an AssertionError exception
        assert True
