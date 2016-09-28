#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enlightenment starts with the following:

import importlib
import io
import unittest


def module_name_and_class_name(full_name):
    full_name = full_name.strip()
    module_name, class_name = full_name.rsplit('.', 1)
    return module_name, class_name


def koan_names(filename):
    with io.open(filename, 'rt', encoding='utf8') as f:
        for full_name in f:
            yield module_name_and_class_name(full_name)


def import_koan(module_name, class_name):
    module = importlib.import_module(module_name)
    testcase = getattr(module, class_name)
    return testcase


def koans(filename='koans.txt'):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    for module_name, class_name in koan_names(filename):
        koan = import_koan(module_name, class_name)
        suite.addTests(loader.loadTestsFromTestCase(koan))
    return suite
