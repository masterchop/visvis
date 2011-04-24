# -*- coding: utf-8 -*-
# Copyright (c) 2011, Robert Schroll
#
# Visvis is distributed under the terms of the (new) BSD License.
# The full license can be found in 'license.txt'.

import visvis as vv

def view(viewparams=None, axes=None, **kw):
    """ view(viewparams=None, axes=None, **kw)
    
    Get or set the view parameters for the given axes.
    
    Parameters
    ----------
    viewparams : dict
        View parameters to set.
    axes : Axes instance
        The axes the view parameters are for.  Uses the current axes by default.
    keyword pairs
        View parameters to set.  These take precidence.
    
    If neither viewparams or any keyword pairs are given, returns the current
    view parameters (as a dict).  Otherwise, sets the view parameters given.
    """
    
    if axes is None:
        axes = vv.gca()
    
    if viewparams or kw:
        axes.SetView(viewparams, **kw)
        axes.Draw()
    else:
        return axes.GetView()