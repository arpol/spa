#!/usr/bin/python

import sys
import os
import array

import mkqsort
from burstSettings import EOS, BURST_LIMIT

class Node(object):

    """An inner node in a burst trie."""

    count = 0

    def __init__(self):
        Node.count += 1
        self.links = [None] * 256
        self.links[EOS] = ZeroContainer()

    def insert(self, pointer):
        c = data[pointer]
        if self.links[c] is None:
            self.links[c] = Container(self, c)
        self.links[c].insert(pointer + 1)
    
    def output(self, prefix = bytearray()):
        """Recursively output all children in alphabetical order"""
        for i, link in enumerate(self.links):
            if not link is None:
                prefix.append(i)
                link.output(prefix)
                prefix.pop()

class ZeroContainer(object):

    """A leaf node counting the occurences of a string that has been
    fully consumed in the inner nodes.
    """

    def __init__(self):
        self.count = 0
            
    def insert(self, pointer):
        self.count += 1
        
    def output(self, prefix):
        global outIndex, outBuf
        for x in xrange(self.count):
            outBuf[outIndex:outIndex + len(prefix)] = prefix
            outIndex += len(prefix) 
    def __str__(self):
        return ""

    def size(self, prefixsize):
        return self.count * prefixsize

class Container(object):

    """A leaf node containing suffixes for strings that have the same
    prefix represented by the path from the root of the trie to this
    node. The suffixes are indexes to an array containing all the
    strings separated with EOS characters. The prefix is not stored
    explicitly. A container may only contain a fixed amount of
    strings. If this limit is reached, the container will burst, i.e.
    a new inner node will be created and the string will be
    distributed in the containers of that node.
    """

    count = 0
    
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.count = 0
        self.buf = array.array('i')
        Container.count += 1

    def insert(self, pointer):
        if self.count == BURST_LIMIT:
            node = self.burst()
            node.insert(pointer)
            self.parent.links[self.value] = node
            return
        self.buf.append(pointer)
        self.count += 1
        
    def burst(self):
        node = Node()
        for i in xrange(self.count):
            node.insert(self.buf[i])
        return node

    def output(self, prefix):
        global outBuf, outIndex

        if self.count > 1:
            mkqsort.sort(data, self.buf, self.count)
        
        for i in xrange(self.count):
            outBuf[outIndex:outIndex + len(prefix)] = prefix
            outIndex += len(prefix)
            j = self.buf[i]
            while True:
                outBuf[outIndex] = data[j]
                outIndex += 1
                if data[j] == EOS:
                    break
                j += 1


def main(filename = sys.argv[1]):
    initBuffers(filename)
    sort()

def initBuffers(filename):
    totalBytes = os.path.getsize(filename)
    global data, outBuf, outIndex
    data = bytearray(totalBytes)
    outBuf = bytearray(totalBytes)
    outIndex = 0
    with open(filename, 'rb') as file:
        file.readinto(data)
    assert data[-1] == EOS

def sort():
    root = Node()

    start = end = 0
    count = 0

    while start < len(data):
        while data[end] != EOS:
            end += 1
        root.insert(start)
        count += 1
        start = end = end + 1

    root.output()
    sys.stdout.write(outBuf)


if __name__ == '__main__':
    main()
