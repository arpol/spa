# -*- coding: utf-8 -*-

import quicksort

def msd(iterable, depth=0):
    """Iterate over the sequences in ``iterable`` in lexicographical order,
    determined using MSD radix sort.
    
    The optional ``depth`` parameter determines the position from which to
    start comparing sequences.  Default is 0.
    
    Note that this function returns a generator, not a list.  If a sorted
    list is desired, invoke it with ``list(msd(iterable))``.
    
    """
    # A naive recursive implementation would blow Python's recursion
    # limit on larger inputs, so we emulate boundless recursion with
    # a simple stack.
    stack = [(iterable, depth)]
    while stack:
        bucket, depth = stack.pop()
        if depth < 0:
            # Negative depth is used to mark pre-sorted buckets; we can
            # output these as-is.
            for string in bucket:
                yield string
        else:
            # A Python dict would be more intuitive here, but as it does not
            # preserve key ordering, we allocate a list of buckets and use
            # each character's Unicode code point number as its address in
            # the table.
            buckets = [list() for x in range(256)]
            for string in bucket:
                # Strings shorter than the sorting depth come first in the
                # in-bucket ordering, so we can output them as-is.  The
                # rest are appended to the appropriate buckets.
                if len(string) <= depth:
                    yield string
                else:
                    buckets[ord(string[depth])].append(string)
            # The newly filled buckets are pushed to the top of the stack in
            # reverse order.  This guarantees that the lexicographically first
            # bucket is always at the top of the stack, so when its contents
            # are eventually pushed to output, they come first as well.
            for bucket in reversed(buckets):
                # Buckets smaller than the alphabet are better sorted with
                # string quicksort, so we use Arturs's implementation and mark
                # the bucket as pre-sorted.  The rest are pushed to the stack
                # as-is, with the sorting depth incremented by one.
                if len(bucket) < 256:
                    stack.append((quicksort.QuickSort(bucket, depth+1), -1))
                else:
                    stack.append((bucket, depth+1))
