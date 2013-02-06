# -*- coding: utf-8 -*-

import insertionsort

def insertion(iterable, depth=0):
    stack = [(iterable, depth)]
    while stack:
        iterable, depth = stack.pop()
        if depth < 0:
            for string in iterable:
                yield string
        else:
            buckets = [list() for x in range(256)]
            for string in iterable:
                key = ord(string[depth] if depth < len(string) else '\0')
                buckets[key].append(string)
            for bucket in reversed(buckets):
                if bucket:
                    if len(bucket) < 16:
                        stack.append((insertionsort.multikey(bucket, depth+1), -1))
                    else:
                        stack.append((bucket, depth+1))
            if buckets[0]:
                stack[-1] = (buckets[0], -1)
