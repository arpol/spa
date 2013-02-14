# String Processing Algorithms - String Sorting

* Onni Koskinen
* Arturs Polis
* Lari Rasku

## Introduction

This repository contains pure-Python implementations of various string sorting
algorithms designed for a university programming course.  All algorithms were
written from scratch, striving for idiomatic and easily understandable Python
code over low-level or implementation-specific optimizations whenever possible.
In addition, the repository contains some empirical measurements on the performance
of these algorithms.

## Implemented algorithms

* MSD radix sort (radixsort.py, by Lari Rasku)
* Burst sort (burst.py, by Onni Koskinen), plus two fallback sorting algorithms:
  * In-place multikey quicksort (mkqsort.py, by Onni Koskinen)
  * Insertion sort (insertion.py, by Onni Koskinen)
* Multikey quicksort (quicksort.py, by Arturs Polis)
* Ternary quicksort (quicksort.py, by Arturs Polis)

See the specified files for documentation on the algorithms.  With the exception
of insertion sort, all implementations were timed; the insertion sort was excepted as
it is a naive implementation, lacking any optimizations for sorting sequential data.
In its place, the Python builtin `sorted` function (using the
[Timsort](http://en.wikipedia.org/wiki/Timsort) algorithm) was timed to see how well
our implementations measure against highly optimized general-purpose solutions.

## Test data

The timing test data consisted of the
[PROTEINS](http://pizzachili.dcc.uchile.cl/texts/protein/),
[DNA](http://pizzachili.dcc.uchile.cl/texts/dna/) and
[ENGLISH](http://pizzachili.dcc.uchile.cl/texts/nlang/) datasets from the
[Pizza&Chili Corpus](http://pizzachili.dcc.uchile.cl/texts.html), in addition
to a set of URLs from Ranjan Sinha's¹ data² for his original Burstsort paper.
(¹) https://sites.google.com/site/ranjansinha/home 
(²) http://www.cs.mu.oz.au/~rsinha/resources/data/sort.data.zip

A 100MB and a 200MB sample of each dataset was used.  The ENGLISH datasets 
were not used as-is, but with each word split on its own line, in order to
make the algorithms sort individual words and not entire lines.  The
`statistics` file documents some stringological properties of these datasets.

## Timing results

Two timing result sets are included in the repository: `times_11.2._16.57`
and `times-11.2._17.22`, of which the latter is the "official" one.  Though
the algorithm implementations were not changed between these two runs, the
former contains one failed burstsort run (marked with a `!` in the leftmost
column, due to a missing newline at the end of `proteins.100MB`) and only
the userspace execution time; though we will likely ignore the
`real` column in `times-11.2._17.22`, as the execution time of our
algorithms is more relevant to our analysis than the time the processor
spent juggling jobs or reading files.  The times documented in the files
are in seconds.

The [pypy](http://pypy.org) just-in-time compiler was used for running the
tests as it performed nearly an order of magnitude better on larger
datasets than standard CPython, cutting total testing time down drastically.

## Running the algorithms

The Python script `map.py` (by Lari Rasku) provides an unified interface to
our string sorting algorithms; see the file itself for further documentation.

We used the `stopwatch` Bash script (by Lari Rasku) to measure the performance
of our algorithms; again, see the file itself for exact documentation.  The
`testset` file documents our exact `stopwatch` testing configuration.
