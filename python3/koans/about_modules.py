#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This is very different to AboutModules in Ruby Koans
# Our AboutMultipleInheritance class is a little more comparable
#

from runner.koan import *

from .another_local_module import *
from .local_module_with_all_defined import *


class AboutModules(Koan):
    def test_importing_other_python_scripts_as_modules(self):
        from . import local_module  # local_module.py

        duck = local_module.Duck()
        self.assertEqual(__, duck.name)

    def test_importing_attributes_from_classes_using_from_keyword(self):
        from .local_module import Duck

        duck = Duck()  # no module qualifier needed this time
        self.assertEqual(__, duck.name)

    def test_we_can_import_multiple_items_at_once(self):
        from . import jims, joes

        jims_dog = jims.Dog()
        joes_dog = joes.Dog()
        self.assertEqual(__, jims_dog.identify())
        self.assertEqual(__, joes_dog.identify())

    def test_importing_all_module_attributes_at_once(self):
        """
        importing all attributes at once is done like so:
            from .another_local_module import *
        The import wildcard cannot be used from within classes or functions.
        """

        goose = Goose()
        hamster = Hamster()

        self.assertEqual(__, goose.name)
        self.assertEqual(__, hamster.name)

    def test_modules_hide_attributes_prefixed_by_underscores(self):
        with self.assertRaises(___):
            private_squirrel = _SecretSquirrel()

    def test_private_attributes_are_still_accessible_in_modules(self):
        from .local_module import Duck  # local_module.py

        duck = Duck()
        self.assertEqual(__, duck._password)
        # module level attribute hiding doesn't affect class attributes
        # (unless the class itself is hidden).

    def test_a_module_can_limit_wildcard_imports(self):
        """
        Examine results of:
            from .local_module_with_all_defined import *
        """

        # 'Goat' is on the __all__ list
        goat = Goat()
        self.assertEqual(__, goat.name)

        # How about velociraptors?
        lizard = _Velociraptor()
        self.assertEqual(__, lizard.name)

        # SecretDuck? Never heard of her!
        with self.assertRaises(___):
            duck = SecretDuck()
