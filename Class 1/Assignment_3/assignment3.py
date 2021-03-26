#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:25:00 2021

@author: santi
"""

import numpy as np

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def partitionFirst(A, leftBound, rightBound):
    counter = rightBound-1
    p = A[leftBound]
    i = leftBound + 1
    for j in range(i, rightBound):
        if A[j] < p:
            A = swap(A,i,j)
            i += 1
    A = swap(A, leftBound, i-1)
    pIndex = i-1
    return A, pIndex, counter

def quickSortFirstElement(arr):
    n = len(arr)
    if n < 2:
        return arr,0
    else:
        arr, pIndex, counter = partitionFirst(arr, 0, n)
        leftArr, counter1 = quickSortFirstElement(arr[0:pIndex])
        rightArr, counter2 = quickSortFirstElement(arr[pIndex+1:n])
        return leftArr + [arr[pIndex]] + rightArr, counter+counter1+counter2



def quickSortLastElement(arr):
    n = len(arr)
    if n < 2:
        return arr,0
    else:
        arr = swap(arr, 0, n-1)
        arr, pIndex, counter = partitionFirst(arr, 0, n)
        leftArr, counter1 = quickSortLastElement(arr[0:pIndex])
        rightArr, counter2 = quickSortLastElement(arr[pIndex+1:n])
        return leftArr + [arr[pIndex]] + rightArr, counter+counter1+counter2
    

def pElement(arr, n):
    if n%2 == 0 :
        elements =[arr[0],arr[(n//2)-1],arr[-1]]
        return arr.index(((sorted(elements))[1]))
    else:
        elements = [arr[0], arr[(n//2)], arr[-1]]
        return arr.index(((sorted(elements))[1]))

    

def quickSortMiddle(arr):
    n = len(arr)
    if n < 2:
        return arr,0
    else:
        p = pElement(arr,n)
        arr = swap(arr, 0, p)
        arr, pIndex, counter = partitionFirst(arr, 0, n)
        leftArr, counter1 = quickSortMiddle(arr[0:pIndex])
        rightArr, counter2 = quickSortMiddle(arr[pIndex+1:n])
        return leftArr + [arr[pIndex]] + rightArr, counter+counter1+counter2


arrComplex = list(np.loadtxt(whereverYouSavedIt, dtype = "int"))
"""BE SUPERCAREFUL !! Launch each function below separetely or they will alter with the input and only the first call would be correct
   or make sure you use a copied version of the list using list[:]"""
#print(quickSortFirstElement(arrComplex)[1])   
#print(quickSortLastElement(arrComplex)[1])
#28 vs 21 pour 10 ; 582 vs 502 pour 100; 10313 vs 9735
    
    