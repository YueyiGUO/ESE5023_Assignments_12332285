# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:48:30 2023

@author: Administrator
"""
# Read the .csv file
sz_df = pd.read_csv('2281305.csv')

#Separate the WND columns with commas to form multiple columns of wind related data.
sz_df_wnd = sz_df['WND'].str.split(',',expand=True)   
sz_df_wnd.columns = ['agl','aglq','wnd_ty','wnd_sp','wndq']
sz_df = pd.concat([sz_df,sz_df_wnd], axis=1)
sz_df = sz_df.drop('WND',axis=1)
sz_df['wnd_sp'] = sz_df['wnd_sp'].str.slice(0, 5).astype(float)

# Filter the data
sz_df = sz_df.loc[sz_df_wnd['wnd_sp'] != 9999]

# Convert date to datetime
sz_df['DATE'] = pd.to_datetime(sz_df['DATE'], format="%Y-%m-%dT%H:%M:%S")
sz_df=sz_df[['DATE','agl','aglq','wnd_ty','wnd_sp','wndq']]
sz_df['YYYY-MM']=sz_df['DATE'].dt.to_period('M')

# Calculate monthly average wind speed
wnd_mon=sz_df[['YYYY-MM','wnd_sp']].groupby(['YYYY-MM']).mean() /10
wnd_mon

# Plot the data
plt.figure(figsize=(10, 6))
wnd_mon['wnd_sp'].plot()
plt.xlabel('Date')
plt.ylabel('wind speed(m$~2$)')
plt.title('Monthly Average Wind Speed in Shenzhen over the past 10 Years)')
plt.legend()
plt.show()
