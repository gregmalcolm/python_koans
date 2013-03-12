#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from runner import helper

class TestHelper(unittest.TestCase):

    def test_that_get_class_name_works_with_a_string_instance(self):
        self.assertEqual("str", helper.cls_name(str()))

    def test_that_get_class_name_works_with_a_4(self):
        self.assertEquals("int", helper.cls_name(4))

    def test_that_get_class_name_works_with_a_tuple(self):
        self.assertEquals("tuple", helper.cls_name((3,"pie", [])))
