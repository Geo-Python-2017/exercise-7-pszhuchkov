# -*- coding: utf-8 -*-
"""
The script reads monthly average anomaly of temperatures data for Helsinki and Sodankyla.
It sorts into special empty DataFrames for each season in each year. Then happens plotting of
comparing bar-plots and creating of animation from ones.


Author: Pavel Zhuchkov - 17.04.2018
"""

# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import imageio
import glob

# Read file
dataHel = pd.read_csv('helsinki.csv',usecols=['YM','TAVG_Celsius','avgTempsC','Diff'])
dataSod = pd.read_csv('sodankyla.csv',usecols=['YM','TAVG_Celsius','avgTempsC','Diff'])

# Convert column to datetime type
dataHel['YM'] = pd.to_datetime(dataHel['YM'],format='%Y%m')
dataSod['YM'] = pd.to_datetime(dataSod['YM'],format='%Y%m')

# Set datetime index
dataHel = dataHel.set_index('YM')
dataSod = dataSod.set_index('YM')

# Create time index
timeindex = pd.date_range('1953','2017',freq='AS')

# Create empty DataFrames
seasonalDataHel = pd.DataFrame(index=timeindex, columns=['Winter','Spring','Summer','Fall'])
seasonalDataSod = pd.DataFrame(index=timeindex, columns=['Winter','Spring','Summer','Fall'])

# Loop seasons and fill empty DataFrame for Helsinki
for i in range(1953,2018):
    winter = dataHel[str(i-1)+'-12':str(i)+'-02']
    spring = dataHel[str(i)+'-03':str(i)+'-05']
    summer = dataHel[str(i)+'-06':str(i)+'-08']
    fall = dataHel[str(i)+'-09':str(i)+'-11']
    if len(winter) == 3:
        seasonalDataHel.loc[str(i)+'-01-01', ['Winter']] = winter['Diff'].mean(skipna=False)
    if len(spring) == 3: 
        seasonalDataHel.loc[str(i)+'-01-01', ['Spring']] = spring['Diff'].mean(skipna=False)
    if len(summer) == 3:   
        seasonalDataHel.loc[str(i)+'-01-01', ['Summer']] = summer['Diff'].mean(skipna=False)
    if len(fall) == 3:
        seasonalDataHel.loc[str(i)+'-01-01', ['Fall']] = fall['Diff'].mean(skipna=False)

# Loop seasons and fill empty DataFrame for Sodankyla
for i in range(1953,2018):
    winter = dataSod[str(i-1)+'-12-01':str(i)+'-02-01']
    spring = dataSod[str(i)+'-03-01':str(i)+'-05-01']
    summer = dataSod[str(i)+'-06-01':str(i)+'-08-01']
    fall = dataSod[str(i)+'-09-01':str(i)+'-11-01']
    if len(winter) == 3:
        seasonalDataSod.loc[str(i)+'-01-01', ['Winter']] = winter['Diff'].mean(skipna=False)
    if len(spring) == 3:    
        seasonalDataSod.loc[str(i)+'-01-01', ['Spring']] = spring['Diff'].mean(skipna=False)
    if len(summer) == 3:   
        seasonalDataSod.loc[str(i)+'-01-01', ['Summer']] = summer['Diff'].mean(skipna=False)
    if len(fall) == 3:   
        seasonalDataSod.loc[str(i)+'-01-01', ['Fall']] = fall['Diff'].mean(skipna=False)

# Change style of plots
plt.style.use('seaborn-whitegrid')

# Folder for saving bar-plots
myfolder = r'D:\Обучение\GIS\Python\Geo-Python\Lesson7\CompareBars'

# Create y-ticks
yticks = np.arange(start=-8, stop=9,step=2)

# Create multiple bar-plots using for-loop
for i in range(1953,2018):
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,8))
    ax0 = axes[0]
    ax1 = axes[1]
    yearHel = seasonalDataHel[str(i)]
    yearHel.plot(yearHel.index.year, ['Winter','Spring','Summer','Fall'], kind='bar', ax=ax0, color=('blue','magenta','green', 'olive'), edgecolor='None', ylim=(-8,8), yticks=yticks)
    ax0.set_title('Weather anomalies in Helsinki, 1953-2017', size=20)
    ax0.tick_params(axis='x', labeltop=False, labelbottom=False)
    ax0.legend(loc=4,fontsize=12, frameon=True, fancybox=True)
    yearSod = seasonalDataSod[str(i)]
    yearSod.plot(yearSod.index.year, ['Winter','Spring','Summer','Fall'], kind='bar', ax=ax1, color=('blue','magenta','green', 'olive'), edgecolor='None', ylim=(-8,8), yticks=yticks)
    ax1.set_title('Weather anomalies in Sodankyla, 1953-2017', size=20)
    ax1.tick_params(axis='x', labeltop=False, labelbottom=False)
    ax1.legend(loc=4,fontsize=12, frameon=True, fancybox=True)
    fig.add_subplot(111, frameon=False)
    plt.grid('off')
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.ylabel('Difference from long-term seasonal average temperature', size=18, labelpad=-2)
    plt.xlabel(i, size=20, labelpad=-3)
    # Save multiple bar-plots
    filename = "Bar_" + str(i) + ".png"
    filepath = os.path.join(myfolder, filename)
    plt.savefig(filepath, dpi=300)
    plt.close()

# Create animation
search_criteria = r'D:\Обучение\GIS\Python\Geo-Python\Lesson7\CompareBars\*.png'
figure_paths = glob.glob(search_criteria)
output_gif_path = r"D:\Обучение\GIS\Python\Geo-Python\Lesson7\Animation2.gif"
imageio.mimsave(output_gif_path, [imageio.imread(fp) for fp in figure_paths], duration=1.00, subrectangles=True)
