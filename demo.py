# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:42:55 2020

@author: Zeki
"""


import numpy as np
import pycparser
import csv
from pycparser import c_parser, c_ast
from nodeencoding import map
from treetraversal import bfs
import matplotlib.pyplot as plt


# This script generates AST-based image representation of code 


def ast2img(root, x,y,z, deltab, childnumbers):
    img = np.full((x, y,z), 255, dtype=int)  #blank image initilization
    delta2 = deltab #interval, i.e. the number of pixels between nodes on the same level
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    tot = 0 
    visited.append((root,0,0,0)) # second element is the level, the third element is its parent's level, the fourth is its parents horizontal position
    queue.append((root,0,0,0))
    previous = (0,0)
    placehorizontal = 0
    level = 0
     

    childno = 0
    nodechildno = 0
    flag = 0
    flag2 = True
    last = 0

    while queue:

        s = queue.pop(0) 

        current_level = s[1]

        index0 = 2*sum(childnumbers[k]+1 for k in range(current_level+1))
        if current_level == 0: # i.e. root
            childno = childno + 1
            img[index0][childno*delta2] = map(s[0]) 
            img[index0][childno*delta2-1] = map(s[0])
            img[index0][childno*delta2+1] = map(s[0])
            horizontal = childno*delta2
            
        
        elif current_level == level: # we are proceeding on the same level

            childno = childno + 1
            if s[3] <= childno*delta2: # s[3] is the horizontal location of the parent node
                index = max(childno*delta2,placehorizontal+delta2)
                
                if index0 < x: #draw only if it is in the image frame  
                    if index < y:
                        img[index0][index] = map(s[0])
                    if index-1 < y:
                        img[index0][index-1] = map(s[0])
                    if index+1 < y:
                        img[index0][index+1] = map(s[0])
                horizontal = index
                flag = 0
                
            else:
                if (s[2],s[3]) == previous: # if the previous node is my sibling
                    flag = flag + 1
                    index = max(s[3] + flag*delta2,placehorizontal+delta2)
                    
                    if index0 < x: #draw only if it is in the image frame  
                        if index < y:
                            img[index0][index] = map(s[0])
                        if index-1 < y:
                            img[index0][index-1] = map(s[0])
                        if index+1 < y:
                            img[index0][index+1] = map(s[0])
                    horizontal = index

                else:
                    index = max(s[3],placehorizontal+delta2)
                    if index0 < x:
                        if index < y:    
                            img[index0][index] = map(s[0])
                        if index-1 < y:
                            img[index0][index-1] = map(s[0])
                        if index+1 < y:
                            img[index0][index+1] = map(s[0])
                    flag = 0
                    horizontal = index
            
        
        else:  # we pass to a new level 
            level = current_level
            childno = 1
            flag = 0
            
            if s[3] <= childno*delta2:
                index = childno*delta2
                if index0 < x:
                    if index < y:                            
                        img[index0][index] = map(s[0])
                    if index-1 < y: 
                        img[index0][index-1] = map(s[0])
                    if index+1 < y: 
                        img[index0][index+1] = map(s[0])
                horizontal = index
                flag = 0
                
            else:
                if (s[2],s[3]) == previous:
                    flag = flag + 1
                    #print("flag ", flag)
                    index = s[3] + flag*delta2
                    if index0 < x:
                        if index < y:  
                            img[index0][index] = map(s[0])
                        if index-1 < y: 
                            img[index0][index-1] = map(s[0])
                        if index+1 < y: 
                            img[index0][index+1] = map(s[0])

                    horizontal = index

                else: 
                    index = max(s[3],placehorizontal)
                    if index0 < x:
                        if index < y: 
                            img[index0][index] = map(s[0])
                        if index-1 < y: 
                            img[index0][index-1] = map(s[0])
                        if index+1 < y:
                            img[index0][index+1] = map(s[0])
                    flag = 0
                    horizontal = index
        
        
        # draw lines between the nodes
        if current_level != 0:
            if (s[2],s[3]) != previous: 
                
                for i in range(1,childno*2):
                    if index0-i < x and horizontal < y:
                        img[index0-i][horizontal] = 0 
            else:
                for i in range(1,3):
                    if index0-i < x and horizontal < y:
                        img[index0-i][horizontal] = 0 
                
                
            if s[3] > horizontal:
                direction = 1
            elif s[3] == horizontal:
                direction = 0  
            else:
                direction = -1
            last = horizontal 
            flag2 = True
            for i in range(abs(placehorizontal-horizontal)):
                if (s[2],s[3]) == previous:
                    if flag2:
                        flag2 = False
                    if index0-2 < x and horizontal+direction*i < y:
                        img[index0-2][horizontal+direction*i] = 0 
                    last = horizontal+direction*(i+1)
                else:
                    if index0-childno*2 < x and horizontal+direction*i < y:
                        img[index0-childno*2][horizontal+direction*i] = 0 
                    last = horizontal+direction*(i+1)
            
            if (s[2],s[3]) != previous and s[3] < horizontal:
                for i in range(abs(s[3]-horizontal)):
                    if index0-childno*2 < x and horizontal+direction*i < y:
                        img[index0-childno*2][horizontal+direction*i] = 0 
                    last = horizontal+direction*(i+1)
                       
            lastver = index0-childno*2
                
            if (s[2],s[3]) != previous: # draw vertical line to parent node
                for i in range(0,abs(index0-2*sum(childnumbers[k]+1 for k in range(current_level))-childno*2)):
                    if lastver-i < x and last < y:
                        img[lastver-i][last] = 0

        for neighbour in s[0]:
            if neighbour not in visited:
                visited.append((neighbour,current_level+1,current_level, horizontal)) # the third and the fourth elements represent location of its parent
                queue.append((neighbour,current_level+1,current_level, horizontal))  
        previous = (s[2],s[3])
        placehorizontal = horizontal
        
    return img


      
def rowdelete(image, h, w):
    imagecompact = np.full((h,w,3), 255, dtype=int)
    k= 0
    for i in range(len(image)-1):    
        temp = image[i] == image[i+1]
        if temp.all():
            continue
        else:
            imagecompact[k] = image[i]
            k = k + 1
            
    for i in range(len(imagecompact)):
        if i > k:
            imagecompact = np.delete(imagecompact,(k), axis=0)
    return imagecompact
    
def columndelete(imagecompact):
    idx = np.argwhere(np.all(imagecompact[..., :] == [255,255,255], axis=0))
    imagecompact2 = np.delete(imagecompact, idx, axis = 1)
    return imagecompact2
    
    

#Example for usage:

parser = c_parser.CParser()

file = r"main.c"
code = open(file, "r")
code2 = code.read()
print(code2,"\n")
AST2 = parser.parse(code2) # AST2 starts with a root node names FileAST which is not an essential node
AST = AST2.ext[0] # we eliminate the node FileAST so that the root of the tree becomes FuncDef node. 
print(AST.show())
_, maxnodeatlevel, depth, totchild , levelbasemaxchild = bfs(AST)
# To visualize the generated image data in png format, the following commands can be used

height = 1024
width = 512
delta2 = 5
image = ast2img(AST, height,width,3, delta2,levelbasemaxchild)

image2 = rowdelete(image, height, width)
image3 = columndelete(image2)

plt.imshow(image3, cmap='Greys')
plt.savefig("visualized_delta2_{}_height{}_width{}_dpi300.png".format(delta2,height,width), dpi=300)
