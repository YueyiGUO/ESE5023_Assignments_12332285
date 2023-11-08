# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:48:30 2023

@author: Administrator
"""

import pandas as pd
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
%matplotlib inline

# Load the data
Sig_Eqs = pd.read_csv('earthquakes-2023-11-05_22-09-37_+0800.tsv',sep='\t') 
Sig_Eqs


# Group the data by country, calculate total deaths in all country
# and sort them in descending order
sig_deaths10 = Sig_Eqs.groupby(['Country']).sum('Total Deaths').sort_values("Total Deaths",ascending=False).head(10)
print("The top ten countries along with the total number of deaths: ")
sig_deaths10['Total Deaths']


Sig_Eqs[Sig_Eqs['Mag']>6.0]['Id'].count()



sig_eqs_ex6 = Sig_Eqs[Sig_Eqs['Mag']>6.0][['Year','Mag']]
sig_eqs_ex6


# Given data in the x and y directions
x=sig_eqs_ex6["Year"]
y=sig_eqs_ex6["Mag"]

# Count the number of earthquakes with magnitude larger than 6.0 each year
eq_count=Sig_Eqs[Sig_Eqs['Mag']>6.0].groupby('Year').size() 

# Plot figure1()
plt.figure(figsize=(8.5, 8.5))
plt.subplot(2,1,1)
plt.plot(x,y,'go--',linewidth=1,markersize=5)
plt.xlabel("Year",size=12)
plt.ylabel("Mag",size=12)
plt.show()

# Plot figure2()
plt.figure(figsize=(8.5, 8.5))
plt.subplot(2,1,2)
plt.plot(eq_count.index, eq_count.values,'b-')    # Plot the time series
plt.xlabel('Year',size=12)
plt.ylabel('Number of earthquakes with magnitude>6.0',size=10)

plt.show()




def CountEq_LargestEq(COUNTRY,Sig_Eqs):
    country_eqs = Sig_Eqs[Sig_Eqs['Country'] == COUNTRY]   
    total_eqs = len(country_eqs)    #Calculate the total number of earthquakes in given country
    if total_eqs == 0:
        return total_eqs, None
    else:
        #Find the date of the largest earthquake in given country
        largest_eq_date = country_eqs[['Year','Mo','Dy','Mag']].sort_values('Mag',ascending=False).head(1)
    return total_eqs, largest_eq_date


CountEq_LargestEq('CHINA',Sig_Eqs)

# Apply function to each country
results = Sig_Eqs.groupby('Country').apply(lambda x: CountEq_LargestEq(x['Country'].iloc[0], x))

# Sort results in descending order
results.sort_values(by='total_eqs', ascending=False, inplace=True)

print(results)