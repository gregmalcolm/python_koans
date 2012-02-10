#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *


class AboutClassAttributes(Koan):
    class Dog(object):
        pass

    def test_new_style_class_objects_are_objects(self):
        # Note: Old style class instances are not objects but they are being
        # phased out it Python 3.

        fido = self.Dog()
        self.assertEqual(__, isinstance(fido, object))

    def test_classes_are_types(self):
        self.assertEqual(__, self.Dog.__class__ == type)

    def test_classes_are_objects_too(self):
        self.assertEqual(__, issubclass(self.Dog, object))

    def test_objects_have_methods(self):
        fido = self.Dog()
        self.assertEqual(__, len(dir(fido)))

    def test_classes_have_methods(self):
        self.assertEqual(__, len(dir(self.Dog)))

    def test_creating_objects_without_defining_a_class(self):
        singularity = object()
        self.assertEqual(__, len(dir(singularity)))

    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4

        self.assertEqual(__, fido.legs)

    def test_defining_functions_on_individual_objects(self):
        fido = self.Dog()
        fido.wag = lambda: 'fidos wag'

        self.assertEqual(__, fido.wag())

    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        rover = self.Dog()

        def wag():
            return 'fidos wag'
        fido.wag = wag

        try:
            rover.wag()
        except Exception as ex:
            self.assertMatch(__, ex[0])

    # ------------------------------------------------------------------

    class Dog2(object):
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

    def test_like_all_objects_classes_can_have_singleton_methods(self):
        self.assertMatch(__, self.Dog2.growl())

    def test_classmethods_are_not_independent_of_instance_methods(self):
        fido = self.Dog2()
        self.assertMatch(__, fido.growl())
        self.assertMatch(__, self.Dog2.growl())

    def test_staticmethods_are_unbound_functions_housed_in_a_class(self):
        self.assertMatch(__, self.Dog2.bark())

    def test_staticmethods_also_overshadow_instance_methods(self):
        fido = self.Dog2()
        self.assertMatch(__, fido.bark())

    # ------------------------------------------------------------------

    class Dog3(object):
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
        name_from_instance = property(
            get_name_from_instance, set_name_from_instance)

    def test_classmethods_can_not_be_used_as_properties(self):
        fido = self.Dog3()
        try:
            fido.name = "Fido"
        except Exception as ex:
            self.assertMatch(__, ex[0])

    def test_classes_and_instances_do_not_share_instance_attributes(self):
        fido = self.Dog3()
        fido.set_name_from_instance("Fido")
        fido.set_name("Rover")
        self.assertEqual(__, fido.get_name_from_instance())
        self.assertEqual(__, self.Dog3.get_name())

    def test_classes_and_instances_do_share_class_attributes(self):
        fido = self.Dog3()
        fido.set_name("Fido")
        self.assertEqual(__, fido.get_name())
        self.assertEqual(__, self.Dog3.get_name())

    # ------------------------------------------------------------------

    class Dog4(object):
        def a_class_method(cls):
            return 'dogs class method'

        def a_static_method():
            return 'dogs static method'

        a_class_method = classmethod(a_class_method)
        a_static_method = staticmethod(a_static_method)

    def test_you_can_define_class_methods_without_using_a_decorator(self):
        self.assertEqual(__, self.Dog4.a_class_method())

    def test_you_can_define_static_methods_without_using_a_decorator(self):
        self.assertEqual(__, self.Dog4.a_static_method())

    # ------------------------------------------------------------------

    def test_you_can_explicitly_call_class_methods_from_instance_methods(self):
        fido = self.Dog4()
        self.assertEqual(__, fido.__class__.a_class_method())
