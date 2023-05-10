# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:45:39 2023

@author: gy22fybm
"""

import csv
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

def write_data(filename,data):
    # Open a file for writing
    f = open(filename, 'w', newline='')
    # Write a to the file
    writer = csv.writer(f, delimiter=' ')
    for row in data:
        writer.writerow(row) # List of values.
    # Close the file
    f.close() 


def weight(data, weight):    
    """
    Applies weights to individual suitability factors.
   
    Weighted factor = Factor x Weight
    
    Parameters
    ----------
    data1 : Input data source (list of lists)
    data2 : Output data name (list of lists)
    weight : Weight of the factor (integer)

    Returns
    -------
    weighted suitability factor : list of lists

    """
    w_data = []
    for row in data:
        w_row = []
        for val in row:
            w_row.append(val*weight)
        w_data.append(w_row)
    return w_data    

def rescale(suit):
    """
    Standardised scales to (0,255):
        1. Find max value
        2. Rescale to (0,255) using
            (data / max value) * 255

    Parameters
    ----------
    suit : combined weighted factors (list of lists)

    Returns
    -------
    suit_map : combined weighted factors rescaled to (0,255) : list of lists
    """
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
    
    return suit_map        
        
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
wg = 2
wp = 2
wt = 5    

# Initilialise weighted factors' lists
w_geo = []
w_pop = []
w_trs = []

# Apply weights
w_geo = weight(data_geo, wg)
w_pop = weight(data_pop, wp)
w_trs = weight(data_trs, wt)

# Plot one weighted factor with scale for QC
#fig, ax = plt.subplots()
#cax = ax.imshow(w_geo, cmap='YlGn') 
#fig.colorbar(cax).set_label("Suitability", rotation=270) 
#ax.set_title("Geology Weighted Factor")
#cax.axes.get_xaxis().set_visible(False)
#cax.axes.get_yaxis().set_visible(False)


# Combine all weighted factors through multiplication
suit = []
for i in zip(w_geo, w_pop, w_trs):
    suit.append([x * y * z for x, y, z in zip(*i)]) 
         
# Plot suitability map
plot = rescale(suit)
fig, ax = plt.subplots()
cax = ax.imshow(plot, cmap='YlGn') 
fig.colorbar(cax).set_label("Suitability", rotation=270) 
ax.set_title("Suitability Map")
cax.axes.get_xaxis().set_visible(False)
cax.axes.get_yaxis().set_visible(False)
plt.savefig('../../data/output/ss_map.jpg')

# Write data and map to file
#def output():
    # Write data
print("write data")
write_data('../../data/output/ss_map.txt', plot)
    
        
    
    