#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = (
    'Goat',
    '_Velociraptor'
)


class Goat(object):
    @property
    def name(self):
        return "George"


class _Velociraptor(object):
    @property
    def name(self):
        return "Cuddles"


class SecretDuck(object):
    @property
    def name(self):
        return "None of your business"
