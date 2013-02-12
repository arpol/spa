#!/usr/bin/python

from random import random
import sys
import os

import insertion
from burstSettings import EOS, INS_SORT_TRESHOLD

class mkqsorter(object):
    
    def setup(self, data, indexes):
        self.data = data
        self.a = indexes

    def swap(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def nswap(self, i, j, l):
        self.a[i: i + l], self.a[j: j + l] = self.a[j: j + l], self.a[i: i + l]

    def ch(self, i):
        return self.data[self.a[i] + self.d]
    
    def __str__(self):
        s = ""
        for i in self.a:
            j = i
            while self.data[j] != EOS:
                s += chr(self.data[j])
                j += 1
            s += ','
        return s 

    """ Sorts indexes [L, R[ of array 'a' using the multikey quicksort
    algorithm. The array 'a' is defined as in sort.  The pivot index 'p'
    is chosen randomly.
    """
    def sort(self, n):
        stack = [(0, n, 0)]
        
        while len(stack) > 0:
            L, R, self.d = stack.pop()
    
            n = R - L

            if n < INS_SORT_TRESHOLD:
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


def read(filename):
    totalBytes = os.path.getsize(filename)
    data = bytearray(totalBytes)
    with open(filename, 'rb') as file:
        file.readinto(data)
    assert data[-1] == EOS
    return data

def index(data):
    indexes = [0]
    for i in xrange(len(data)):
        if data[i] == EOS:
            indexes.append(i + 1);
    indexes.pop()
    return indexes

def outputBuffer(data, strings):
    output = bytearray(len(data))
    counter = 0
    for i in strings:
        j = i
        while True:
            output[counter] = b[j]
            counter += 1
            if data[j] == EOS:
                break
            j += 1
    return output

def main(filename = sys.argv[1]):
    data = read(filename)
    strings = index(data)
    sort(data, strings)
    sys.stdout.write(outputBuffer(data, strings))

if __name__ == '__main__':
    main()
