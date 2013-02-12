# String Processing Algorithms - String Sorting

<!-- Author names go here -->

## Introduction

Python implementations of string sorting algorithms for a university
programming course.  The algorithms were tested on four separate
datasets with two differently-sized variants each, and their performance
benchmarks were recorded (results coming soon).  The [pypy](http://pypy.org/)
just-in-time compiler was used in order to reduce runtimes.

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

In order to preserve space and bandwidth, the exact dataset used will not be
hosted with the repository, but access to it will be prepared at a later date.

## Running the algorithms

The Python script `map.py` provides an unified interface to our string sorting
algorithms; see the file itself for further documentation.

We used the `stopwatch` Bash script to measure the performance of our
algorithms; again, see the file itself for exact documentation.  The `testset`
file documents our exact `stopwatch` testing configuration.
