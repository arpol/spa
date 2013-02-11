String Processing Algorithms - String Sorting
=============================================

String processing algorithm implementations in Python for a university programming course. The following implementation includes string sorting algorithms done in Python, with various approaches taken to string abstraction, recursion, and input partitioning. 

The algorithms were tested with various test materials, and the results (running times) were recorded.

All tests were performed using [pypy](http://pypy.org/) Just-In-Time compiler for Python, in order to obtain faster running times.

Team
----

* name 1
* name 2
* name 3?

Test material
-------------

The test material for the algorithm was originally obtained from http://pizzachili.dcc.uchile.cl/texts.html. In addition the list of URL-strings was obtained from: ???

The sources used were in particular:
    
* [PROTEINS](http://pizzachili.dcc.uchile.cl/texts/protein/) - protein sequences
* [DNA](http://pizzachili.dcc.uchile.cl/texts/dna/) - DNA snippets  
* [ENGLISH](http://pizzachili.dcc.uchile.cl/texts/nlang/) - Concatenated English texts (normal language)
* [URLs](http://???) - URL database

Before running the sorting algorithms through the above test material, the test material was normalized by:
    
1. Separating each string with a `NEWLINE` character
2. Appending a `NEWLINE` character to the end of the file

Algorithms
----------

### MSD Radixsort

Implemented by:

### Burst sort

Implemented by:

### Multi-key quicksort

Implemented by:

### Ternary Quicksort (string comparison)

Implemented by:
    
Simple Ternary Quicksort implementation using recursive sorting function. String comparisons done using standard Python comparison operators (<,<=,>,=>,==)

### Quicksort (character comparison)

Implemented by:

String Quicksort implementation based on iterating over the position of the currently compared character. Recurssion implemented using stack

Shares pivot function with Ternary Quicksort

Running the algorithms
----------------------
### Individual run using *map.py*

Using the following syntax: `./map.py radixsort:msd dataset.txt > sorted.txt`

The above command tells `map.py` to execute function `msd()` from file `radixsort.py` with an `iterable` list obtained from `dataset.txt` as an argument

### Batch run using *stopwatch* shell script

When performing the test, a batch run using a `stopwatch` shell-script is more convenient. 
This is done using the following syntax: `./stopwatch testset results.csv 2> totaltime`

`stopwatch` goes through all testing material and sorting functions in series, and runs each function with each possibly type of input

`stopwatch` is configured This is done by specifying the paths to the dataset in the file `testset` (last part)

