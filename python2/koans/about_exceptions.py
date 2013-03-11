#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutExceptions(Koan):

    class MySpecialError(RuntimeError):
        pass

    def test_exceptions_inherit_from_exception(self):
        mro = self.MySpecialError.__mro__
        self.assertEqual(__, mro[1].__name__)
        self.assertEqual(__, mro[2].__name__)
        self.assertEqual(__, mro[3].__name__)
        self.assertEqual(__, mro[4].__name__)

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except StandardError as ex:
            result = 'exception handled'

        self.assertEqual(__, result)

        self.assertEqual(____, isinstance(ex, StandardError))
        self.assertEqual(____, isinstance(ex, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, StandardError), \
            "RuntimeError is a subclass of StandardError")

        self.assertEqual(__, ex[0])

    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError, "My Message"
        except self.MySpecialError as ex:
            result = 'exception handled'

        self.assertEqual(__, result)
        self.assertEqual(__, ex[0])

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        self.assertEqual(__, result)

    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual(__, result)
