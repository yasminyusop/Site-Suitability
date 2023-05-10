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

def update(x):
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
    scale1_label.config(text='Geology=' + str(wg))
    
    wp = int(float(scale2.get()))
    scale2_label.config(text='Population=' + str(wp))   

    wt = int(float(scale3.get()))
    scale3_label.config(text='Transportation=' + str(wt))  
    
    plot(wg, wp, wt)

def plot(wg, wp, wt):
    
    # Clears figure
    
    figure.clear()
    w_geo = fw.weight(data_geo, wg)
    w_pop = fw.weight(data_pop, wp)
    w_trs = fw.weight(data_trs, wt)
    
    # Combine all weighted factors through multiplication
    suit = fw.combine(w_geo, w_pop, w_trs, wg, wp, wt)
    # suit = []
    # for i in zip(w_geo, w_pop, w_trs):
    #     suit.append([x * y * z for x, y, z in zip(*i)]) 
         
    # Plot suitability map
    ss_map = fw.rescale(suit)
    plt.imshow(ss_map, cmap='YlGn')
    plt.grid(False)
    plt.axis('off')
    plt.colorbar(label='Suitability')
    plt.title('Site Suitability Map')
    plt.text(230, 60,'Geology=' + str(wg))
    plt.text(230, 75,'Population=' + str(wp))
    plt.text(230, 90,'Transportation=' + str(wt))
    plt.show()
    
    # Draw on canvas
    canvas.draw()             

def save():
    """
    Saves image of the map generated into the output folder

    Returns
    -------
    None.

    """
    plt.savefig('../../data/output/ss_map.jpg')
    #print("write data")

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

     


      
# Initialise data : geology, population and transport suitability factors
data_geo = io.read_data(geo)
data_pop = io.read_data(pop)
data_trs = io.read_data(trs)





# Initialise figure

figure = matplotlib.pyplot.figure(figsize=(7, 7))
 
# GUI setup

# Initialise GUI window    
root = tk.Tk()

# Create label with instructions
label = tk.Label(root, text="Move sliders to choose weightage 1-10 for each factor. "
                 "Changes will be automatically applied", anchor="c")        


# Create a canvas to display the figure
canvas = FigureCanvasTkAgg(figure, master=root)





# Create sliders
scale1 = ttk.Scale(root, from_=1, to=10, command=update)
scale1_label = ttk.Label(root, text= 'Geology')

scale2 = ttk.Scale(root, from_=1, to=10, command=update)
scale2_label = ttk.Label(root, text= 'Population')

scale3 = ttk.Scale(root, from_=1, to=10, command=update)
scale3_label = ttk.Label(root, text= 'Transportation')

# Create window title
root.title("Site Suitability Map")

# Create a Button widget and link this with the save function
save_button = ttk.Button(root, text="Save", command=save)

# Create a Button widget and link this with the exiting function
exit_button = ttk.Button(root, text="Exit", command=exiting)

# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)

# Pack widgets
label.pack()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
scale1.pack()
scale1_label.pack()
scale2.pack()
scale2_label.pack()
scale3.pack()
scale3_label.pack()
save_button.pack(side=tk.LEFT)
exit_button.pack(side=tk.RIGHT)

#root.pack(side="top", fill="both", expand=True)
root.mainloop()




    
        
    
    