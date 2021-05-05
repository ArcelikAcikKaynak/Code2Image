# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:11:44 2020

@author: Zeki Bilgin
"""


import pycparser
import csv
import h5py
import numpy as np
from pycparser import c_parser, c_ast

               
def bfs(root):
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    tot = 0 
    tottree = 1
    visited.append((root,0))
    queue.append((root,0))
    level = 0
    maxchildrennode = 0
    maxchildrenlevel = 0
    depth = 0
    childstat = dict.fromkeys(range(61),0)
    childstat[0] = 1

    while queue:

        s = queue.pop(0) 

        current_level = s[1]
        maxchildrennode = max(maxchildrennode, len(s[0].children()))
        depth = max(depth,current_level)
        tottree = tottree + len(s[0].children())
        if current_level == level: # proceed on the same level
            tot = tot + len(s[0].children())      
        else:
            level = current_level 
            maxchildrenlevel = max(maxchildrenlevel, tot)
            childstat[level] = max(childstat[level], tot)      
            tot = len(s[0].children())
            
        for neighbour in s[0]:
            if neighbour not in visited:
                visited.append((neighbour,current_level+1))
                queue.append((neighbour,current_level+1))  
       
    return maxchildrennode, maxchildrenlevel, depth, tottree, childstat