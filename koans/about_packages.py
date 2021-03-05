#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This is very different to AboutModules in Ruby Koans
# Our AboutMultipleInheritance class is a little more comparable
#

from runner.koan import *

#
# Package hierarchy of Python Koans project:
#
# contemplate_koans.py
# koans/
#     __init__.py
#     about_asserts.py
#     about_attribute_access.py
#     about_class_attributes.py
#     about_classes.py
#     ...
#     a_package_folder/
#         __init__.py
#         a_module.py

class AboutPackages(Koan):
    def test_subfolders_can_form_part_of_a_module_package(self):
        # Import ./a_package_folder/a_module.py
        from .a_package_folder.a_module import Duck

        duck = Duck()
        self.assertEqual(__, duck.name)

    def test_subfolders_become_modules_if_they_have_an_init_module(self):
        # Import ./a_package_folder/__init__.py
        from .a_package_folder import an_attribute

        self.assertEqual(__, an_attribute)

    # ------------------------------------------------------------------

    def test_use_absolute_imports_to_import_upper_level_modules(self):
        # Import /contemplate_koans.py
        import contemplate_koans

        self.assertEqual(__, contemplate_koans.__name__)

        # contemplate_koans.py is the root module in this package because it's
        # the first python module called in koans.
        #
        # If contemplate_koans.py was based in a_package_folder that would be
        # the root folder, which would make reaching the koans folder
        # almost impossible. So always leave the starting python script in
        # a folder which can reach everything else.

    def test_import_a_module_in_a_subfolder_folder_using_an_absolute_path(self):
        # Import contemplate_koans.py/koans/a_package_folder/a_module.py
        from koans.a_package_folder.a_module import Duck

        self.assertEqual(__, Duck.__module__)
