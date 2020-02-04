#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AboutClassAttributes(Koan):
    class Dog:
        pass

    def test_objects_are_objects(self):
        fido = self.Dog()
        self.assertEqual(True, isinstance(fido, object))

    def test_classes_are_types(self):
        self.assertEqual(True, self.Dog.__class__ == type)

    def test_classes_are_objects_too(self):
        self.assertEqual(True, issubclass(self.Dog, object))

    def test_objects_have_methods(self):
        fido = self.Dog()
        self.assertEqual(26, len(dir(fido)))

    def test_classes_have_methods(self):
        self.assertEqual(26, len(dir(self.Dog)))

    def test_creating_objects_without_defining_a_class(self):
        singularity = object()
        self.assertEqual(23, len(dir(singularity)))

    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4

        self.assertEqual(4, fido.legs)

    def test_defining_functions_on_individual_objects(self):
        fido = self.Dog()
        fido.wag = lambda : 'fidos wag'

        self.assertEqual('fidos wag', fido.wag())

    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        rover = self.Dog()

        def wag():
            return 'fidos wag'
        fido.wag = wag

        with self.assertRaises(AttributeError): rover.wag()

    # ------------------------------------------------------------------

    class Dog2:
        def wag(self):
            return 'instance wag'

        def bark(self):
            return "instance bark"

        def growl(self):
            return "instance growl"

        @staticmethod
        def bark():
            return "staticmethod bark, arg: None"

        @classmethod
        def growl(cls):
            return "classmethod growl, arg: cls=" + cls.__name__

    def test_since_classes_are_objects_you_can_define_singleton_methods_on_them_too(self):
        self.assertRegex(self.Dog2.growl(), 'classmethod growl, arg: cls=Dog2')

    def test_classmethods_are_not_independent_of_instance_methods(self):
        fido = self.Dog2()
        self.assertRegex(fido.growl(), 'classmethod growl, arg: cls=Dog2')
        self.assertRegex(self.Dog2.growl(), 'classmethod growl, arg: cls=Dog2')

    def test_staticmethods_are_unbound_functions_housed_in_a_class(self):
        self.assertRegex(self.Dog2.bark(), 'staticmethod bark, arg: None')

    def test_staticmethods_also_overshadow_instance_methods(self):
        fido = self.Dog2()
        self.assertRegex(fido.bark(), 'staticmethod bark, arg: None')

    # ------------------------------------------------------------------

    class Dog3:
        def __init__(self):
            self._name = None

        def get_name_from_instance(self):
            return self._name

        def set_name_from_instance(self, name):
            self._name = name

        @classmethod
        def get_name(cls):
            return cls._name

        @classmethod
        def set_name(cls, name):
            cls._name = name

        name = property(get_name, set_name)
        name_from_instance = property(get_name_from_instance, set_name_from_instance)

    def test_classmethods_can_not_be_used_as_properties(self):
        fido = self.Dog3()
        with self.assertRaises(TypeError): fido.name = "Fido"

    def test_classes_and_instances_do_not_share_instance_attributes(self):
        fido = self.Dog3()
        fido.set_name_from_instance("Fido")
        fido.set_name("Rover")
        self.assertEqual('Fido', fido.get_name_from_instance())
        self.assertEqual('Rover', self.Dog3.get_name())

    def test_classes_and_instances_do_share_class_attributes(self):
        fido = self.Dog3()
        fido.set_name("Fido")
        self.assertEqual('Fido', fido.get_name())
        self.assertEqual('Fido', self.Dog3.get_name())

    # ------------------------------------------------------------------

    class Dog4:
        def a_class_method(cls):
            return 'dogs class method'

        def a_static_method():
            return 'dogs static method'

        a_class_method = classmethod(a_class_method)
        a_static_method = staticmethod(a_static_method)

    def test_you_can_define_class_methods_without_using_a_decorator(self):
        self.assertEqual('dogs class method', self.Dog4.a_class_method())

    def test_you_can_define_static_methods_without_using_a_decorator(self):
        self.assertEqual('dogs static method', self.Dog4.a_static_method())

    # ------------------------------------------------------------------

    def test_heres_an_easy_way_to_explicitly_call_class_methods_from_instance_methods(self):
        fido = self.Dog4()
        self.assertEqual('dogs class method', fido.__class__.a_class_method())
