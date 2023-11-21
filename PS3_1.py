# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:11:29 2023

@author: Administrator
"""

import numpy as np
import pandas as pd
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt

# # 1 Niño 3.4 index

# Load the dataset
ds = nc.Dataset('NOAA_NCDC_ERSST_v3b_SST.nc')

# Extract the SST variable
sst = ds.variables['sst'][:]

# Define the Niño 3.4 region (5N-5S, 170W-120W)
lat_mask = (ds.variables['lat'][:] >= -5) & (ds.variables['lat'][:] <= 5)
lon_mask = (ds.variables['lon'][:] >= 120) & (ds.variables['lon'][:] <= 170)

# Create a 2D mask for the Niño 3.4 region
mask = np.outer(lat_mask, lon_mask)

# Extract the data from the Niño 3.4 region
nino34_region = sst[:, mask]





# ## 1.1
# Compute the monthly climatology
climatology = np.mean(nino34_region, axis=0)

# Compute the anomalies
anomalies = nino34_region - climatology

# Convert the time variable to datetime format
import datetime
time = ds.variables['time'][:]
time_units = ds.variables['time'].units
time_calendar = ds.variables['time'].calendar
dates = nc.num2date(time, units=time_units, calendar=time_calendar)

# Convert dates to year-month format
dates = [datetime.datetime(date.year, date.month, 1) for date in dates]





# ## 1.2 

# Visualize the computed Niño 3.4
plt.figure(figsize=(12, 8))
plt.plot(dates, anomalies)
plt.title('Niño 3.4 Anomalies')
plt.xlabel('Time (Year-Month)')
plt.ylabel('Temperature Anomaly (°C)')
plt.show()

