#!/usr/bin/env python
"""mapper.py"""

# input comes from STDIN (standard input)
import sys
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output)
        print('%s\t%s' % (len(word), 1))
