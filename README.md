# String Processing Algorithms - String Sorting

## Introduction

Python implementations of string sorting algorithms for a university
programming course.  The algorithms were tested on four separate
datasets with two differently-sized variants each, and their performance
benchmarks were recorded.  The [pypy](http://pypy.org/) just-in-time
compiler was used in order to reduce runtimes on the more complex inputs.

## Implemented algorithms

* MSD radix sort (radixsort.py)
* Burst sort (burst.py)
* In-place multikey quicksort, implemented as a helper function for
  burst sort (mkqsort.py)
* Multikey quicksort (quicksort.py)
* Ternary quicksort (quicksort.py)

## Test data

The test data consisted of the
[PROTEINS](http://pizzachili.dcc.uchile.cl/texts/protein/),
[DNA](http://pizzachili.dcc.uchile.cl/texts/dna/) and
[ENGLISH](http://pizzachili.dcc.uchile.cl/texts/nlang/) datasets from the
[Pizza&Chili Corpus](http://pizzachili.dcc.uchile.cl/texts.html), in addition
to a set of URLs (source to be filled in.)  A 100MB and a 200MB sample of each
dataset was used.  The ENGLISH datasets were not used as-is, but with each
word split on its own line, in order to make the algorithms sort individual
words and not entire lines.

## Results

Two timing result sets are included in the repository: `times_11.2._16.57`
and `times-11.2._17.22`, of which the latter is the "official" one.  Though
the algorithm implementations were not changed between these two runs, the
former contains one failed burstsort run (marked with a `!` in the leftmost
column, due to a missing newline at the end of `proteins.100MB`) and only
the userspace execution time in seconds; though we will likely ignore the
`real` column in `times-11.2._17.22`, as the execution time of our
algorithms is more relevant to our analysis than the time the processor
spent juggling jobs or reading files.

## Running the algorithms

The Python script `map.py` provides an unified interface to our string sorting
algorithms; see the file itself for further documentation.

We used the `stopwatch` Bash script to measure the performance of our
algorithms; again, see the file itself for exact documentation.  The `testset`
file documents our exact `stopwatch` testing configuration.
