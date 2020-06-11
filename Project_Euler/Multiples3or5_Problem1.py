#!/bin/python3
# Project Euler #1: Multiples of 3 and 5

import sys
import math

def sumMultiple(num):
    sum = 0
    num = num - 1

    # probably rounding off is causing an issue
    quoThree = num//3
    quoFive = num//5
    quoBoth = num//15

    sum = (int(3*((quoThree*(quoThree+1))//2)) + int(5*((quoFive*(quoFive+1))//2))) - int(15*((quoBoth*(quoBoth+1))//2))

    return sum

# Get inputs
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumMultiple(n))

