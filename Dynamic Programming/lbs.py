from os import *
from sys import *
from collections import *
from math import *

def longestBitonicSequence(arr, n):

    left = [1 for _ in range(n)]
    right = [1 for _ in range(n)]
    bitonic = [1 for _ in range(n)]

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and left[i] < 1 + left[prev]:
                left[i] = 1 + left[prev]

    for i in reversed(range(n)):
        for prev in reversed(range(i+1,n)):
            if arr[i] > arr[prev] and right[i] < 1 + right[prev]:
                right[i] = 1 + right[prev]
    
    for i in range(n):
            bitonic[i] = left[i] + right[i] - 1

    return max(bitonic)