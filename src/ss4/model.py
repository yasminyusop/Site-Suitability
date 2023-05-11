# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:45:39 2023

@author: gy22fybm
"""

import modules.io as io
import modules.framework as fw
import matplotlib.pyplot as plt
import random
import time


# Location of inputs
geo ='../../data/input/geology.txt' # geology
pop ='../../data/input/population.txt' # population
trs ='../../data/input/transport.txt' # transport


def plot(wg, wp, wt):
    """
    Plots the site suitability map in (0,255) scale based on weights

    Parameters
    ----------
    wg : weight for geology factor
    wp : weight for population factor
    wt : weight for transportation factor


    Returns
    -------
    ss_map : list of lists

    """

    # Read data from source files   
    data_geo = io.read_data(geo)
    data_pop = io.read_data(pop)
    data_trs = io.read_data(trs)

    # Apply weights and combine the three factors    
    suit = fw.combine(data_geo, data_pop, data_trs, wg, wp, wt)
             
    # Plot suitability map
    ss_map = fw.rescale(suit)
    fig, ax = plt.subplots()
    cax = ax.imshow(ss_map, cmap='YlGn') 
    fig.colorbar(cax).set_label("Suitability", rotation=270) 
    ax.set_title("Suitability Map")
    cax.axes.get_xaxis().set_visible(False)
    cax.axes.get_yaxis().set_visible(False)
    
    return ss_map    



#start = time.perf_counter()



# Initialise weights
wg = random.randint(1, 10)
wp = random.randint(1, 10)
wt = random.randint(1, 10)    
print('wg', wg)
print('wp', wp)
print('wt', wt)  



# Plot, write data and map to file
ss_map = plot(wg, wp, wt)
plt.savefig('../../data/output/ss_map.jpg')
io.write_data('../../data/output/ss_map.txt', ss_map)
print("write data")
    


#end = time.perf_counter()        
#print("Time taken to plot", end - start, "seconds")
    
    