#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from libs.mock import *

from runner.mountain import Mountain

class TestMountain(unittest.TestCase):

    def setUp(self):
        self.mountain = Mountain()

    def test_it_gets_test_results(self):
        with patch_object(self.mountain.stream, 'writeln', Mock()):
            with patch_object(self.mountain.lesson, 'learn', Mock()):
                self.mountain.walk_the_path()
                self.assertTrue(self.mountain.lesson.learn.called)
