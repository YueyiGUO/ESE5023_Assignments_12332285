# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:13:10 2023

@author: Administrator
"""

# # 2 Earth’s energy budget

# load the dataset
TOA = xr.open_dataset("CERES_EBAF-TOA_200003-201701.nc", engine="netcdf4")
TOA.data_vars
#TOA['cldarea_total_daynight_mon']



# ## 2.1 
# Make a plot of the time-mean TOA longwave, shortwave, and solar radiation for all-sky conditions

# Compute the time-mean TOA longwave, shortwave, and solar radiation for all-sky conditions
toa_lw_all_mon = TOA['toa_lw_all_mon'].mean(dim='time')
toa_sw_all_mon = TOA['toa_sw_all_mon'].mean(dim='time')
solar_mon = TOA['solar_mon'].mean(dim='time')
toa_net_all_mon = TOA['toa_net_all_mon'].mean(dim='time')

# Make a plot of the time-mean TOA longwave, shortwave, and solar radiation for all-sky conditions
fig, axes = plt.subplots(ncols=4, figsize=(20, 4))
toa_lw_all_mon.plot(ax=axes[0])
axes[0].set_title('TOA Longwave')
toa_sw_all_mon.plot(ax=axes[1])
axes[1].set_title('TOA Shortwave')
solar_mon.plot(ax=axes[2])
axes[2].set_title('Solar Radiation')
toa_net_all_mon.plot(ax=axes[3])
axes[3].set_title('TOA_net_flux')
plt.tight_layout()
plt.show()

# Add up the three variables above and verify (visually) that they are equivalent to the TOA net flux
net_flux = toa_lw_all_mon + toa_sw_all_mon + solar_mon
net_flux.plot()
plt.title('TOA Net Flux')
plt.show()

# the sum of TOA longwave, shortwave, and solar radiation for all-sky conditions is not equivalent to the TOA net flux.





# ## 2.2
# Calculate and verify that the TOA incoming solar, outgoing longwave, and outgoing shortwave approximately match up with the cartoon above

# Calculate the global mean values
glb_mean_toa_lw_all_mon = toa_lw_all_mon.mean(dim=['lat', 'lon']).values
glb_mean_toa_sw_all_mon = toa_sw_all_mon.mean(dim=['lat', 'lon']).values
glb_mean_solar_mon = solar_mon.mean(dim=['lat', 'lon']).values

print(f'Global mean TOA longwave radiation: {glb_mean_toa_lw_all_mon}')
print(f'Global mean TOA shortwave radiation: {glb_mean_toa_sw_all_mon}')
print(f'Global mean solar radiation: {glb_mean_solar_mon}')

# As the cartoon showes, incoming solar radiation(340.4) = total reflected solar radiation(99.9) + total outgoing infrared radiation(239.9) + net absorbed(0.6)
# 
# My calculation outputs are as given above, Global mean TOA longwave radiation(224.7551727294922) ≈ 239.9，Global mean TOA shortwave radiation(102.30432891845703) ≈ 99.9, and Global mean solar radiation(298.3305358886719) ≈ 340.4
# 
# Therefore, the TOA incoming solar, outgoing longwave, and outgoing shortwave approximately match up with the cartoon above.





# ## 2.3
# Calculate and plot the total amount of net radiation in each 1-degree latitude band.

total_net_radiation = net_flux.sum(dim='lon')
total_net_radiation.plot()
plt.ylabel('Net Radiation (W/m²)')
plt.title('Total Net Radiation in Each 1-Degree Latitude Band')
plt.show()





# ## 2.4
# Calculate and plot composites of time-mean outgoing shortwave and longwave radiation for low and high cloud area regions. 

# define low cloud area as ≤25% and high cloud area as ≥75%
low_cloud_area = TOA['cldarea_total_daynight_mon'] <= 25
high_cloud_area = TOA['cldarea_total_daynight_mon'] >= 75

# time-mean for low and high cloud area regions
low_cloud_sw = TOA['toa_sw_all_mon'].where(low_cloud_area).mean(dim='time')
high_cloud_sw = TOA['toa_sw_all_mon'].where(high_cloud_area).mean(dim='time')
low_cloud_lw = TOA['toa_lw_all_mon'].where(low_cloud_area).mean(dim='time')
high_cloud_lw = TOA['toa_lw_all_mon'].where(high_cloud_area).mean(dim='time')

lowcld_sl = low_cloud_sw + low_cloud_lw
highcld_sl = high_cloud_sw + high_cloud_lw

# plot low and high cloud composites outgoing shortwave and longwave radiation
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(8, 8))
low_cloud_sw.plot(ax=axs[0, 0])
axs[0,0].set_title('shortwave, low cloud')
high_cloud_sw.plot(ax=axs[0, 1])
axs[0,1].set_title('shortwave, high cloud')
low_cloud_lw.plot(ax=axs[1, 0])
axs[1,0].set_title('longwave, low cloud')
high_cloud_lw.plot(ax=axs[1, 1])
axs[1,1].set_title('longwave, high cloud')
lowcld_sl.plot(ax=axs[2,0])
axs[2,0].set_title('the composite of sw and lw, low cloud')
highcld_sl.plot(ax=axs[2,1])
axs[2,1].set_title('the composite of sw and lw, high cloud')
plt.tight_layout()
plt.show()





# ## 2.5
# Calculate the global mean values of shortwave and longwave radiation, composited in high and low cloud regions.

glb_mean_sw_lowhigh = (low_cloud_sw + high_cloud_sw).mean()
glb_mean_lw_lowhigh = (low_cloud_lw + high_cloud_lw).mean()
glb_mean_low_cld = lowcld_sl.mean()     # 全球low cloud region的平均太阳辐射（短波+长波）
glb_mean_high_cld = highcld_sl.mean()   # 全球high cloud region的平均太阳辐射（短波+长波）
print(f'Global mean values of shortwave radiation in low cloud and high cloud regions: {glb_mean_sw_lowhigh.values}')
print(f'Global mean values of longwave radiation in low cloud and high cloud regions: {glb_mean_lw_lowhigh.values}')
print(f'Global mean values of shortwave and longwave radiation in low cloud region: {glb_mean_low_cld.values}')
print(f'Global mean values of shortwave and longwave radiation in high cloud region: {glb_mean_high_cld.values}')


# As the cartoon showes, total reflected solar radiation is 99.9 W/m^2, total outgoing infrared radiation is 239.9 W/m^2. Compared with the calculation results given above, global mean shortwave radiation is 218.92 W/m^2 for low cloud and high cloud areas, global mean longwave radiation is 430.67 W/m^2 for low cloud and high cloud areas.and Global mean values of shortwave and longwave radiation in low cloud area is 321.88 W/m^2,  global mean values of shortwave and longwave radiation in high cloud area is  330.12 W/m^2.
# 
# Therefore, clouds can scatter and absorb shortwave radiation from the sun and block longwave radiation emitted from the surface. And I found that high cloud areas scatter and absorb more solar radiation than low cloud areas. In addition, clouds emit longwave thermal radiation to the surface and into space, which plays a key role in the earth's energy budget.
