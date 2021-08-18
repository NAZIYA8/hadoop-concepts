#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
current_word = None
current_count = 0
word = None
  
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word, count = line.split('\t',1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so skip this line
        continue
    if current_word == word:
 		  current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
  
# printing last word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
