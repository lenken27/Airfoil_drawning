# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:55:09 2019

@author: Emre
"""

import math
import numpy as np
import matplotlib.pyplot as plt
ascii
import os
import glob

                                    #Part A
# =============================================================================
def normalize(x,y,name):
        """
        The Coordinates are fitting in definited interval
        especially in x coordinates start from 1 to 0 then from 0 to 1.
        
        arg: two arrays of x and y.
        
        return: normalized x and y values
        """
        x=airfoil[:,0]/x[0]
        y=airfoil[:,1]/x[0]
        # make the zero of the x coordinates
        if len(x)%2==0:
            x[int((len(x))/2)-1]=0   #for dual total number of points
        elif len(x)%2!=0:   
            x[int((len(x))/2)]=0   #for single total number of points 
        xnew=np.asarray([x,y])
        xnew=np.transpose(xnew)
        np.savetxt('C:/Users/Toshıba/Desktop/figures/datas/'+name[:-2]+'.txt',xnew)
        return x, y
# =============================================================================