#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

def function():
    return "pineapple"

def function2():
    return "tractor"

class Class:
    def method(self):
        return "parrot"

class AboutMethodBindings(Koan):
    def test_methods_are_bound_to_an_object(self):
        obj = Class()
        self.assertEqual(__, obj.method.__self__ == obj)

    def test_methods_are_also_bound_to_a_function(self):
        obj = Class()
        self.assertEqual(__, obj.method())
        self.assertEqual(__, obj.method.__func__(obj))

    def test_functions_have_attributes(self):
        obj = Class()
        self.assertEqual(__, len(dir(function)))
        self.assertEqual(__, dir(function) == dir(obj.method.__func__))

    def test_methods_have_different_attributes(self):
        obj = Class()
        self.assertEqual(__, len(dir(obj.method)))

    def test_setting_attributes_on_an_unbound_function(self):
        function.cherries = 3
        self.assertEqual(__, function.cherries)

    def test_setting_attributes_on_a_bound_method_directly(self):
        obj = Class()
        with self.assertRaises(___): obj.method.cherries = 3

    def test_setting_attributes_on_methods_by_accessing_the_inner_function(self):
        obj = Class()
        obj.method.__func__.cherries = 3
        self.assertEqual(__, obj.method.cherries)

    def test_functions_can_have_inner_functions(self):
        function2.get_fruit = function
        self.assertEqual(__, function2.get_fruit())

    def test_inner_functions_are_unbound(self):
        function2.get_fruit = function
        with self.assertRaises(___): cls = function2.get_fruit.__self__

    # ------------------------------------------------------------------

    class BoundClass:
        def __get__(self, obj, cls):
            return (self, obj, cls)

    binding = BoundClass()

    def test_get_descriptor_resolves_attribute_binding(self):
        bound_obj, binding_owner, owner_type = self.binding
        # Look at BoundClass.__get__():
        #   bound_obj = self
        #   binding_owner = obj
        #   owner_type = cls

        self.assertEqual(__, bound_obj.__class__.__name__)
        self.assertEqual(__, binding_owner.__class__.__name__)
        self.assertEqual(AboutMethodBindings, owner_type)

    # ------------------------------------------------------------------

    class SuperColor:
        def __init__(self):
            self.choice = None

        def __set__(self, obj, val):
            self.choice = val

    color = SuperColor()

    def test_set_descriptor_changes_behavior_of_attribute_assignment(self):
        self.assertEqual(None, self.color.choice)
        self.color = 'purple'
        self.assertEqual(__, self.color.choice)

