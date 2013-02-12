EOS = 10                #String delimiter character code

INS_SORT_THRESHOLD = 8  #Switch to using insertion sort from multikey
                        #quicksort for arrays smaller than this.

BURST_LIMIT = 32768     #Maximum size for the burst trie
                        #containers. About 32k seemed to offer best
                        #speed for large collections of strings on the
                        #test hardware.

#The following are obsolete since manually allocating space for the
#containers could not match the speed of using Python's built-in
#dynamically growing arrays.

CONTAINER_INITIAL_SIZE = 16 
CONTAINER_RESIZE_FACTOR = 8
