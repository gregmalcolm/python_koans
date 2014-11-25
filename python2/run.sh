#!/bin/sh

if [ -x /usr/bin/python2 ]; then
    python2 -B contemplate_koans.py
else
    python -B contemplate_koans.py
fi
