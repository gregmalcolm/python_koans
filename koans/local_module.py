#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Duck:
    def __init__(self):
        self._password = 'password' # Genius!

    @property
    def name(self):
        return "Daffy"
