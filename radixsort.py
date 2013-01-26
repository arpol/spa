def msd(iterable):
    stack = list([(iterable, 0)])
    while stack:
        iterable, depth = stack.pop()
        if len(iterable) < 8192:
            for string in sorted(iterable):
                yield string
        else:
            buckets = [list() for x in range(256)]
            for string in iterable:
                key = ord(string[depth] if depth < len(string) else '\0')
                buckets[key].append(string)
            for string in buckets[0]:
                yield string
            stack.extend((bucket, depth+1)
                         for bucket in buckets[-1:0:-1] if bucket)
