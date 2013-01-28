#!/usr/bin/python

"""
Try next 1)Binary quicksort, 2)Multikey quicksort

Algorithm 1.16
"""
import math
import sys

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
            i_median = i_mid
        elif R[i_first] >= [i_last] : #312
            i_median = i_last
        else : #213
            i_median = i_first
    else: #last element is smaller than the middle: 132,231,321 
        if R[i_mid] <= R[i_first] : #321
            i_median = i_mid
        elif R[i_first] <= R[i_last] : #132
            i_median = i_last
        else : #231
            i_median = i_first
    return i_median
        
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

def QuickSort(R, l=0):
    """
    Performs string quicksort on the strings in R 
    
    Input: 
    
        (Multi)set R of strings and the length
        Integer l = position being compared, defaults to zero
        
    Output: 
    
        R in ascending lexicographical order.
        
    """
    length = len(R)
    
    if length <= 1:
        return R
    
    #init empty lists
    R_less = [] 
    R_equal = [] 
    R_greater = []
    R_short = [] #list for storing the string that are exactly of length l
    
    for index, S in enumerate(R) :
        if len(S) <= l+1:
            R_short.append(S)
            R.pop(index)
            
    X = R[SelectPivot(R)]
    
    for S in R : 
        if S[l] < X[l] :
            R_less.append(S)
        elif S[l] == X[l] :
            R_equal.append(S)
        else :
            R_greater.append(S)
    R_less = QuickSort(R_less, l)
    R_equal = QuickSort(R_equal, l+1)
    R_greater = QuickSort(R_greater, l)
    
    return R_short + R_less + R_equal + R_greater
            
_R = ['abc','def','aaf','adsf1','gxxa','a']

print TernaryQuickSort(_R)
print QuickSort(_R)




