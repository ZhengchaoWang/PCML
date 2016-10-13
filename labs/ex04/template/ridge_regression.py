# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lamb):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    phi_temp = np.dot(np.transpose(tx),tx)
    phi_temp = np.linalg.inv(phi_temp+ lamb*2*len(y) * np.eye(np.shape(phi_temp)[0]))
    phi_temp = np.dot(phi_temp,np.transpose(tx))
    w = np.dot(phi_temp,y)
    
    return w
    #raise NotImplementedError
