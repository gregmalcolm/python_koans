#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from runner.runner_tests.test_mountain import TestMountain
from runner.runner_tests.test_sensei import TestSensei
from runner.runner_tests.test_helper import TestHelper

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMountain))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSensei))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHelper))
    return suite

if __name__ == '__main__':
    res = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(not res.wasSuccessful())
