#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutNewStyleClasses(Koan):
    class OldStyleClass:
        "An old style class"
        # Original class style have been phased out in Python 3.
        
    class NewStyleClass(object):
        "A new style class"
        # Introduced in Python 2.2
        #
        # Aside from this set of tests, Python Koans sticks exclusively to this
        # kind of class
        pass

    def test_new_style_classes_inherit_from_object_base_class(self):
        self.assertEqual(____, issubclass(self.NewStyleClass, object))
        self.assertEqual(____, issubclass(self.OldStyleClass, object))
        
    def test_new_style_classes_have_more_attributes(self):
        self.assertEqual(__, len(dir(self.OldStyleClass)))
        self.assertEqual(__, self.OldStyleClass.__doc__)
        self.assertEqual(__, self.OldStyleClass.__module__)
    
        self.assertEqual(__, len(dir(self.NewStyleClass)))
        # To examine the available attributes, run 'dir(<Class name goes here>)'
        # from a python console

    # ------------------------------------------------------------------

    def test_old_style_classes_have_type_but_no_class_attribute(self):
        self.assertEqual(__, type(self.OldStyleClass).__name__)
        
        try:
            cls = self.OldStyleClass.__class__
        except Exception as ex:
            pass
        
        self.assertMatch(__, ex[0])
    
    def test_new_style_classes_have_same_class_as_type(self):
        new_style = self.NewStyleClass()
        self.assertEqual(__, type(self.NewStyleClass).__name__)
        self.assertEqual(__, type(self.NewStyleClass) == self.NewStyleClass.__class__)
        
    # ------------------------------------------------------------------
        
    def test_in_old_style_instances_class_is_different_to_type(self):
        old_style = self.OldStyleClass()
        self.assertEqual(__, type(old_style).__name__)
        self.assertEqual(__, old_style.__class__.__name__)

    def test_new_style_instances_have_same_class_as_type(self):
        new_style = self.NewStyleClass()
        self.assertEqual(__, type(new_style).__name__)
        self.assertEqual(__, type(new_style) == new_style.__class__)
