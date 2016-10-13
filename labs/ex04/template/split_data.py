# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    
    def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    trainDataLen = round(len(y)*ratio)
    
    trainDataID = random.sample(range(len(y)), trainDataLen)
    
    # USing bool value to obtaint he remainling data for validation data set
    validDataID = np.array(range(len(y))) + 1
    validDataID[trainDataID] = 0
    validDataID = validDataID >0
    
    
    # obtain the trainning data
    trainDataX = x[trainDataID]
    trainDataY = y[trainDataID]
    
    # obtain the validation data
    validDataX = x[validDataID]
    validDataY = y[validDataID]    
    
    return trainDataX,trainDataY, validDataX, validDataY
    
    #raise NotImplementedError
