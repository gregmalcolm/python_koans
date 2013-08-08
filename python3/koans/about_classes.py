#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutClasses(Koan):
    class Dog:
        "Dogs need regular walkies. Never, ever let them drive."

    def test_instances_of_classes_can_be_created_adding_parentheses(self):
        # NOTE: The .__name__ attribute will convert the class
        # into a string value.
        fido = self.Dog()
        self.assertEqual(__, fido.__class__.__name__)

    def test_classes_have_docstrings(self):
        self.assertRegexpMatches(self.Dog.__doc__, __)

    # ------------------------------------------------------------------

    class Dog2:
        def __init__(self):
            self._name = 'Paul'

        def set_name(self, a_name):
            self._name = a_name

    def test_init_method_is_the_constructor(self):
        dog = self.Dog2()
        self.assertEqual(__, dog._name)

    def test_private_attributes_are_not_really_private(self):
        dog = self.Dog2()
        dog.set_name("Fido")
        self.assertEqual(__, dog._name)
        # The _ prefix in _name implies private ownership, but nothing is truly
        # private in Python.

    def test_you_can_also_access_the_value_out_using_getattr_and_dict(self):
        fido = self.Dog2()
        fido.set_name("Fido")

        self.assertEqual(__, getattr(fido, "_name"))
        # getattr(), setattr() and delattr() are a way of accessing attributes
        # by method rather than through assignment operators

        self.assertEqual(__, fido.__dict__["_name"])
        # Yes, this works here, but don't rely on the __dict__ object! Some
        # class implementations use optimization which result in __dict__ not
        # showing everything.

    # ------------------------------------------------------------------

    class Dog3:
        def __init__(self):
            self._name = None

        def set_name(self, a_name):
            self._name = a_name

        def get_name(self):
            return self._name

        name = property(get_name, set_name)

    def test_that_name_can_be_read_as_a_property(self):
        fido = self.Dog3()
        fido.set_name("Fido")

        # access as method
        self.assertEqual(__, fido.get_name())

        # access as property
        self.assertEqual(__, fido.name)

    # ------------------------------------------------------------------

    class Dog4:
        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, a_name):
            self._name = a_name

    def test_creating_properties_with_decorators_is_slightly_easier(self):
        fido = self.Dog4()

        fido.name = "Fido"
        self.assertEqual(__, fido.name)

    # ------------------------------------------------------------------

    class Dog5:
        def __init__(self, initial_name):
            self._name = initial_name

        @property
        def name(self):
            return self._name

    def test_init_provides_initial_values_for_instance_variables(self):
        fido = self.Dog5("Fido")
        self.assertEqual(__, fido.name)

    def test_args_must_match_init(self):
        with self.assertRaises(___):
            self.Dog5()

        # THINK ABOUT IT:
        # Why is this so?

    def test_different_objects_have_difference_instance_variables(self):
        fido = self.Dog5("Fido")
        rover = self.Dog5("Rover")

        self.assertEqual(__, rover.name == fido.name)

    # ------------------------------------------------------------------

    class Dog6:
        def __init__(self, initial_name):
            self._name = initial_name

        def get_self(self):
            return self

        def __str__(self):
            #
            # Implement this!
            #
            return __

        def __repr__(self):
            return "<Dog named '" + self._name + "'>"

    def test_inside_a_method_self_refers_to_the_containing_object(self):
        fido = self.Dog6("Fido")

        self.assertEqual(__, fido.get_self())  # Not a string!

    def test_str_provides_a_string_version_of_the_object(self):
        fido = self.Dog6("Fido")

        self.assertEqual("Fido", str(fido))

    def test_str_is_used_explicitly_in_string_interpolation(self):
        fido = self.Dog6("Fido")

        self.assertEqual(__, "My dog is " + str(fido))

    def test_repr_provides_a_more_complete_string_version(self):
        fido = self.Dog6("Fido")
        self.assertEqual(__, repr(fido))

    def test_all_objects_support_str_and_repr(self):
        seq = [1, 2, 3]

        self.assertEqual(__, str(seq))
        self.assertEqual(__, repr(seq))

        self.assertEqual(__, str("STRING"))
        self.assertEqual(__, repr("STRING"))
