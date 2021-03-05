#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import unittest

from runner import path_to_enlightenment as pte


class TestFilterKoanNames(unittest.TestCase):

    def test_empty_input_produces_empty_output(self):
        infile = io.StringIO('')
        expected = []
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def test_names_yielded_match_names_in_file(self):
        names = [
          'this.is.a.test',
          'this.is.only.a.test',
          ]
        infile = io.StringIO('\n'.join(names))
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(names, received)
        return

    def test_whitespace_is_stripped(self):
        names = [
          'this.is.a.test',
          '    white.space.should.be.stripped',
          'this.is.only.a.test',
          'white.space.should.be.stripped    ',
          ]
        infile = io.StringIO('\n'.join(names))
        expected = [
          'this.is.a.test',
          'white.space.should.be.stripped',
          'this.is.only.a.test',
          'white.space.should.be.stripped',
          ]
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def test_commented_out_names_are_excluded(self):
        names = [
          'this.is.a.test',
          '#this.is.a.comment',
          'this.is.only.a.test',
          '    #    this.is.also a.comment    ',
          ]
        infile = io.StringIO('\n'.join(names))
        expected = [
          'this.is.a.test',
          'this.is.only.a.test',
          ]
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def all_blank_or_comment_lines_produce_empty_output(self):
        names = [
          ' ',
          '# This is a comment.',
          '\t',
          '    # This is also a comment.',
          ]
        infile = io.StringIO('\n'.join(names))
        expected = []
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return


class TestKoansSuite(unittest.TestCase):

    def test_empty_input_produces_empty_testsuite(self):
        names = []
        suite = pte.koans_suite(names)
        self.assertTrue(isinstance(suite, unittest.TestSuite))
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
        self.assertTrue(isinstance(suite, unittest.TestSuite))
        expected = [
          'AboutAsserts',
          'AboutNone',
          'AboutStrings',
          ]
        received = sorted(set(test.__class__.__name__ for test in suite))
        self.assertListEqual(expected, received)
        return
