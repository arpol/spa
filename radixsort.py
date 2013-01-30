from quicksort import QuickSort

def msd(iterable):
    stack = [(iterable, 0)]
    while stack:
        iterable, depth = stack.pop()
        if depth < 0:
            for string in iterable:
                yield string
        else:
            buckets = [list() for x in range(128)]
            for string in iterable:
                key = ord(string[depth] if depth < len(string) else '\0')
                buckets[key].append(string)
            for bucket in reversed(buckets):
                if bucket:
                    if len(bucket) < 12:
                        stack.append((QuickSort(bucket, depth+1), -1))
                    else:
                        stack.append((bucket, depth+1))
            stack[-1] = (buckets[0], -1)
