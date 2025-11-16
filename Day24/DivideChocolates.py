from os import *
from sys import *
from collections import *
from math import *

def getMaximumSweetness(arr, k):

    def canDivide(target):
        pieces = 0
        total = 0
        for s in arr:
            total += s
            if total >= target:
                pieces += 1
                total = 0
        return pieces >= (k + 1)   

    low = 1
    high = sum(arr)
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if canDivide(mid):
            answer = mid
            low = mid + 1   
        else:
            high = mid - 1  

    return answer
