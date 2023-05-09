# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:57:20 2023

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


# Plot one factor with scale for QC
#fig, ax = plt.subplots()
#cax = ax.imshow(data_geo, cmap='YlGn')   
#fig.colorbar(cax).set_label("Suitability", rotation=270) 
#ax.set_title("Geology Unweighted Factor")
#cax.axes.get_xaxis().set_visible(False)
#cax.axes.get_yaxis().set_visible(False)


# Plot all three site suitability factors
f, ax = plt.subplots(1,3)
label = ["Geology", "Population", "Transportation"]
data = [data_geo, data_pop, data_trs]

for i in range(0,3):
    ax[i].imshow(data[i])
    ax[i].set_title(label[i])
    ax[i].set_axis_off()
