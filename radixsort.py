import itertools
from quicksort import QuickSort

def msd(iterable, depth=0):
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
                    if len(bucket) < 256:
                        stack.append((QuickSort(bucket, depth+1), -1))
                    else:
                        stack.append((bucket, depth+1))
            stack[-1] = (buckets[0], -1)

def lsd(iterable):
    array = sorted(iterable, key=len)
    bound = len(array) - 1
    for depth in reversed(range(len(array[bound]))):
        while bound > 0 and len(array[bound-1]) > depth:
            bound -= 1
        buckets = [list() for x in range(256)]
        for string in array[bound:]:
            key = ord(string[depth])
            buckets[key].append(string)
        array[bound:] = itertools.chain.from_iterable(buckets)
    return array
