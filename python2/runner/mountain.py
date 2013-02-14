#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

import path_to_enlightenment
from sensei import Sensei
from writeln_decorator import WritelnDecorator

class Mountain:
    def __init__(self):
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)
    
    def walk_the_path(self, args=None):
        "Run the koans tests with a custom runner output."
        
        if args and len(args) >=2:
	    args.pop(0)
	    for arg in args:
            	self.tests = unittest.TestLoader().loadTestsFromName("koans." + arg)
        	self.tests(self.lesson)
        	self.lesson.learn()
        return self.lesson
