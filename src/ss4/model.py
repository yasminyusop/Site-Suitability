# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:45:39 2023

@author: gy22fybm
"""

import modules.io as io
import modules.framework as fw
import matplotlib.pyplot as plt


# Location of inputs
geo ='../../data/input/geology.txt' # geology
pop ='../../data/input/population.txt' # population
trs ='../../data/input/transport.txt' # transport


def plot(data_geo, data_pop, data_trs):

 
    w_geo = []
    w_pop = []
    w_trs = []  
    
    # Apply weights
    w_geo = fw.weight(data_geo, wg)
    w_pop = fw.weight(data_pop, wp)
    w_trs = fw.weight(data_trs, wt)
    
    # Combine all weighted factors through multiplication
    suit = []
    for i in zip(w_geo, w_pop, w_trs):
        suit.append([x * y * z for x, y, z in zip(*i)]) 
         
    # Plot suitability map
    ss_map = fw.rescale(suit)
    fig, ax = plt.subplots()
    cax = ax.imshow(ss_map, cmap='YlGn') 
    fig.colorbar(cax).set_label("Suitability", rotation=270) 
    ax.set_title("Suitability Map")
    cax.axes.get_xaxis().set_visible(False)
    cax.axes.get_yaxis().set_visible(False)

    return ss_map          


        
# Read and import site suitability factors: geology, population and transport
data_geo = io.read_data(geo)
data_pop = io.read_data(pop)
data_trs = io.read_data(trs)



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



# Plot, write data and map to file
ss_map = plot(data_geo, data_pop, data_trs)
plt.savefig('../../data/output/ss_map.jpg')
io.write_data('../../data/output/ss_map.txt', ss_map)
print("write data")
    
        
    
    