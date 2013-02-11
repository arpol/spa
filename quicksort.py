#!/usr/bin/python

import math
import sys
import itertools

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
    Performs string quicksort on the strings in iterable
    
    Input: 
    
        (Multi)set iterable of strings and the length
        Integer depth = position being compared, defaults to zero
        
    Output: 
    
        iterable in ascending lexicographical order.
        
    """
    stack = [[iterable, depth]] #recurssion stack    
    
    result = [] #store the sorted list here
    
    while stack :
        R, l = stack.pop() #get the list to sort in the current iteration, position marker being sorted
        
        length = len(R)
        
        if length <= 1:
            if length == 1 :
                result += R
            continue
        
        #init empty lists
        R_less = [] 
        R_equal = [] 
        R_greater = []
        R_new = [] #updated R

        for S in R:
            if len(S) <= l :
                result.append(S)
            else :
                R_new.append(S)
        
        if len(R_new) == 0 :
            continue
        
        X = R_new[SelectPivot(R_new)]
        
        char_at_x = X[l]
        
        for S in R_new : #partition the list into smaller-than, equal, greater-than lists
            if S[l] < char_at_x :
                R_less.append(S)
            elif S[l] == char_at_x :
                R_equal.append(S)
            else :
                R_greater.append(S)

        stack.append((R_greater, l))
        stack.append((R_equal, l+1))
        stack.append((R_less, l))

    return result

if __name__ == "__main__" :
    #rudimentary test:
    _R = ['abc','def', 'i', 'aaf','adsf1','gxxa','a']

    print(TernaryQuickSort(_R))
    print(QuickSort(_R))
