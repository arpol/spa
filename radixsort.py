import itertools

def _partition(iterable, key):
    buckets = [list() for x in range(128)]
    for item in iterable:
        buckets[key(item)].append(item)
    return buckets

def msd(iterable):
    # Store the iterable as a list in case a generator is passed as the
    # argument.
    iterable = list(iterable)
    # We start with one partition containing the indices of all strings
    # in the set.
    partitions = [list(range(len(iterable)))]
    # Imagine all the strings in the set written out as rows of characters;
    # this confusing expression will iterate over successive columns of
    # characters, returning each column as a tuple.  As we stored the original,
    # *unsorted* indices of the strings in the partitions list, we can use them
    # to extract the relevant symbol of every string at each iteration of the
    # loop. We pad out strings that are too short with the null character.
    for column in itertools.zip_longest(*iterable, fillvalue='\0'):
        by_symbol = lambda i: ord(column[i])
        # Re-partition the previous partitions and merge the results
        # into a single list of partitions.  We effectively simulate
        # creating a trie of the string set here; by overwriting the
        # partitions variable, we only preserve one level of it in memory.
        partitions = list(itertools.chain.from_iterable(
            _partition(part, by_symbol) if len(part) > 1 else [part]
            for part in partitions if part
        ))
        # Break early if the set can't be partitioned any further.
        if all(len(part) == 1 for part in partitions):
            break
    # Extract the strings proper from the indices.
    return [iterable[i] for i in itertools.chain.from_iterable(partitions)]
