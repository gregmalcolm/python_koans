#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on https://www.dabeaz.com/coroutines/Coroutines.pdf
#

from runner.koan import *

# the global total
total = 0


class AboutCoroutines(Koan):
    class summerv0:
        def __init__(self, total=0):
            self.total = total

        def __call__(self, m=0):
            self.total += m
            return self.total

    def test_non_coroutines(self):
        # typical summmer is supposed to keep record of total
        # the total can be incremented by calling the function
        sum0 = self.summerv0()
        self.assertEqual(__, sum0(), "The initial value")
        self.assertEqual(__, sum0(10), "When you add 10")
        self.assertEqual(__, sum0(), "When you do not add anything")
        self.assertEqual(__, sum0(11), "When you add 11")
        self.assertEqual(__, sum0(), "When you do not add anything")

    def summerv1(self, total_init=0):
        global total
        total = total_init
        while True:
            z = yield
            total += z if z else 0
        pass

    def test_coroutines(self):
        sum1 = self.summerv1()
        global total
        total = 0
        # the summerv1 stores the total in global variable
        next(sum1), self.assertEqual(__, total, "The initial value")
        # to send value to z in coroutines use send function
        sum1.send(__), self.assertEqual(__, total, "When you add 10")
        # next(coroutines) == coroutines.send(None)
        next(sum1), self.assertEqual(__, total, "When you do not add anything")
        sum1.send(__), self.assertEqual(__, total, "When you add 11")
        sum1.send(None), self.assertEqual(__, total, "When you do not add anything")

    def summerv2(self, total=0):
        total = total
        while True:
            z = yield total
            total += z if z else 0
        pass

    def test_coroutines(self):
        sum2 = self.summerv2()
        # the function should be moved to yield first this can be done by
        # coroutines.send(None) or next(coroutines)
        self.assertEqual(__, sum2.send(None), "To move the function to yield")
        self.assertEqual(__, sum2.send(10), "When you add 10")
        self.assertEqual(__, next(sum2), "When you do not add anything")
        self.assertEqual(__, sum2.send(11), "When you add 11")
        self.assertEqual(__, sum2.send(None), "When you do not add anything")
        sum3 = self.summerv2()
        # if you don't move the function to yield the it throws typeerror
        with self.assertRaises(__, msg="catch the type error, you can only send None"):
            sum3.send(10)

    def safety_wrapper(cr):
        """the safety wrapper"""

        def init_cr(*args, **kwargs):
            dec_cr = cr(*args, **kwargs)
            dec_cr.send(None)
            return dec_cr

        return init_cr

    @safety_wrapper
    def summerv3(self):
        total = total
        while True:
            z = yield total
            total += z if z else 0
        pass

    def test_coroutines(self):
        sum4 = self.summerv3()
        # to avoid accidental error it is always good to call
        # decorate the coroutine which trigger next before other calls
        # all further coroutines are decorated using safety_wrapper
        self.assertEqual(__, sum4.send(10), "This won't throw type error")
        self.assertEqual(__, next(sum4), "When you do not add anything")
        self.assertEqual(__, sum4.send(11), "When you add 11")
        self.assertEqual(__, sum4.send(None), "When you do not add anything")

    @safety_wrapper
    def summerv4(self, total_init=0):
        total4 = total_init
        try:
            while True:
                z = yield total4
                total4 += z if z else 0
        except GeneratorExit:
            global total
            total = total4
        pass

    def looper(self, num_list=[]):
        sum5 = self.summerv4()
        for num in num_list:
            sum5.send(num)

    def test_generator_exit(self):
        # when the coroutines goes out of scope or is closed (coroutines.close())
        # GeneratorExit is throw in the coroutines
        # this can be caught and clean-up action can be taken
        global total
        # reseting the global total
        total = 0
        self.looper([100, 200, 300, 400, 500, 600])
        self.assertEqual(__, total, "see that total is set on exit")
        # reseting the global total
        total = 0
        sum6 = self.summerv4()
        for num in [100, 200, 300, 600]:
            if num == 500:
                break
            sum6.send(num)
        self.assertEqual(
            __, total, "see that total is not yet set as coroutine is not closed"
        )
        self.assertEqual(
            __, next(sum6), "see that coroutine is still alive and shows the sum"
        )
        sum6.close()
        self.assertEqual(__, total, "see that total is set on close")
        with self.assertRaises(
            __, msg="on closing the coroutine throws StopIteration on sending value"
        ):
            sum6.send(10)

    class reset_sum(Exception):
        "custom exception to be resting the value"
        pass

    @safety_wrapper
    def summerv5(self, total_init=0):
        total = total_init
        while True:
            try:
                z = yield total
                total += z if z else 0
            except self.reset_sum:
                total = total_init
        pass

    def test_coroutines(self):
        sum7 = self.summerv5()
        # Exception can be thrown at the yield and can be handled by genrator
        # here we design custom exception to reset the sum to initial value
        for num in [100, 200, 300, 400, 500, 600]:
            sum7.send(num)
        self.assertEqual(
            __,
            sum7.send(None),
            "see that the couroutine gives the sum of loop_list elements",
        )
        # let us reset the value of the summer
        self.assertEqual(
            __,
            sum7.throw(self.reset_sum),
            "reseting sum by throwing custom reset_sum exception",
        )
        for num in [100, 200, 300, 600]:
            sum7.send(num)
        self.assertEqual(
            __,
            next(sum7),
            "see that the couroutine gives the sum of loop_list2 elements",
        )
