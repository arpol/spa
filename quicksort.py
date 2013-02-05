#!/usr/bin/python

"""
Try next 1)Binary quicksort, 2)Multikey quicksort
"""
import math
import sys
import itertools

#sys.setrecursionlimit(5)

def SelectPivot(R):
    """
    Cacluclate a pivot given list of strings R
    Pick the last, the first, and the middle element, and choose their median as a pivot
    Source: http://www.cs.utexas.edu/~lavender/courses/EE360C/lectures/lecture-22.pdf
    """
    length = len(R)    
    i_first = 0
    i_last = length-1
    i_mid = int(math.ceil((length-1)/2))
    #only two elements, return any:
    if i_last == i_mid :
        return i_first 
    #Otherwise, if there are three elements,
    #Possible arrangements are: 123,132,213,231,312,321
    if R[i_last] >= R[i_mid] : #last element is bigger than the middle:  123,213,312
        if R[i_mid] >= R[i_first] : #123
            return i_mid
        elif R[i_first] >= R[i_last] : #312
            return i_last
        else : #213
            return  i_first
    else: #last element is smaller than the middle: 132,231,321 
        if R[i_mid] <= R[i_first] : #321
            return i_mid
        elif R[i_first] <= R[i_last] : #132
            return i_last
        else : #231
            return i_first
    return None
        
def TernaryQuickSort(R):
    """
    Performs string ternary quicksort on the strings in R 
    
    Input: 
    
        (Multi)set R in arbitrary order.
        
    Output: 
    
        R in ascending order.
        
    """
    length = len(R)
    if length <= 1:
        return R
    x = SelectPivot(R)
    #init empty lists
    R_less = [] 
    R_equal = [] 
    R_greater = []
    for s in R :
        if s < R[x] :
            R_less.append(s)
        elif s == R[x] :
            R_equal.append(s)
        else :
            R_greater.append(s)
    R_less = TernaryQuickSort(R_less)
    R_greater = TernaryQuickSort(R_greater)
    return R_less + R_equal + R_greater

def QuickSort(iterable, depth=0):
    """
    Performs string quicksort on the strings in R 
    
    Input: 
    
        (Multi)set iterable of strings and the length
        Integer l = position being compared, defaults to zero
        
    Output: 
    
        R in ascending lexicographical order.
        
    """
    #print(R)
    
    stack = [[iterable, depth]]
    
    result = []
    while stack :
        R, l = stack.pop()
        #print("\n")
        #print("Iterating: ")
        #print(R)
        #print(l)
        length = len(R)
        
        if length <= 1:
            #print("R is: ")
            #print(R)
            #print("length is: ")
            #print(length)
            if length == 1 :
                result += R
            continue
        
        #init empty lists
        R_less = [] 
        R_equal = [] 
        R_greater = []
        R_short = [] #list for storing the string that are exactly of length l
        R_new = [] #updated R

        """
        for x in R:
            if len(x) <= l :
                result.append(x)
            else :
                R_new.append(x)
        """
        def yielding():
            def yielder():
                for x in R:
                    if len(x) <= l :
                        result.append(x)
                        continue
                    yield x
            return list(yielder())
        
        R = yielding()

        if len(R) == 0 :
            continue
        
        #print("prepivot...")
        
        #Try with random pivot with value close to center
        X = R[SelectPivot(R)]
        #X = R[int(math.floor((len(R))/2))]
        
        #print("Pivot")
        #print(X)
        
        char_at_x = X[l]
        
        for S in R :
            if S[l] < char_at_x :
                R_less.append(S)
            elif S[l] == char_at_x :
                R_equal.append(S)
            else :
                R_greater.append(S)

        stack.append((R_greater, l))
        stack.append((R_equal, l+1))
        stack.append((R_less, l))
        #print "Printing stack: "
        #print(stack)
        #return R_short + R_less + R_equal + R_greater
    
    #print("Result: ")
    #print(result)
    return result



"""
def yielding():
    def yielder():
        for d in data:
            yield d
    return list(yielder())

        for S in R :                
            if S[l] < char_at_x :
                R_less.append(S)
            elif S[l] == char_at_x :
                R_equal.append(S)
            else :
                R_greater.append(S)
                
from itertools import groupby 

def cleave_by_change2(stream, key_fn):
    return (group for key, group in groupby(stream, key_fn))

main_gen = cleave_by_change2(R, lambda x: x)

print main_gen

for sub_gen in main_gen:
    print sub_gen
    print list(sub_gen)

"""
if __name__ == "__main__" :
    #rudimentary test
    _R = ['abc','def', 'i', 'aaf','adsf1','gxxa','a']

    print(TernaryQuickSort(_R))
    print(QuickSort(_R))
