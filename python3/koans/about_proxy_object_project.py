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

# Note: This is a bit trickier that it's Ruby Koans counterpart, but you
# can do it!

from runner.koan import *

class Proxy(object):
    def __init__(self, target_object):
        # Write your attribute initialisations here
        self._messages = list()
        
        #initialize attribute this last. Trust me!
        self._obj = target_object

    # WRITE CODE HERE
    def __getattr__(self, name):
        #print 'Debug GET ' + type(self).__name__ + "." + name + " dict=" + str(self.__dict__)
    
        attr = getattr(self._obj, name)
        
        self._messages.append(name)
        return attr    

    def __setattr__(self, name, value):
        #print 'Debug SET ' + type(self).__name__ + "." + name + "=" + str(value) + "   __dict__=" + str(self.__dict__)
       
        if '_' == name[0]:
            return object.__setattr__(self, name, value)
                    
        setattr(self._obj, name, value)
        
        self._messages.append(name + '=')
                
    def messages(self):
        return self._messages
    
    def was_called(self, attr):
        return self.number_of_times_called(attr) > 0
            
    def number_of_times_called(self, attr):
        return len(list(filter(lambda msg: msg==attr , self._messages)))
#class Proxy:
#    def __init__(self, target_object):
#        # WRITE CODE HERE
#        
#        #initialize '_obj' attribute last. Trust me on this!
#        self._obj = target_object
#    
#    # WRITE CODE HERE                                   

# The proxy object should pass the following Koan:
#
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
        
        self.assertEqual(['power', 'channel='], tv.messages())
    
    def test_proxy_handles_invalid_messages(self):
        tv = Proxy(Television())
        
        ex = None
        with self.assertRaises(AttributeError): #####
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
        self.assertEqual(1, tv.number_of_times_called('channel='))
        self.assertEqual(0, tv.number_of_times_called('is_on'))
    
    def test_proxy_can_record_more_than_just_tv_objects(self):
        proxy = Proxy("Code Mash 2009")
      
        result = proxy.upper()

        self.assertEqual("CODE MASH 2009", result)
        
        result = proxy.split()

        self.assertEqual(["Code", "Mash", "2009"], result)
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
    def test_it_turns_on(self):
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
