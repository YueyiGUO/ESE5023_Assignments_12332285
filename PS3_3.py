# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:17:32 2023

@author: Administrator
"""

# # 3 Explore a netCDF dataset


# Load the dataset
pp=xr.open_dataset("precip.mon.total.2.5x2.5.v7.nc",engine="netcdf4")

pp['precip'].mean(dim='time').plot()


# I use the monthly precipitation dataset from NOAA Physical Sciences Laboratory GPCC(Global Precipitation Climatology Centre) from 1891-present,the dataset is calculated from global station data.
# https://psl.noaa.gov/data/gridded/data.gpcc.html#detail





# ## 3.1
# Plot a time series of 'precip' with monthly seasonal cycle removed


# Group data by month
mon_pp = pp.precip.groupby('time.month')
mon_pp.mean(dim='time')

# Apply mean to grouped data, and then compute the anomaly
precip_anom = mon_pp - mon_pp.mean(dim='time')
precip_anom

# Plot global mean anomalies
precip_anom.mean(dim=['lat','lon']).plot()


# Group data by month
mon_pp = pp.precip.groupby('time.month')

# Apply mean to grouped data, and then compute the anomaly
pp_anom = mon_pp - mon_pp.mean()
pp_anom

# Plot global mean anomalies
pp_anom.mean(dim=['lat','lon']).plot()






# ## 3.2 
# Make 5 plots using the dataset

# ### Plot 1:
# Various statistical graphs of the precipitation data

# Mean of precipitation
mon_pp.mean(dim='time').plot()
plt.show()

# Histogram of precipitation
plt.hist(mon_pp.mean(dim='time').values.flatten(), bins=100)
plt.show()

# Variance of the variable over time
mon_pp.var('time').plot()
plt.show()



# ### Plot 2:
# Calculate the monthly max global precipitation in time series

pp.precip.max(dim=['time']).plot()



# ### Plot 3:
# Calculate the monthly max global precipitation in location

pp.precip.max(dim=['lat','lon']).plot()



# ### Plot 4 :
# The precipitation(pp) of last year(2013) and select the area of pp>500

# The last year pp
pp_new = pp.precip.isel(time=-1)
pp_new

# the last year pp where pp is higher than 500
masked_pp_new = pp_new.where(pp_new > 500.0)
masked_pp_new

# Plot 2 panels
fig, axes = plt.subplots(ncols=2, figsize=(19, 6))
pp_new.plot(ax=axes[0], robust=True)
masked_pp_new.plot(ax=axes[1], robust=True)

# Note: the last year of the dataset is 2013.



# ### Plot 5: 
# Calculate and plot zonal mean climatology

precip_clim = pp.precip.groupby('time.month').mean()
precip_clim.mean(dim='lon').transpose().plot.contourf(levels=12, robust=True, cmap='turbo')

