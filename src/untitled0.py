# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:00:00 2023

@author: yasmi
"""
import csv
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExampleView(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)      
        l = tk.Label(self, text="your widgets go here...", anchor="c")
        l.pack(side="top", fill="both", expand=True)

if __name__=='__main__':
    root = tk.Tk()
    view = ExampleView(root)
    view.pack(side="top", fill="both", expand=True)

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
    
# Create canvas for map
canvas = FigureCanvasTkAgg(f, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create sliders
scale1 = ttk.Scale(root, from_=1, to=10) #, command=update(data_geo))
scale1_label = ttk.Label(root, text= 'Geology')

scale2 = ttk.Scale(root, from_=1, to=10) #, command=update(data_pop))
scale2_label = ttk.Label(root, text= 'Population')

scale3 = ttk.Scale(root, from_=1, to=10) #, command=update(data_trs))
scale3_label = ttk.Label(root, text= 'Transportation')

note = ttk.Label(root, text='Move sliders to choose weightage 1-10 for each factor to apply changes')
    
print(scale1.get())
print(int(float(scale1.get())))

# Pack widgets
scale1.pack()
scale1_label.pack()
scale2.pack()
scale2_label.pack()
scale3.pack()
scale3_label.pack()
note.pack()

root.title("Site Suitability Map")
root.mainloop()