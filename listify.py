#!/usr/bin/python
import sys
import re

def listify(filepath) :
    """
    Converts the input text into a line separated list of words
    
    Usage ./listify.py INPUT > OUTPUT
    
    Input: 
        filepath - path to the dataset filepath
    
    Output: 
        dataset converted to one word by line format
    """
    output = []
    f = open(filepath)
    for line in f :
        output += re.findall(r"[\w']+", line)
    for S in output :
        print S
    #print output
    
if __name__ == "__main__" :
    listify(sys.argv[1])