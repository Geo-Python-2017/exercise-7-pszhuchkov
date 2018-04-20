# -*- coding: utf-8 -*-
"""
The script reads monthly average anomaly of temperatures data for Helsinki. It sorts 
into special empty DataFrame for each season in each year. Then happens plotting of
bar-plots and creating of animation from ones.


Author: Pavel Zhuchkov - 17.04.2018
"""

# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio
import glob

# Read file
dataHel = pd.read_csv('helsinki.csv',usecols=['YM','TAVG_Celsius','avgTempsC','Diff'])

# Convert column to datetime type
dataHel['YM'] = pd.to_datetime(dataHel['YM'],format='%Y%m')

# Set datetime index
dataHel = dataHel.set_index('YM')

# Create time index
timeindex = pd.date_range('1953','2017',freq='AS')

# Create empty DataFrame
seasonalData = pd.DataFrame(index=timeindex, columns=['Winter','Spring','Summer','Fall'])

# Loop seasons and fill empty DataFrame
for i in range(1953,2018):
    winter = dataHel[str(i-1)+'-12':str(i)+'-02']
    spring = dataHel[str(i)+'-03':str(i)+'-05']
    summer = dataHel[str(i)+'-06':str(i)+'-08']
    fall = dataHel[str(i)+'-09':str(i)+'-11']
    if len(winter) == 3:
        seasonalData.loc[str(i)+'-01-01', ['Winter']] = winter['Diff'].mean(skipna=False)
    if len(spring) == 3:   
        seasonalData.loc[str(i)+'-01-01', ['Spring']] = spring['Diff'].mean(skipna=False)
    if len(summer) == 3:   
        seasonalData.loc[str(i)+'-01-01', ['Summer']] = summer['Diff'].mean(skipna=False)
    if len(fall) == 3:
        seasonalData.loc[str(i)+'-01-01', ['Fall']] = fall['Diff'].mean(skipna=False)

# Change style of plots
plt.style.use('seaborn-whitegrid')

# Folder for saving bar-plots
myfolder = r'D:\Обучение\GIS\Python\Geo-Python\Lesson7\Bars'

# Create y-ticks
yticks = np.arange(start=-6, stop=7,step=2)

# Create multiple bar-plots using for-loop
for i in range(1953,2018):
    fig, ax = plt.subplots(figsize=(10,6))
    raw = seasonalData[str(i)]
    raw.plot(raw.index.year, ['Winter','Spring','Summer','Fall'], kind='bar', ax=ax, color=('blue','magenta','green', 'olive'), edgecolor='None', ylim=(-6.5,6.5), yticks=yticks)
    ax.set_title('Weather anomalies in Helsinki, 1953-2017', size=25)
    ax.set_ylabel('Difference from long-term\n seasonal average temperature', size=22)
    plt.xticks(rotation=0)
    ax.tick_params(axis='x', which='major', pad=10, labelsize=20)
    # Save multiple bar-plots
    filename = "Bar_" + str(i) + ".png"
    filepath = os.path.join(myfolder, filename)
    plt.savefig(filepath, dpi=300)
    plt.close()

# Create animation
search_criteria = r'D:\Обучение\GIS\Python\Geo-Python\Lesson7\Bars\*.png'
figure_paths = glob.glob(search_criteria)
output_gif_path = r"D:\Обучение\GIS\Python\Geo-Python\Lesson7\Animation.gif"
imageio.mimsave(output_gif_path, [imageio.imread(fp) for fp in figure_paths], duration=1.00, subrectangles=True)
