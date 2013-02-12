#!/usr/bin/python

import sys
import os
import array

import mkqsort
from burstSettings import EOS, BURST_LIMIT


class Node(object):

    """An inner node in a burst trie."""

    def __init__(self):
        self.links = [None] * 256
        self.links[EOS] = Counter()

    def insert(self, data, pointer):
        c = data[pointer]
        if self.links[c] is None:
            self.links[c] = Container(self, c)
        self.links[c].insert(data, pointer + 1)
    
    def output(self, data, buffer, index = 0, prefix = bytearray()):
        """Recursively output all children in alphabetical order"""
        for i, link in enumerate(self.links):
            if not link is None:
                prefix.append(i)
                index = link.output(data, buffer, index, prefix)
                prefix.pop()
        return index


class Counter(object):

    """A leaf node counting the occurences of a string that has been
    fully consumed in the inner nodes.
    """

    def __init__(self):
        self.count = 0
            
    def insert(self, data, pointer):
        self.count += 1
        
    def output(self, data, buffer, index, prefix):
        for x in xrange(self.count):
            buffer[index: index + len(prefix)] = prefix
            index += len(prefix)
        return index


class Container(object):

    """A leaf node containing suffixes for strings that have the same
    prefix represented by the path from the root of the trie to this
    node. The suffixes are indexes to an array containing all the
    strings separated with EOS characters. The prefix is not stored
    explicitly.
    """

    count = 0
    
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.count = 0
        self.buf = array.array('i')
        Container.count += 1

    def insert(self, data, pointer):
        if self.count == BURST_LIMIT:
            node = self.burst(data)
            node.insert(data, pointer)
            self.parent.links[self.value] = node
            return
        self.buf.append(pointer)
        self.count += 1
        
    def burst(self, data):
        node = Node()
        for i in xrange(self.count):
            node.insert(data, self.buf[i])
        return node

    def output(self, data, buffer, index, prefix):
        if self.count > 1:
            mkqsort.sort(data, self.buf, self.count)
        for i in xrange(self.count):
            buffer[index: index + len(prefix)] = prefix
            index += len(prefix)
            j = self.buf[i]
            while True:
                buffer[index] = data[j]
                index += 1
                if data[j] == EOS:
                    break
                j += 1
        return index


def read(filename):
    """Read the contents of a file to a bytearray. Ensure the final
    character is EOS.
    """
    data = bytearray(os.path.getsize(filename) + 1)
    with open(filename, 'rb') as file:
        file.readinto(data)
    if data[-2] == EOS:
        data.pop()
        finalEOS = True
    else:
        data[-1] = EOS
        finalEOS = False
    return data, finalEOS

def makeTrie(data):
    """Scan data for string delimeters and insert the found strings to
    a burst trie.
    """
    root = Node()
    start = end = count = 0
    while start < len(data):
        while data[end] != EOS:
            end += 1
        root.insert(data, start)
        count += 1
        start = end = end + 1
    return root

def main(filename = sys.argv[1]):
    data, finalEOS = read(filename)
    trie = makeTrie(data)
    outputBuffer = bytearray(len(data))
    trie.output(data, outputBuffer)
    if not finalEOS:  #don't print a final EOS if there was none in the input
        outputBuffer.pop()
    sys.stdout.write(outputBuffer)


if __name__ == '__main__':
    main()
