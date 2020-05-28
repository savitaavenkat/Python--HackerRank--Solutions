#!/bin/python3
# Author: Savitaa Venkateswaran
# Date code accepted for submission on hackerrank: May 28th 2020
# Problem from HackerRank: https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=false

# Problem statement:
# ------------------
#A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
#Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
#A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].
#By this logic, we say a sequence of brackets is balanced if the following conditions are met:
#It contains no unmatched brackets.
#The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
#Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

# Function Description:
# ---------------------
#Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.
#isBalanced has the following parameter(s):
#s: a string of bracket

# Input Format:
# -------------
#The first line contains a single integer , the number of strings.
#Each of the next  lines contains a single string , a sequence of brackets.

# Constraints:
# ------------
#All chracters in the sequences ∈ { {, }, (, ), [, ] }.

# Output Format:
# --------------
#For each string, return YES or NO.


# Solution:
# ---------
import math
import os
import random
import re
import sys

# The push function pushes an element into the stack
def push(stack, val, count):
    stack[count] = val
    count -= 1
    
    return stack, count

# The pop function which pops out the most recent element when it encounters a closing brace and checks for an associated opening brace. Depending upon the a matching opening brace prescence the function does the needful//
def pop(stack, val, count, char_dict):
    flag = 0
    key = char_dict[val]
    
    # If closing brace is the only element left in the stack//
    if (count+1) == (len(stack)-1):
        flag = 1
    # If there is a matching opening brace for the closing brace//
    elif stack[count+2] == key:
        # Remove the matching brace from the stack
        del(stack[count+2])
        del(stack[count+1])
        # Append zeroes to the start of the stack inorder to maintain the stack length
        stack.insert(0, 0)
        stack.insert(0, 0)
        # Increment the count pointer to point to the right index
        count += 2   
    # If there is no matching opening brace for the closing brace//      
    elif stack[count+2] != key:
        flag = 1

    return stack, count, flag

# Complete the isBalanced function below.
def isBalanced(s):
    # Character set dictionary
    char_dict = {")": "(", "}" : "{", "]" : "["}
    count = len(s)-1

    # Create and Initialize the stack with all 0s//
    stack = []
    for i in range(len(s)):
        stack.append(0)

    #l = []
    # check len of string if odd - rule out//
    if len(s)%2 != 0:
        return "NO"
    else:
        for iter_val in range(len(s)):
            flag = 0
            val = s[iter_val]
            # Testing purpose
            #l.append(val)

            # Push item into stack
            stack, count = push(stack, val, count)

            # If item is a closing brace, check for a corresponding opening brace
            if val in char_dict:
                stack, count, flag = pop(stack, val, count, char_dict)
                if flag == 1:
                    break
            # To test the correctness of code//
            # if iter_val == 5:
            #     break
            
    if (flag == 0):
        if all([ value == 0 for value in stack]):
            return "YES"
        else:
            return "NO"
    elif flag == 1:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

