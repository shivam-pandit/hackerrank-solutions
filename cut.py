#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    mini=min(arr)
    n=0
    a=[]
    a.append(len(arr))
    while len(arr)>0:
        if mini in arr:
            arr.remove(mini)
        else:
            a.append(len(arr))
            mini=min(arr)

    return a
                

                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
