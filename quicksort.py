# -*- coding: utf-8 -*-

import insertionsort

def median(x,y,z):
    if   y <= x <= z or z <= x <= y:
        return x
    elif x <= y <= z or z <= y <= x:
        return y
    elif x <= z <= y or y <= z <= x:
        return z

def insertion(iterable, depth=0):
    stack = [(iterable, depth)]
    while stack:
        bucket, depth = stack.pop()
        new_bucket = []
        for string in bucket:
            if len(string) > depth >= 0:
                new_bucket.append(string)
            else:
                yield string
        if len(new_bucket) > 16:
            pivot = median(new_bucket[0][depth],
                           new_bucket[len(new_bucket)//2][depth],
                           new_bucket[-1][depth])
            lesser = []
            equal = []
            greater = []
            for string in new_bucket:
                if string[depth] < pivot:
                    lesser.append(string)
                elif string[depth] == pivot:
                    equal.append(string)
                elif string[depth] > pivot:
                    greater.append(string)
            stack.append((greater, depth))
            stack.append((equal, depth+1))
            stack.append((lesser, depth))
        else:
            for string in insertionsort.multikey(new_bucket, depth):
                yield string
