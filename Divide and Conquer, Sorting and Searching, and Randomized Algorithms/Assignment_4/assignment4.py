#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:50:15 2021

@author: santi
"""
 
import numpy as np
import random as rd
import copy
 
 
 
def MinCut(graphDictInput):
    while(len(graphDictInput) > 2):
       
        #randomely select two vertex
        pointerA = rd.choice(list(graphDictInput.keys()))
        pointerB = rd.choice(graphDictInput[pointerA])
 
        #Call function to contract the edge
        graphDictInput = graphContractor(graphDictInput, pointerA, pointerB)
 
    return len(graphDictInput[list(graphDictInput.keys())[0]])
 
def graphContractor(graphDictInput, pointerA, pointerB):
    for nodes in graphDictInput[pointerB]:
        if nodes != pointerA:
            graphDictInput[pointerA].append(nodes) #this node is not a self-loop we can append it to vertex A
            graphDictInput[nodes].append(pointerA) #and we can append the other end of the edge to its node
        graphDictInput[nodes].remove(pointerB) #vertex B has been absorbed, it should not remain as end point of remaining vertex
   
    del graphDictInput[pointerB] #delete absorbed vortex
    return graphDictInput
 
 
input_file = "input file location here"
def MinCutCaller(input_file, N):
    """Get the Input"""
    with open(input_file, 'r') as data:
        line = data.read().strip().split("\n")
   
    graphDict = {} #we will store information on the node in the index, i.e. index 0 = node 1
    for element in line:
        line_list = list(map(int, element.strip().split("\t")))
        graphDict[line_list[0]] = (line_list[1:])
    
    """get the min cut """   
    cut = []
    for i in range(N):
        graphDictCopy = copy.deepcopy(graphDict)
        cut.append(MinCut(graphDictCopy))
       
    return min(cut)
 
print(MinCutCaller(input_file, 100))
