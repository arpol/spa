#!/usr/bin/python

from random import random
import sys
import os

import burst
import insertion
from burstSettings import EOS, INS_SORT_THRESHOLD

class mkqsorter(object):

    """A multikey quicksort implementation. Strings are stored in an
    array, delimited by EOS. The index array pointing to each string's
    start is sorted.
    """

    def setup(self, data, indexes):
        self.data = data
        self.a = indexes

    def swap(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def nswap(self, i, j, l):
        self.a[i: i + l], self.a[j: j + l] = self.a[j: j + l], self.a[i: i + l]

    def ch(self, i):
        return self.data[self.a[i] + self.d]
    
    def sort(self, n):
        """ Sorts the first n strings of array self.a. Falls back to
        insertion sort for partitions with fewer than
        INS_SORT_THRESHOLD elements. During partitioning swaps items
        that are equal to the pivot to the beginning and end of the
        range and finally swaps them to their correct place before
        sorting the partitions.

        stack     - stores the partitions to be sorted and the corresponding depths
        L,R       - limits of the current partition (L inclusive, R exclusive)
        p         - pivot index, randomly selected from [L,R[
        pivot     - pivot value
        l, r      - sliding indexes. ch(i) <= pivot for i in [L, l[; r mirrors this
        lEq, rEq  - the indexes for the next equal-to-pivot items on the left and right side
        """
        stack = [(0, n, 0)]
        while len(stack) > 0:
            L, R, self.d = stack.pop()
            n = R - L
            if n < INS_SORT_THRESHOLD:
                insertion.sort(self.data, self.a, self.d, L, R)
                continue
            if n < 2:
                continue
            p = L + int(random() * n)
            p = L
            self.swap(L, p)
            lEq = l = L + 1
            rEq = r = R - 1
            pivot = self.ch(L)
            while True:
                while l <= r and self.ch(l) <= pivot:
                    if self.ch(l)  == pivot:
                        self.swap(lEq, l)
                        lEq += 1
                    l += 1
                while l <= r and self.ch(r) >= pivot:
                    if self.ch(r) == pivot:
                        self.swap(rEq, r)
                        rEq -= 1
                    r -= 1
                if l > r:
                    break
                self.swap(l, r)
                l += 1
                r -= 1
            c = min(lEq - L, l - lEq)
            self.nswap(L, l - c, c)
            c = min(R - 1 - rEq, rEq - r)
            self.nswap(l, R - c, c)
            stack.append((L, L + l - lEq, self.d))
            if pivot != EOS:
                stack.append((L + l - lEq, l + (R - 1 - rEq), self.d + 1))
            stack.append((R - (rEq - r), R, self.d))


sorter = mkqsorter() 

def sort(data, array, n = -1):
    if n == -1:
        n = len(array)
    sorter.setup(data, array)
    sorter.sort(n)


# The following functions are not used when mkqsort is used as a
# helper sort.

def index(data):
    """Find all strings, delimited by EOS, in 'data' and return them
    as a list.
    """
    indexes = [0]
    for i in xrange(len(data)):
        if data[i] == EOS:
            indexes.append(i + 1);
    indexes.pop()
    return indexes

def output(data, indexes):
    """Write the strings pointed to by 'indexes' to a bytearray buffer
    and return the buffer.
    """
    output = bytearray(len(data))
    counter = 0
    for i in indexes:
        j = i
        while True:
            output[counter] = data[j]
            counter += 1
            if data[j] == EOS:
                break
            j += 1
    return output

def main(filename = sys.argv[1]):
    data, finalEOS = burst.read(filename)
    strings = index(data)
    sort(data, strings)
    outputBuffer = output(data, strings);
    if not finalEOS:
        outputBuffer.pop()
    sys.stdout.write(outputBuffer)

if __name__ == '__main__':
    main()
