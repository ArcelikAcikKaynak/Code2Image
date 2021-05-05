# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:31:51 2020

@author: Zeki Bilgin
"""

#We read data (i.e. functions from the Draper dataset), generate image representation, rename and put them either in folder 0 (i.e. non-vulnerable) or in folder 1 (i.e. vulnerable) for each vulnerability type. 

import pycparser
import csv
import h5py
import numpy as np
from pycparser import c_parser, c_ast
from image_representation import ast2img, rowdelete, columndelete
from treetraversal import bfs
from numpy import savez_compressed
from numpy import save

parser = c_parser.CParser()

condition1 = True
while condition1:
    secim = int(input("Make your choice 1:training dataset, 2:validation dataset, 3:test dataset "))
    if secim == 1:
        filename = r"VDISC_train.hdf5"
        folder='train'
        condition1 = False
    elif secim == 2:
        filename = r"VDISC_validate.hdf5"
        folder='validate'
        condition1 = False
    elif secim == 3:
        filename = r"VDISC_test.hdf5" 
        folder='test'
        condition1 = False


        
        
weights ={}
keys = []
with h5py.File(filename, 'r') as f:
    print("Keys: %s" % f.keys())
    for key in f.keys():
        print(f[key].name)
    a_group_key = list(f.keys())[-1]
    a_group_key119 = list(f.keys())[0]
    a_group_key120 = list(f.keys())[1]
    a_group_key469 = list(f.keys())[2]
    a_group_key476 = list(f.keys())[3]
    a_group_keyother = list(f.keys())[4]

    # Get the labels (True:vulnerable  False: Not vulnerable)
    dataCWE119 = list(f[a_group_key119])
    dataCWE120 = list(f[a_group_key120])
    dataCWE469 = list(f[a_group_key469])
    dataCWE476 = list(f[a_group_key476])
    dataCWEother = list(f[a_group_keyother])
    print("Reading the labels is completed. Now we read data")
    #Get the data (source codes)
    data = list(f[a_group_key])
    print("Reading the data is completed")
    
    
parsedno= 0
skip = 0

height = 4096
width = 1024
delta2 = 5


images = []
labels = []


for i in range(0, len(data)):
    if i%1000 == 0:
        print("Reading the function no: ",i, "out of ", len(data))
        
    if (dataCWE119[i] == False) and (dataCWE120[i] == False) and (dataCWE469[i] == False) and (dataCWE476[i] == False) and (dataCWEother[i] == False):
        skip = skip + 1
        if skip%3 != 0:  # Soften class imbalance by ignoring some functions which are false (not vulnerable) for all categories
            continue   
    if secim == 1:
        if i == 17200 or i == 170342 or i == 433610 or i == 495198 or i == 503849 or i == 534485 or i == 583727 or i == 940298: #indexes of problematic functions in train set
            continue
    elif secim == 2:
        if i == 6308 or i == 104403: #These are indexes of the problematic functions in validate dataset, they make pycparser frozen while generating AST. So, we skip them.   
            continue
    elif secim == 3:
        if i == 80792 or i == 93763 : # There are problematic functions in test dataset
            continue

    code = r"""{0}""".format(data[i])

    try:        
        AST = parser.parse(code, filename='<none>')
        parsedno = parsedno + 1 
        _, maxnodeatlevel, depth, totchild , levelbasemaxchild = bfs(AST.ext[0])
        height = 2*sum(levelbasemaxchild[k]+1 for k in range(depth+1)) + 2*levelbasemaxchild[depth]
        width = totchild*delta2
        image = ast2img(AST.ext[0], height, width,3, delta2,levelbasemaxchild)
        image2 = rowdelete(image, height, width)
        image3 = columndelete(image2)
        label = [dataCWE119[i],dataCWE120[i],dataCWE469[i], dataCWE476[i], dataCWEother[i]]
        labelbinary = [0 if s == False else 1 for s in label]
        ## SELECT CORRECT CATEGORY 
        category = str(labelbinary[1])

        if secim == 1:
            save('imagesbinary120/train/{}/f{}.npy'.format(category,parsedno), image3)           
        elif secim == 2:
            save('imagesbinary120/validate/{}/f{}.npy'.format(category,parsedno), image3)
        elif secim == 3:
            save('imagesbinary120/test/{}/f{}.npy'.format(category,parsedno), image3)
    except Exception as exc:
        pass    
