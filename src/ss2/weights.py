# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:45:39 2023

@author: gy22fybm
"""

import csv
import matplotlib
import matplotlib.pyplot as plt



# Location of inputs
geo ='../../data/input/geology.txt' # geology
pop ='../../data/input/population.txt' # population
trs ='../../data/input/transport.txt' # transport


def read_data(path):
    """
    Read data.

    Parameters
    ----------
    path : String
        Path of the file to be read. The file is expected to be a rectangular
        2D CSV format data with numerical values.

    Returns
    -------
    data : List of lists
        The data in row major order.

    """
    f = open(path)
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        data.append(row)
    f.close()
    #print(data)
    return data

# Read and import site suitability factors: geology, population and transport
data_geo = read_data(geo)
data_pop = read_data(pop)
data_trs = read_data(trs)



# Plot all three site suitability factors (un-weighted)
f, ax = plt.subplots(1,3)
label = ["Geology", "Population", "Transportation"]
data = [data_geo, data_pop, data_trs]

for i in range(0,3):
    ax[i].imshow(data[i])
    ax[i].set_title(label[i])
    ax[i].set_axis_off()
    

# Initialise weights
wg = 1
wp = 2
wt = 3    
    
# Multiply geology factor with a weight
w_geo = []
for row in data_geo:
	row_geo = []
	for val in row:
		row_geo.append(val*wg)
	w_geo.append(row_geo)

# Multiply population factor with a weight
w_pop = []
for row in data_pop:
	row_pop = []
	for val in row:
		row_pop.append(val*wp)
	w_pop.append(row_pop)

# Multiply transportation factor with a weight
w_trs = []
for row in data_trs:
	row_trs = []
	for val in row:
		row_trs.append(val*wt)
	w_trs.append(row_trs)

# Plot one weighted factor with scale for QC
fig, ax = plt.subplots()
cax = ax.imshow(w_geo, cmap='YlGn') 
fig.colorbar(cax).set_label("Suitability", rotation=270) 
ax.set_title("Geology Weighted Factor")
cax.axes.get_xaxis().set_visible(False)
cax.axes.get_yaxis().set_visible(False)



# Combine all weighted factors through multiplication
suit = []
for i in zip(w_geo, w_pop, w_trs):
    suit.append([x * y * z for x, y, z in zip(*i)]) 
    
# Plot combined weighted factors for QC
fig, ax = plt.subplots()
cax = ax.imshow(suit, cmap='YlGn') 
fig.colorbar(cax).set_label("Suitability", rotation=270) 
ax.set_title("Combined Factors")
cax.axes.get_xaxis().set_visible(False)
cax.axes.get_yaxis().set_visible(False)



# Standardised scales to (0,255)
# Find max value
max_suit = 0
for row in suit:
    for val in row:
        max_row = max(row)
        max_suit = max(max_suit, max_row)
#print("max", max_suit)
        
# Rescale to (0,255)
suit_map = []
for row in suit:
    row_suit = []
    for val in row:
        row_suit.append((val / max_suit) * 255)
    suit_map.append(row_suit)    
    
# Plot suitability map
fig, ax = plt.subplots()
cax = ax.imshow(suit_map, cmap='YlGn') 
fig.colorbar(cax).set_label("Suitability", rotation=270) 
ax.set_title("Suitability Map")
cax.axes.get_xaxis().set_visible(False)
cax.axes.get_yaxis().set_visible(False)    
        
    
    