# -*- coding: utf-8 -*-
# Copyright (c) 2010, Almar Klein
#
# Visvis is distributed under the terms of the (new) BSD License.
# The full license can be found in 'license.txt'.

import visvis as vv
import numpy as np

def hist(data, bins=10, range=None, normed=False, weights=None, **kwargs):
    """ hist(data, bins=10, range=None, normed=False, weights=None, **kwargs)
    
    Make a histogram plot of the data. Uses np.histogram (new version) 
    internally. See its docs for more information. 
    
    kwargs are given to the plot function.
    
    """
    
    # let numpy do the work
    if np.__version__ < '1.3':
        values, edges = np.histogram(data, bins, range, normed, weights, new=True)
    else:
        values, edges = np.histogram(data, bins, range, normed, weights)
    
    # the bins are the left bin edges, let's get the centers
    range = __builtins__['range']
    centers = np.empty(values.shape, np.float64)
    for i in range(len(values)):
        centers[i] = (edges[i] + edges[i+1]) * 0.5
    
    # plot
    return vv.plot(centers, values, **kwargs)
    
if __name__ == '__main__':
    data = np.random.normal(7,2,size=(100,100))
    hist(data)
