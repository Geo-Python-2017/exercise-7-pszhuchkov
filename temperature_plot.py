# -*- coding: utf-8 -*-
"""
The script builds graph of monthly average temperatures for period 2010-2017

Author: Pavel Zhuchkov - 16.04.2018
"""
# Import modules
import pandas as pd
import matplotlib.pyplot as plt

# Read file
dataHel = pd.read_csv('helsinki.csv')

# Convert column to datetime type
dataHel['YM'] = pd.to_datetime(dataHel['YM'],format='%Y%m')

# Set datetime index
dataHel = dataHel.set_index('YM')

# Slice period 2010-2017
period = dataHel['2010-01-01':'2017-01-01']

# Plot
plt.plot(period.index,period['TAVG_Celsius'],'ko--')
plt.title('Monthly average temperatures in Helsinki for period 2010-2017')
plt.xlabel('DATE')
plt.ylabel('Temperature [°C]')
plt.show()