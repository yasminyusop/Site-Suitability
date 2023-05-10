# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:45:39 2023

@author: gy22fybm
"""

import modules.io as io
import modules.framework as fw
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Location of inputs
geo ='../../data/input/geology.txt' # geology
pop ='../../data/input/population.txt' # population
trs ='../../data/input/transport.txt' # transport


def plot(w_geo, w_pop, w_trs):
   
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


def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    """
    Exit the program.
    """
    root.quit()
    try:
        root.destroy()
    except Exception:
        # Prevents reporting of a harmless Tcl error message:
        # "TclError: can't invoke "destroy" command: application has been destroyed"
        pass


def update_geo(x):
    """
    Updates scale_label and canvas.

    Parameters
    ----------
    x : str.
        Number.

    Returns
    -------
    None.

    """
    
    wg = int(float(scale1.get()))
    scale1_label.config(text='power=' + str(wg))
    weight_geo(wg)
    
def weight_geo(wg):
    global w0
    if w0 != wg:
        w_geo = fw.weight(data_geo, wg)
        
def update(data):
    """
    Updates scale_label and canvas.

    Parameters
    ----------
    x : str.
        Number.

    Returns
    -------
    None.

    """
    
    wg = int(float(scale1.get()))
    #scale1_label.config(text='power=' + str(wg))
    
    wp = int(float(scale2.get()))
    #scale2_label.config(text='power=' + str(wp))   

    wt = int(float(scale3.get()))
    #scale2_label.config(text='power=' + str(wt))
    
    global w0
    if w0 != wg:
        w_geo = fw.weight(data_geo, wg)
   #w_pop = fw.weight(data_pop, wp)
    #w_trs = fw.weight(data_trs, wt)  
    
    
    plot(w_geo, w_pop, w_trs)

      
# Initialise data : geology, population and transport suitability factors
data_geo = io.read_data(geo)
data_pop = io.read_data(pop)
data_trs = io.read_data(trs)

# Initialise weight
w0 = None
    
# Plot all three site suitability factors (un-weighted)
f, ax = plt.subplots(1,3)
label = ["Geology", "Population", "Transportation"]
data = [data_geo, data_pop, data_trs]

for i in range(0,3):
    ax[i].imshow(data[i])
    ax[i].set_title(label[i])
    ax[i].set_axis_off()    

# Plot, write data and map to file
#ss_map = plot(w_geo, w_pop, w_trs)
#plt.savefig('../../data/output/ss_map.jpg')
#io.write_data('../../data/output/ss_map.txt', ss_map)
#print("write data")



     
root = tk.Tk()
l = tk.Label(self, text="Move sliders to choose weightage 1-10 for each factor to apply changes", anchor="c")
l.pack(side="top", fill="both", expand=True)
        

# Create a canvas to display the figure
canvas = FigureCanvasTkAgg(f, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create sliders
scale1 = ttk.Scale(root, from_=1, to=10), command=update(data_geo))
scale1_label = ttk.Label(root, text= 'Geology')

scale2 = ttk.Scale(root, from_=1, to=10), command=update)
scale2_label = ttk.Label(root, text= 'Population')

scale3 = ttk.Scale(root, from_=1, to=10), command=update)
scale3_label = ttk.Label(root, text= 'Transportation')

# Create window title
root.title("Site Suitability Map")

# Pack widgets
scale1.pack()
scale1_label.pack()
scale2.pack()
scale2_label.pack()
scale3.pack()
scale3_label.pack()

root.pack(side="top", fill="both", expand=True)
root.mainloop()




    
        
    
    