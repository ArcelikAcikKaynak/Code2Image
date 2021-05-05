#!/bin/bash
for filename in train/1/*.npy; do
    for i in {1..5}; do  # set the number of copies. Change based on the imbalance ratio for each vulnerability type separately   
        cp $filename  train/1/$(basename "$filename" .npy)_$i.npy
    done
done