# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:48:30 2023

@author: Administrator
"""

# Load file
bj_df = pd.read_csv('54511099999.csv')

#Separate the TMP columns with commas to form multiple columns of air temperature related data.
bj_tmp = bj_df['TMP'].str.split(',',expand=True)
bj_tmp.columns = ['tmp','tmpq']
bj_df = pd.concat([bj_df,bj_tmp], axis=1)
bj_df = bj_df.drop('TMP',axis=1)
bj_df['tmp'] = bj_df['tmp'].str.slice(0, 5).astype(float)

# Filter the data
bj_df = bj_df.loc[bj_df['tmp'] != 9999]
bj_df


# Calculate the monthly average temperature in Beijing based on time series
# Convert date to datetime
bj_df['DATE'] = pd.to_datetime(bj_df['DATE'], format="%Y-%m-%dT%H:%M:%S")
bj_df[["DATE","tmp","tmpq"]]
bj_df['YYYY-MM']=bj_df['DATE'].dt.to_period('M')
# Calculate monthly average air temperature
tmp_mon=bj_df[['YYYY-MM','tmp']].groupby(['YYYY-MM']).mean()
tmp_mon

# Plot the data
plt.figure(figsize=(10, 6))
tmp_mon['tmp'].plot()
plt.xlabel('Date')
plt.ylabel('Air temperature(m$~2$)')
plt.title('Beijing Monthly Average air temperature in 2022)')
plt.legend()
plt.show()
bj_df['DATE'] 



# Load file
bj_df = pd.read_csv('54511099999.csv')

#Separate the TMP columns with commas to form multiple columns of air temperature related data.
bj_tmp = bj_df['TMP'].str.split(',',expand=True)
bj_tmp.columns = ['tmp','tmpq']
bj_df = pd.concat([bj_df,bj_tmp], axis=1)
bj_df = bj_df.drop('TMP',axis=1)
bj_df['tmp'] = bj_df['tmp'].str.slice(0, 5).astype(float)

# Filter the data
bj_df = bj_df.loc[bj_df['tmp'] != 9999]

# Convert date to datetime
bj_df['DATE'] = pd.to_datetime(bj_df['DATE'], format="%Y-%m-%dT%H:%M:%S")
bj_df=bj_df[['DATE','tmp','tmpq']]

# Set date as index
bj_df


# 1 Calculate the average annual air temperature in Beijing
ann_avg=bj_df['tmp'].mean()/10
ann_avg


# 2 Calculate the annual maximum air temperature in Beijing
max_avg=bj_df['tmp'].max()/10
max_avg

# 3 Calculate the daily minimum air temperature in Beijing
min_avg=bj_df['tmp'].min()/10
min_avg


# 4 Calculate the variance of annual average temperature in Beijing
bj_cels=bj_df['tmp']/10
var_avg=bj_cels.var()
var_avg


# 5 Calculate the number of days with a temperature above 35 degrees
bj_df.loc[bj_df['tmp']>350].count()