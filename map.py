#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage: ./map.py path.to.module:function input.file > output.file
# 
# Reads the argument of a function from standard input and prints its
# return value to standard output.  The function must accept an iterator
# over strings as its argument and return an iterable over strings.
# Newlines will be stripped from the end of the input strings.
# 
# Example: ./map.py radixsort:msd dataset.txt > sorted.txt

import sys

try:
    module, member = sys.argv[1].rsplit(':', 1)
except ValueError:
    func = getattr(__builtins__, sys.argv[1])
else:
    func = getattr(__import__(name=module, fromlist=[member]), member)
with open(sys.argv[2]) as f:
    for line in func([line.rstrip('\n') for line in f]):
        print(line)
