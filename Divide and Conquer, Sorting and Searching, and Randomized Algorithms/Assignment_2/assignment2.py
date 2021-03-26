#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:38:52 2021

@author: santi
"""
import numpy as np

def mergeAndCount(L,R):
    inversions = 0
    if(len(L) != 0 and len(R) != 0):
        i = j = k = 0
        output = []
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                output.append(L[i])
                i += 1
            else:
                output.append(R[j])
                j += 1
                inversions += (len(L)-i)
        while i < len(L):
            output.append(L[i])
            i += 1 
        while j < len(R):
            output.append(R[j])
            j += 1
    return output, inversions


def sortAndCount(arr):
    if(len(arr) == 1):
        return arr, 0
    else:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        print(L,R)
        (L, inversionsL) = sortAndCount(L)
        (R, inversionsR) = sortAndCount(R)
        (sortedArr, inversionsSplit) = mergeAndCount(L,R)
        
    return (sortedArr, inversionsL+inversionsR+inversionsSplit)

#arr = np.loadtxt(fileDirection, dtype = "int")
arr = [5,3,8,9,1,7,0,6,2,4]
#arr = [1,3,5,2,4,6] 
print(arr)
print(sortAndCount(arr))