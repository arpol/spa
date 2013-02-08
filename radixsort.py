# -*- coding: utf-8 -*-

import insertionsort

def msd(iterable, depth=0):
    stack = [(iterable, depth)]
    while stack:
        bucket, depth = stack.pop()
        if depth < 0:
            for string in bucket:
                yield string
        else:
            buckets = [list() for x in range(256)]
            for string in bucket:
                if len(string) > depth:
                    buckets[ord(string[depth])].append(string)
                else:
                    yield string
            for bucket in reversed(buckets):
                if len(bucket) < 256:
                    stack.append((quicksort.QuickSort(bucket, depth+1), -1))
                else:
                    stack.append((bucket, depth+1))
