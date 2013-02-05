# -*- coding: utf-8 -*-

# Python 3 compatibility
def cmp(x,y):
    if    x < y:  return -1
    elif  x > y:  return +1
    else:         return  0

def LCPcmp(A,B,k):
    while k < min(len(A),len(B)):
        order = cmp(A[k],B[k])
        if order:  return order, k
        else:      k += 1
    return cmp(len(A),len(B)), k

def multikey(iterable, depth=0):
    ordered = []
    for s in iterable:
        LCPs = lcp = depth
        i = len(ordered)
        for p, LCPp in reversed(ordered):
            order, LCPs = LCPcmp(s,p,lcp)
            if order >= 0:
                break
            i -= 1
            lcp = LCPs
            if LCPs > LCPp:
                LCPs = LCPp
                break
        if 0 <= i < len(ordered):
            ordered[i] = ordered[i][0], lcp
        ordered.insert(i, (s, LCPs))
    return (p for p, LCPp in ordered)
