#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
Light-GG grid utilities.

Memory-efficient construction of 2D coordinate systems using
1D axes and NumPy broadcasting.
"""

import numpy as np
from typing import Optional

def make_axes_from_reference(
    x_reference: float,
    y_reference: float,
    span_x: float,
    span_y: Optional[float] = None,
    step: float = 1.0,
    endpoint: bool=False,
):

    """
    Create 1D coordinate axes for a 2D grid 
    without explicitly allocating a full 2D mesh.

    This function defines a rectangular coordinate system using intuitive, 
    human-readable parameters: a reference point, a total span, and a
    resolution (step size). The resulting axes can be used with NumPy
    broadcasting to emulate 2D grids efficiently.
    
    The abstract core grid is mathematically as:
        x = x0 + i * dx
        y = y0 + j * dy
    The x0, y0 are the reference / origin coordinates.
    The dx, dy are the spacing, while the i and j are the grid indices.
    This can be applied to sky maps, rasters, radar images, 
        agricultural fields, image processing in general.

    All input values are unit-agnostic:
      - x_reference, y_reference, span_x/span_y, step are just numbers.
      - They can represent degrees, meters, pixels, etc.
      
    The same function can be used for:
      - angular coordinates (degrees, arcseconds)
      - Cartesian distances (meters, kilometers)
      - pixel coordinates
      - any other linear unit system

    Parameters
    ----------
    x_reference, y_reference : float
        Origin (lower-left corner) of the grid, in arbitrary units.
    span_x : float
        Total grid width in the same units.
    span_y : float or None, optional
        Total grid height; if None, uses span_x (square grid).
    step : float
        Spacing between samples (resolution) in the same units.
    endpoint : bool
        If False (default), the end value is excluded so spacing stays exactly `step`.

    Returns
    -------
    vector_x : np.ndarray
        1D array of x-axis coordinates.
    vector_y : np.ndarray
        1D array of y-axis coordinates.
        
        
    Notes
    -----
    - This function intentionally avoids creating a 2D meshgrid
      to reduce memory usage.
    - Full 2D coordinate arrays can be generated later if needed
      using broadcasting or numpy.meshgrid.
    - The total number of grid cells is:
            len(vector_x) * len(vector_y)
        
        
        Examples
    --------
    >>> # 1 degree span with 1 arcsecond resolution
    >>> arcsec = 1.0 / 3600.0
    >>> x, y = make_grid_axes(
    ...     x_reference=0.0,
    ...     y_reference=1.0,
    ...     span_x=1.0,
    ...     step=arcsec
    ... )
    >>> x.shape, y.shape
    ((3600,), (3600,))
    """   
    
    if span_y is None:
        span_y = span_x
    if step <= 0:
        raise ValueError("step must be > 0")
    if span_x <= 0 or span_y <= 0:
        raise ValueError("span_x/span_y must be >0 ")
        
    start_x = x_reference
    start_y = y_reference
    
    end_x = start_x + span_x
    end_y = start_y + span_y
    
    if endpoint:
        # include end: may slightly adjust step depending on divisibility
        vector_x = np.arange(start_x, end_x + step, step, dtype = float)
        vector_y = np.arange(start_y, end_y + step, step, dtype = float)
    else:
        # exclude end: exact step
        vector_x = np.arange(start_x, end_x, step, dtype=float)
        vector_y = np.arange(start_y, end_y, step, dtype=float)
        
    return vector_x, vector_y

__all__ = ["make_axes_from_reference"]

