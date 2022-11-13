import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    count = len(arr)
    for num in arr:
        if num == 0:
            zero_count += 1
        elif num < 0:
            negative_count += 1
        else:
            positive_count += 1
    print(format(positive_count/count,'.6f'))
    print(format(negative_count/count,'.6f'))
    print(format(zero_count/count,'.6f'))
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
