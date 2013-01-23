#!/usr/bin/python3

# Usage: ./map.py path.to.module:function < input.file > output.file
# 
# Reads the argument of a function from standard input and prints its
# return value to standard output.  The function must accept an iterator
# over strings as its argument and return an iterable over strings.
# Newlines will be stripped from the end of the input strings.
# 
# Example: ./map.py radixsort:msd < dataset.txt > sorted.txt

import sys
import radixsort

module, member = sys.argv[1].rsplit(':', 1)
func = getattr(__import__(name=module, fromlist=[member]), member)
print('\n'.join(func(line.rstrip('\n') for line in sys.stdin)))
