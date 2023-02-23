#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindrom' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING kalimat as parameter.
#

def palindrom(kalimat):
    # Write your code here
    res = ""
    res_len = 0
    res_dict = {}
    str_len = len(kalimat)
    
    for i in range(str_len):
        # CASE: ODD LEN PALINDROME
        l, r = i, i
        while l >= 0 and r < str_len and kalimat[l] == kalimat[r]:
#             using >= just in case there are more than one palindrome of the current greatest length
            if(r - l + 1) >= res_len:
                res = kalimat[l:r+1]
                res_len = r - l + 1             
            l -= 1
            r += 1
            
        
            
        # CASE: EVEN LEN PALINDROME
        l, r = i, i+1
        while l >= 0 and r < str_len and  kalimat[l] == kalimat[r]:
            if (r - l + 1) >= res_len:
                res = kalimat[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
        
        if(res_len not in res_dict): res_dict[res_len] = [res]
        else: 
            if(res not in res_dict[res_len]): res_dict[res_len].append(res)
            
    max_len = max(res_dict.keys())
    # print(res_dict[res_len])
    
    return (" ".join(res_dict[max_len]))
 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    for N_itr in range(N):
        kalimat = input()

        result = palindrom(kalimat)

        fptr.write(result + '\n')

    fptr.close()
