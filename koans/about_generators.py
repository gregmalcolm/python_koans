#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Written in place of AboutBlocks in the Ruby Koans
#
# Note: Both blocks and generators use a yield keyword, but they behave
# a lot differently
#

from runner.koan import *

class AboutGenerators(Koan):

    def test_generating_values_on_the_fly(self):
        result = list()
        bacon_generator = (n + ' bacon' for n in ['crunchy','veggie','danish'])

        for bacon in bacon_generator:
            result.append(bacon)

        self.assertEqual(__, result)

    def test_generators_are_different_to_list_comprehensions(self):
        num_list = [x*2 for x in range(1,3)]
        num_generator = (x*2 for x in range(1,3))

        self.assertEqual(2, num_list[0])

        # A generator has to be iterated through.
        with self.assertRaises(___): num = num_generator[0]

        self.assertEqual(__, list(num_generator)[0])

        # Both list comprehensions and generators can be iterated though. However, a generator
        # function is only called on the first iteration. The values are generated on the fly
        # instead of stored.
        #
        # Generators are more memory friendly, but less versatile

    def test_generator_expressions_are_a_one_shot_deal(self):
        dynamite = ('Boom!' for n in range(3))

        attempt1 = list(dynamite)
        attempt2 = list(dynamite)

        self.assertEqual(__, attempt1)
        self.assertEqual(__, attempt2)

    # ------------------------------------------------------------------

    def simple_generator_method(self):
        yield 'peanut'
        yield 'butter'
        yield 'and'
        yield 'jelly'

    def test_generator_method_will_yield_values_during_iteration(self):
        result = list()
        for item in self.simple_generator_method():
            result.append(item)
        self.assertEqual(__, result)

    def test_generators_can_be_manually_iterated_and_closed(self):
        result = self.simple_generator_method()
        self.assertEqual(__, next(result))
        self.assertEqual(__, next(result))
        result.close()

    # ------------------------------------------------------------------

    def square_me(self, seq):
        for x in seq:
            yield x * x

    def test_generator_method_with_parameter(self):
        result = self.square_me(range(2,5))
        self.assertEqual(__, list(result))

    # ------------------------------------------------------------------

    def sum_it(self, seq):
        value = 0
        for num in seq:
            # The local state of 'value' will be retained between iterations
            value += num
            yield value

    def test_generator_keeps_track_of_local_variables(self):
        result = self.sum_it(range(2,5))
        self.assertEqual(__, list(result))

    # ------------------------------------------------------------------

    def coroutine(self):
        result = yield
        yield result

    def test_generators_can_act_as_coroutines(self):
        generator = self.coroutine()

        # THINK ABOUT IT:
        # Why is this line necessary?
        #
        # Hint: Read the "Specification: Sending Values into Generators"
        #       section of http://www.python.org/dev/peps/pep-0342/
        next(generator)

        self.assertEqual(__, generator.send(1 + 2))

    def test_before_sending_a_value_to_a_generator_next_must_be_called(self):
        generator = self.coroutine()

        try:
            generator.send(1 + 2)
        except TypeError as ex:
            self.assertRegex(ex.args[0], __)

    # ------------------------------------------------------------------

    def yield_tester(self):
        value = yield
        if value:
            yield value
        else:
            yield 'no value'

    def test_generators_can_see_if_they_have_been_called_with_a_value(self):
        generator = self.yield_tester()
        next(generator)
        self.assertEqual('with value', generator.send('with value'))

        generator2 = self.yield_tester()
        next(generator2)
        self.assertEqual(__, next(generator2))

    def test_send_none_is_equivalent_to_next(self):
        generator = self.yield_tester()

        next(generator)
        # 'next(generator)' is exactly equivalent to 'generator.send(None)'
        self.assertEqual(__, generator.send(None))
