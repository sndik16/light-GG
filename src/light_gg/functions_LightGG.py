#!/usr/bin/env python
# coding: utf-8

# Copyright @2025 Maria Babakhanyan Stone
# 
# # Light-GG
# # Functions

# In[ ]:


#import the necessary packages

#for working with array data
import numpy as np

# for astronomy considerations
from astropy import units as u # to have units
from astropy.coordinates import SkyCoord, Angle # to work with coordinates
from astropy.table import Table # for tables

#for plotting
import matplotlib.pyplot as plt


# In[1]:


def make_LightGG(ra_reference, dec_reference, 
                 delta_ra, delta_dec,
                 max_points=5e7,
                ):
    
    """
    Create a rectangular sky grid and return a SkyCoord object.
    We use human-intuitive inputs and clear design and transparent steps.
    
    Parameters:
    -----------
    ra_reference, dec_reference : float
        Reference point coordinates for the coordinaty system. Units of arcseconds. These are absolute coordinates.
    delta_ra, delta_dec: float
        Interval extent from reference point along each axis. Units of arcseconds. These are extents, not angular separations on the sphere.
    max_points : int
        Safety limit to avoid accidental memory exhaustion.
        
    Returns
    -------
    skycoord : astropy.coordinates.SkyCoord
        Flattened grid of sky coordinates.
    
    """


    # Calculate the number of points ( 1 arcsecond resolution)
    N_points_ra = int(delta_ra) + 1
    N_points_dec = int(delta_dec) + 1


    n_total = N_points_ra * N_points_dec
    if n_total > max_points:
        raise MemoryError(
            f"Grid has {n_total:.2e} points; exceeds limit {max_points:.2e}")

    # Calculate the end-points
    ra_end = ra_reference + delta_ra
    dec_end = dec_reference + delta_dec


    # 1D axes (human-intuitive)
    ra_axis = np.linspace(ra_reference, ra_end, N_points_ra)
    dec_axis = np.linspace(dec_reference, dec_end, N_points_dec)

    # Flattened grid (no 2D intermediate arrays)
    tiled_vector_ra = np.tile(ra_axis, N_points_dec)
    repeated_vector_dec = np.repeat (dec_axis, N_points_ra)


    # SkyCoord catalog. Pairwise matching the above vectors.

    ## We first explicitely write out what is input into the SkyCoord for clarity, in arcsecond unit for each coordinate vertex in the grid

    SkyCoord_RA_1D = np.copy(tiled_vector_ra)*u.arcsec
    SkyCoord_Dec_1D = np.copy(repeated_vector_dec)*u.arcsec


    ## Now we create the sky model or the grid model.
    ## I repeat the units, to be clear
    ## I explicitely state the frame, even though it is the default value, for clarity.

    LightGG_model = SkyCoord(
        ra = SkyCoord_RA_1D,
        dec = SkyCoord_Dec_1D,
        frame = "icrs",
        unit = u.arcsec)

    return LightGG_model


# In[2]:


def LightGG_catalog(grid_model, filename, units):
    
    """
    Save a SkyCoord object as a FITS Table/catalog.
    The Catalog has two columns, one for RA and one for Dec.
    Each row represents the RA and Dec of a single vertex in a grid.
    The units are chosen by the user, degree or arcseconds, for example.
    """
    
    table = Table()
    table["RA"] = grid_model.ra.to(units)
    table["DEC"] = grid_model.dec.to(units)
    
    table.write(filename, format = "fits", overwrite=True)
    
    
    


# In[ ]:


def plot_LightGG(model, units = u.arcsec, max_points=2e6, s=1,):
    
    """
    Visualize a LightGG Sky Grid.
    This shows the points which marke the vertices of the grid tiles.
    This is a good design because it works for small and large grids.
    Avoids crashing for 10M+ points. The grid geometry is clearly shown.
    No WCS or image assumptions. It prioritizes clarity.
    
    Parameters
    ----------
    
    model: the LightGG model (SkyCoord object)
        Grid to visualize.
    units : astropy.units
        Units for plotting axes. For now, arcseconds.
    max_points : int
        Maximum number of points to plot (downsamples if exceeded).
    s: float
        Marker size for scatter plot. Purely for visualization, 
        the vertex of a coordinate grid is a point of infinitesimal size.
    
    """
    
    ra = model.ra.to(units).value
    dec = model.dec.to(units).value
    
    n = ra.size
    if n>max_points:
            idx = np.random.choice(n, int(max_points), replace=False)
            ra = ra[idx]
            dec = dec[idx]
            
    plt.figure(figsize=(10,10))
    plt.scatter(ra, dec, s=s, alpha=0.8)
    plt.xlabel(f"RA[{units}]")
    plt.ylabel(f"Dec[{units}]")
    plt.title('LightGG Sky Grid')
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
    
    
    
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




