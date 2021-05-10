# Code2Image: Intelligent Code Analysis by Computer Vision Techniques and Application to Vulnerability Prediction

Paper: https://arxiv.org/abs/2105.03131

## Source Code Representation
- **demo.py:** Demonstration of AST-based image representation of source code with a sample C file (main.c) 
- **nodeencoding.py:** Encodes AST tokens to RGB values 
- **treetraversal.py:** Tree traversal over AST 
- **image_representation.py:** Generates image representation of source code in numpy matrice format  

## Vulnerability Prediction
- **readdraper.py:** Read data (i.e. function source codes from the Draper dataset (https://osf.io/d45bw/)), generate image representation, rename and put them either in folder 0 (i.e. non-vulnerable) or in folder 1 (i.e. vulnerable) for each vulnerability type. 
- **copyfiles.sh:** Creates multiple copies of samples for oversampling to deal with data imbalance 
- **FCNdense.py:** Convolutional neural network (CNN) architecture 
- **generator.py:** Generator for loading and processing images 
- **train.py:** Script for training the model
- **plotPR.py:** Plots precision-recall curve and calculates several performance metrics 

The Pretrained_Models folder contains a pretrained model for each vulnerability type   
