#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'tebakCangkir' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER T
#  3. INTEGER P
#  4. 2D_INTEGER_ARRAY posisi
#

def tebakCangkir(N, T, P, posisi):
    # First initialize the 'cups' with zero arrays
    cups = [0 for i in range(N)]
    # Then mark the cup with the dice with a 1 value
    cups[P-1] = 1
    # Then loop through the arrays of position
    for pos in posisi:
        pos1 = pos[0] - 1
        pos2 = pos[1] - 1
        # pop
        popped_val = cups.pop(pos1)
        #insert
        cups.insert(pos2, popped_val)
    
    for idx, cup in enumerate(cups):
        if cup == 1:
            return idx + 1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    T = int(first_multiple_input[1])

    P = int(first_multiple_input[2])

    posisi = []

    for _ in range(T):
        posisi.append(list(map(int, input().rstrip().split())))

    result = tebakCangkir(N, T, P, posisi)

    fptr.write(str(result) + '\n')

    fptr.close()
