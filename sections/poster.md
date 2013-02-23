# Introduction

Comparison-based sorting is one of the most mature subfields of CS research.
However, the more well-known of such algorithms have been designed with the
expectation that the objects they sort can be compared in constant time.
When used to sort objects that require linear-time comparison operations,
such as strings, they perform a lot of wasteful work that leads to suboptimal
performance.  For maximum efficiency, *string sorting algorithms* are
necessary.

We have implemented a family of three different string sorting algorithms in
Python and compared their performance against Python's native Timsort [1] using
four different datasets with two variants each.

# Algorithms

String processing algorithms distinguish themselves from naive comparison
algorithms by maintaining knowledge of the lengths of the *longest common
prefixes* (LCP) of pairs of input strings as they sort them, which they use to
avoid redundant comparisons.  The *LCP array* of a set of strings, by
extension, is defined as follows:

    Given an ordered set of strings *S_1 < ... < S_n*,
    *LCP[1]* is *0* and *LCP[i]* is the length of the longest common prefix of
    strings *S_i* and *S_i-1* when *i > 1*.
    
    i  S_i          LCP[i]
    1  actor        0
    2  *a*llocate   1
    3  *al*pha      2
    4  beta         0
    5  *b*yproduct  1

Observe that were one to confirm that the set of strings in the above example
is indeed sorted, one would have to check exactly the highlighted characters
plus one for every string, with the first string excepted.
In fact, *Ω(L(R) + n)* represents the lower bound for any algorithm that must
access symbols one at a a time, where *L(R)* is the sum of the LCP array for
a set of strings *R* and *n* is its number of elements.  In comparison, the
average lower bound for sorting strings using only naive comparisons is
*Ω(n(log n)^2)*.

## Quicksort

## Burstsort

## MSD radix sort

MSD radix sort first partitions the strings into different buckets based on
first symbol is, then recursively partitions *those* buckets based on what
the second symbol is, and so on.  When only single-element buckets or buckets
containing only strings shorter than the recursion depth are left, the results
are concatenated and output.

    *Highlight and underline these to illustrate the partitioning.*
    actor
    allocate
    alpha
    beta
    byproduct

MSD radix sort never needs to process a symbol twice, technically giving it
*O(L(R) + n)* complexity assuming a finite alphabet.  However, the complexity
is dominated by the bucket container data structure: if *σ* is the size of the
alphabet and if the buckets are stored in a binary search tree, each addition
takes *O(log σ)* time.  If they are stored in an array or a hash table, merging
takes *Φ(σ)* time.

Our implementation uses a fixed alphabet size of 256 and stores the buckets in
an array, falling back to string quicksort on buckets smaller than the alphabet
size.

# Datasets

With the exception of the URLs dataset, all datasets were retrieved from
the Pizza & Chili Corpus [2]; the URL dataset is the one used by Ranjan Sinha
in his original burstsort paper [3]. The algorithms were tested on a sample
of 100 and 200 megabytes with each dataset.

## DNA

The DNA dataset consists of sequences of nucleotide codes, all exactly 3732300
characters in length.  This is by far the easiest dataset, having the smallest
number of strings and the smallest LCP array sum; very little of the extremely
long strings is actually required for sorting them.

## PROTEINS

The PROTEINS dataset consists of sequences of amino acid codons of varying
lengths.  It can be perceived as a more challenging variant of the DNA dataset,
having two orders of magnitude more strings and an LCP array sum four whole
orders of magnitude larger while retaining a similar alphabet.

## URLS

The URLS dataset consists of several web addresses.  Due to most common URLs
having similar prefixes, as well as the dataset containing several duplicate
URLs, this dataset has the highest LCP array sum, though not significantly
higher than the WORDS dataset.

## WORDS

The WORDS dataset is a modification of the ENGLISH dataset of the Pizza & Chili
Corpus, constructed by splitting each word on its own line in order to make our
algorithms sort individual words instead of entire lines.  The dataset thus
consists of very many very short strings, with a few outliers due to formatting
markup in the source file.  The dataset also ranks second highest in LCP array
sum size and highest in alphabet size, due to common words appearing hundreds of
times in the text and some loan words using characters not in the English
alphabet.

# Conclusion

Our choice of a fixed alphabet of 256 symbols for MSD radix sort definitely
hurt its performance: less than half of the buckets allocated at each
partitioning step are ever used to hold any strings with every other dataset
besides WORDS.

It was interesting to note how much better the in-place algorithms performed on
the more demanding datasets.  Despite being geared towards high-level
programming, it appears there are still performance gains to be had in
low-level programming. *Insert more stuff here*

# References

[1] T. Peters.  [Python-Dev] Sorting.  From *Python Developers Mailinglist*.
    2002.  Retrieved on 21 Feb 2013.
[2] P. Ferragina, and G. Navarro.  The Pizza & Chili Corpus.
    2007.  Retrieved on 11 Feb 2013.
[3] R. Sinha and A. Wirth.  Engineering burstsort: Towards fast in-place string
    sorting.  In *Experimental Algorithms*, pages 14-27.  Springer, 2008.
