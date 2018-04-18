# -*- coding: utf-8 -*-
"""
The script reads monthly average temperatures data for Helsinki. Then monthly
average temperatures sorts into special empty DataFrame for each season in each year..
Author: Pavel Zhuchkov - 17.04.2018
"""

# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read file
dataHel = pd.read_csv('helsinki.csv',usecols=['YM','TAVG_Celsius','avgTempsC','Diff'])

# Convert column to datetime type
dataHel['YM'] = pd.to_datetime(dataHel['YM'],format='%Y%m')

# Set datetime index
dataHel = dataHel.set_index('YM')

# Create time index
timeindex = pd.date_range('1953','2016',freq='AS')

# Create empty DataFrame
seasonalData = pd.DataFrame(index=timeindex, columns=['Winter','Spring','Summer','Fall'])

# Loop seasons and fill empty DataFrame
for i in range(1953,2017):
    winter = dataHel[str(i-1)+'-12-01':str(i)+'-02-01'].mean()
    spring = dataHel[str(i)+'-03-01':str(i)+'-05-01'].mean()
    summer = dataHel[str(i)+'-06-01':str(i)+'-08-01'].mean()
    fall = dataHel[str(i)+'-09-01':str(i)+'-11-01'].mean()
    seasonalData.loc[str(i)+'-01-01', ['Winter']] = winter['Diff']
    seasonalData.loc[str(i)+'-01-01', ['Spring']] = spring['Diff']
    seasonalData.loc[str(i)+'-01-01', ['Summer']] = summer['Diff']
    seasonalData.loc[str(i)+'-01-01', ['Fall']] = fall['Diff']

# Change style of plots
plt.style.use('seaborn-whitegrid')

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8))

# Create variables of subplots
ax11 = axes[0][0]
ax12 = axes[0][1]
ax21 = axes[1][0]
ax22 = axes[1][1]

# Create array of y-ticks
yticks = np.arange(start=-5, stop=6, step=2.5)

# Create subplots
seasonalData.plot(x=seasonalData.index, y='Winter', ax=ax11, c='blue', legend=False, lw=2.5, ylim=(-7, 7), xlim=('1950','2019'))
seasonalData.plot(x=seasonalData.index, y='Spring', ax=ax12, c='blue', legend=False, lw=2.5, ylim=(-7, 7), xlim=('1950','2019'))
seasonalData.plot(x=seasonalData.index, y='Summer', ax=ax21, c='blue', legend=False, lw=2.5, ylim=(-7, 7), xlim=('1950','2019'))
seasonalData.plot(x=seasonalData.index, y='Fall', ax=ax22, c='blue', legend=False, lw=2.5, ylim=(-7, 7), xlim=('1950','2019'))

# Set y-axis labels
for ax in [ax11,ax21]:
    ax.set_ylabel('Temperature [°C]')

# Set x-axis labels    
for ax in [ax21,ax22]:
    ax.set_xlabel('Date')

# Add legend with parameters
for ax in [ax11,ax12,ax21,ax22]:
    ax.legend(frameon=True,loc='best',framealpha=0.5)
    
# Set y-ticks
for ax in [ax11,ax12,ax21,ax22]:
    ax.yaxis.set_ticks(yticks)

# Tight layout
plt.tight_layout()
    