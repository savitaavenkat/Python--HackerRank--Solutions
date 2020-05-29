#!/bin/python3
# Author: Savitaa Venkateswaran
# Date code accepted for submission on hackerrank: May 28th 2020
# Difficulty: MEDIUM
# Problem from HackerRank: https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    count = []
    processed = []
    freq = 0

    for i in range(len(queries)):
        length = len(strings)
        index = []

        if length == 0:
            if str(queries[i]) in processed:
                val = processed.index((str(queries[i])))
                freq = count[val]
                
        else:
            for j in range(length):
                if str(queries[i]) in processed:
                    val = processed.index((str(queries[i])))
                    freq = count[val]
                    break

                if str(queries[i]) == str(strings[j]):
                    freq += 1
                    index.append(strings[j])

            if len(index) > 0:
                for k in index:
                    strings.remove(k)

        count.append(freq)
        processed.append(str(queries[i]))
        freq = 0

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

