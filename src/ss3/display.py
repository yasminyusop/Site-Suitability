# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:45:39 2023

@author: gy22fybm
"""

import csv
import random
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
    """
    Writes and saves data into CSV format

    Parameters
    ----------
    filename : location and name of file
    data : data to be saved (list of lists)

    Returns
    -------
    None.

    """
    
    # Open a file for writing
    f = open(filename, 'w', newline='')
    # Write a to the file
    writer = csv.writer(f, delimiter=' ')
    for row in data:
        writer.writerow(row) # List of values.
    # Close the file
    f.close() 


def combine(data_geo, data_pop, data_trs, wg, wp, wt):    
    """
    Multiplies weights to individual suitability factors then adds the
    weighted factors together.
   
    Unscaled Suitability = (Weight1 x Factor1) + (Weight2 x Factor2) 
                                + (Weight3 x Factor3)

    Parameters
    ----------
    data_geo : Suitability factor 1 (list of lists)
    data_pop : Suitability factor 2 (list of lists)
    data_trs : Suitability factor 3 (list of lists)
    wg : Weight for factor 1 (integer)
    wp : Weight for factor 2 (integer)
    wt : Weight for factor 3 (integer)

    Returns
    -------
    suit : list of lists

    """
    suit = []
    for row in range(len(data_geo)):
        row_suit = []
        suit.append(row_suit)
        for val in range(len(data_geo[0])):
            row_suit.append(data_geo[row][val]*wg + data_pop[row][val]*wp + 
                            data_trs[row][val]*wt)
    
    return suit

def rescale(suit):
    """
    Standardised scales to (0,255):
        1. Find max value
        2. Rescale to (0,255) using
            ((data - min value) / (max value - value)) * 255
            
            where min value = 0

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
    
    # Find min value
    min_suit = 0
    for row in suit:
        min_row = min(row)
        for val in row:
            min_suit = min(min_suit, min_row)
    #print("min", min_suit)    
    
    # Rescale to (0,255)
    suit_map = []
    for row in suit:
        row_suit = []
        for val in row:
            row_suit.append((val - min_suit) / (max_suit - min_suit) * 255)
        suit_map.append(row_suit)
    
    return suit_map        
        


# Read and import site suitability factors: geology, population and transport
data_geo = read_data(geo)
data_pop = read_data(pop)
data_trs = read_data(trs)

# Plot all three site suitability factors (un-weighted)
#f, ax = plt.subplots(1,3)
#label = ["Geology", "Population", "Transportation"]
#data = [data_geo, data_pop, data_trs]

#for i in range(0,3):
    #ax[i].imshow(data[i])
    #ax[i].set_title(label[i])
    #ax[i].set_axis_off()
    


# Initialise weights
wg = random.randint(1, 10)
wp = random.randint(1, 10)
wt = random.randint(1, 10)    
print('wg', wg)
print('wp', wp)
print('wt', wt) 



# Combine all weighted factors
suit = combine(data_geo, data_pop, data_trs, wg, wp, wt) 

# Plot combined weighted factors
#fig, ax = plt.subplots()
#cax = ax.imshow(suit, cmap='YlGn') 
#fig.colorbar(cax).set_label("Suitability", rotation=270) 
#ax.set_title("Combined Weighted Factors")
#cax.axes.get_xaxis().set_visible(False)
#cax.axes.get_yaxis().set_visible(False)


         
# Plot suitability map
ss_map = rescale(suit) # rescale to (0,255)
fig, ax = plt.subplots()
cax = ax.imshow(ss_map, cmap='YlGn') 
fig.colorbar(cax).set_label("Suitability", rotation=270) 
ax.set_title("Suitability Map")
cax.axes.get_xaxis().set_visible(False)
cax.axes.get_yaxis().set_visible(False)



# Write data and map to file
plt.savefig('../../data/output/ss_map.jpg')
write_data('../../data/output/ss_map.txt', ss_map)
print("write data")    
        
    
    