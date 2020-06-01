#!/bin/python3
# Competition: Hack the interview IV 101 U.S
# Author: Savitaa Venkateswaran
# Difficulty level: MEDIUM
 
import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER d
#

def check_substring(substring_dlength, substring, min_changes):
    if "1" in substring_dlength:
        return min_changes, substring_dlength
    else:
        substring_dlength = str(str(substring[1:])+str("1"))
        min_changes += 1
        return min_changes, substring_dlength

def minimumMoves(s, d):
    # Write your code here
    count = 0
    index = d+1
    min_changes = 0
    
    string_length = len(s)
    min_ones  = int(string_length/int(d))
    if string_length == str(s).count('0'):
        return min_ones
    
    substring = s[:d]
    
    min_changes, substring = check_substring(substring, substring, min_changes)
    
    while count < len(s)-d: 
        substring_dlength = str(str(substring[1:])+str(s[index-1]))
        min_changes, substring = check_substring(substring_dlength, substring, min_changes)
        index += 1
        count += 1

    return min_changes
                                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()

