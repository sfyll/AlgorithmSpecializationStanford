#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:21:40 2021

@author: santi
"""

def karatsuba(x,y, base=10):
    #if number < 10 quicker to simply multiply
    if(x<10 or y<10):
        return x*y
    
    #Calculate size of the numbers
    length = max(len(str(x)), len(str(y)))
    m2 = length//2

    #split the digits sequence in the middle
    power = base**m2
    a = x // power
    b = x % power
    c = y // power
    d = y % power
    #recursive calls to number with half the size
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    e = karatsuba(a+b, c+d) - ac - bd
    return int(base**(2*m2) *ac + (base ** m2) * e +bd)
    
        
a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(a,b))