#!/bin/sh
printf '%-11s  %-26s  %-33s  %s\n' \
        environment function input time
parallel \
    'time=$((time {1} map.py {2} {3} > /dev/null) 2>&1)
     if [ $? -ne 0 ] ; then
         time=$(echo "$time" | tail -n 5 | head -n 1)
     else
         time=$(echo "$time" | sed -n 3p | cut -f 2)
     fi
     printf "%-11s  %-26s  %-33s  %s\n" $status {1} {2} {3} "$time"' \
    ::: pypy \
        python2 \
        python3 \
    ::: sorted \
        radixsort:msd \
        quicksort:TernaryQuickSort \
        quicksort:QuickSort \
    ::: dataset/*MB
