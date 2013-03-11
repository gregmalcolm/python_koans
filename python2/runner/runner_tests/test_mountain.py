#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from libs.mock import *

from runner.mountain import Mountain
from runner import path_to_enlightenment

class TestMountain(unittest.TestCase):

    def setUp(self):
        path_to_enlightenment.koans = Mock()
        self.mountain = Mountain()
        self.mountain.stream.writeln = Mock()

    def test_it_gets_test_results(self):
        self.mountain.lesson.learn = Mock()
        self.mountain.walk_the_path()
        self.assertTrue(self.mountain.lesson.learn.called)

