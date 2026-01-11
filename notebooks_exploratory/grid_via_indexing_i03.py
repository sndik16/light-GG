#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Light-GG
# Memory saving algorithm to create a coordinate system (2D), but with human-intuitive inputs


# In[2]:


#import the necessary packages
import numpy as np


# Create a coordinate grid

# In[3]:


# We use units of angles
delta_angle = 1 # units in degrees
x_reference = 0 # units in degrees
y_reference = 1 # units in degrees


# In[4]:


# Calculate start and End from reference point
start_x = x_reference
start_y = y_reference

end_x = start_x + delta_angle
end_y = start_y + delta_angle


# In[5]:


# Number of points, we do the same for a square grid
# For 1 arcsecond resolution, we input the number of arcseconds in a degree
N = delta_angle * 60 * 60 # number of points is the number of arcseconds
N_points_x = N
N_points_y = N


# In[6]:


# creating the axes with evenly spaced coordinate spots
vector_x = np.linspace (start_x, end_x, N_points_x)
vector_y = np.linspace (start_y, end_y, N_points_y)


# In[7]:


# Use broadcasting to mimic the behaviour of a grid, without actually making a 2D Numpy Grid


# In[8]:


N_tiles = N*N
print('The total number of tiles is ',N_tiles)


# In[10]:


vector_x[:3]


# In[11]:


vector_y[:3]


# In[ ]:




