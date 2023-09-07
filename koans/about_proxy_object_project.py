#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project: Create a Proxy Class
#
# In this assignment, create a proxy class (one is started for you
# below).  You should be able to initialize the proxy object with any
# object.  Any attributes called on the proxy object should be forwarded
# to the target object.  As each attribute call is sent, the proxy should
# record the name of the attribute sent.
#
# The proxy class is started for you.  You will need to add a method
# missing handler and any other supporting methods.  The specification
# of the Proxy class is given in the AboutProxyObjectProject koan.

# Note: This is a bit trickier than its Ruby Koans counterpart, but you
# can do it!

from runner.koan import Koan


class Proxy:
    def __init__(self, target_object):
        # WRITE CODE HERE
        self._messages = []
        # initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object

    # WRITE CODE HERE
    def messages(self):
        return self._messages

    def was_called(self, attr_name):
        response = False

        for v in self._messages:
            if v == attr_name:
                response = True
                break

        return response

    def number_of_times_called(self, attr_name):
        response = 0

        for message in self._messages:
            if message == attr_name:
                response += 1

        return response

    def __setattr__(self, attr_name, value):
        to_set = None

        if attr_name == "_obj" or attr_name == '_messages':
            to_set = self
        else:
            self._messages.append(attr_name)
            to_set = super().__getattribute__("_obj")

        return object.__setattr__(to_set, attr_name, value)

    def __getattr__(self, attr_name):
        obj = super().__getattribute__("_obj")
        response = obj.__getattribute__(attr_name)
        self._messages.append(attr_name)
        return response

# The proxy object should pass the following Koan:


class AboutProxyObjectProject(Koan):
    def test_proxy_method_returns_wrapped_object(self):
        # NOTE: The Television class is defined below
        tv = Proxy(Television())

        self.assertTrue(isinstance(tv, Proxy))

    def test_tv_methods_still_perform_their_function(self):
        tv = Proxy(Television())

        tv.channel = 10
        tv.power()

        self.assertEqual(10, tv.channel)
        self.assertTrue(tv.is_on())

    def test_proxy_records_messages_sent_to_tv(self):
        tv = Proxy(Television())

        tv.power()
        tv.channel = 10

        self.assertEqual(['power', 'channel'], tv.messages())

    def test_proxy_handles_invalid_messages(self):
        tv = Proxy(Television())

        with self.assertRaises(AttributeError):
            tv.no_such_method()

    def test_proxy_reports_methods_have_been_called(self):
        tv = Proxy(Television())

        tv.power()
        tv.power()

        self.assertTrue(tv.was_called('power'))
        self.assertFalse(tv.was_called('channel'))

    def test_proxy_counts_method_calls(self):
        tv = Proxy(Television())

        tv.power()
        tv.channel = 48
        tv.power()

        self.assertEqual(2, tv.number_of_times_called('power'))
        self.assertEqual(1, tv.number_of_times_called('channel'))
        self.assertEqual(0, tv.number_of_times_called('is_on'))

    def test_proxy_can_record_more_than_just_tv_objects(self):
        proxy = Proxy("Py Ohio 2010")

        result = proxy.upper()

        self.assertEqual("PY OHIO 2010", result)

        result = proxy.split()

        self.assertEqual(["Py", "Ohio", "2010"], result)
        self.assertEqual(['upper', 'split'], proxy.messages())

# ====================================================================
# The following code is to support the testing of the Proxy class.  No
# changes should be necessary to anything below this comment.

# Example class using in the proxy testing above.


class Television:
    def __init__(self):
        self._channel = None
        self._power = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        if self._power == 'on':
            self._power = 'off'
        else:
            self._power = 'on'

    def is_on(self):
        return self._power == 'on'

# Tests for the Television class.  All of theses tests should pass.

class TelevisionTest(Koan):
    "asdfadsf"
    def test_it_turns_on(self):
        "Hey"
        tv = Television()

        tv.power()
        self.assertTrue(tv.is_on())

    def test_it_also_turns_off(self):
        tv = Television()

        tv.power()
        tv.power()

        self.assertFalse(tv.is_on())

    def test_edge_case_on_off(self):
        tv = Television()

        tv.power()
        tv.power()
        tv.power()

        self.assertTrue(tv.is_on())

        tv.power()

        self.assertFalse(tv.is_on())

    def test_can_set_the_channel(self):
        tv = Television()

        tv.channel = 11
        self.assertEqual(11, tv.channel)
