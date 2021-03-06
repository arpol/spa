#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage: ./map.py path.to.module:function input.file > output.file
# 
# Read the input file as a list of strings and pass it to the named
# function, printing each string of output on its own line to standard
# output.  The function must take as its argument an iterable over
# strings and return an iterable over strings.  Python built-in
# functions are referred to without a module path or any leading
# periods or colons.
# 
# Examples:
#   ./map.py radixsort:msd dataset.txt > sorted.txt
#   ./map.py sorted dataset.txt > comparison.txt

import sys

# These two algorithms are special-cased as they operate on the input as one
# large string, as opposed to a list of lines.
if sys.argv[1] == 'burst:main':
    import burst
    burst.main(sys.argv[2])
elif sys.argv[1] == 'mkqsort:main':
    import mkqsort
    mkqsort.main(sys.argv[2])
else:
    try:
        module, member = sys.argv[1].rsplit(':', 1)
    except ValueError:
        func = getattr(__builtins__, sys.argv[1])
    else:
        func = getattr(__import__(name=module, fromlist=[member]), member)
    with open(sys.argv[2]) as f:
        for line in func([line.rstrip('\n') for line in f]):
            print(line)
