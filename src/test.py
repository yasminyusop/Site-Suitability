# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:46:14 2023

@author: gy22fybm
"""
import csv
#import modules.io as io
#import modules.framework as fw
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')


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
    #print(x)
    #print(type(x))
    #print(scale.get())
    #print(int(float(scale.get())))
    # Integerise p
    wg = int(float(scale.get()))
    scale_label.config(text='power=' + str(wg))
    plot(wg)

def plot(wg):
    """
    Redraws the canvas if there is a new power.

    Parameters
    ----------
    p : int
        The power to raise values to.

    Returns
    -------
    None.

    """
    global w0
    if w0 != wg:
        figure.clear()
        #print(p)
    w_geo = []
    for row in data_geo:
        w_row = []
        for val in row:
            w_row.append(val*wg)
        w_geo.append(w_row)
      
    suit = []
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
        w0 = wg
    #canvas.draw()


def exiting():
    """
    Exit the program.
    """
    a.quit()
    a.destroy()
    """
    Exit the program.
    """
    a.quit()
    try:
        a.destroy()
    except Exception:
        # Prevents reporting of a harmless Tcl error message:
        # "TclError: can't invoke "destroy" command: application has been destroyed"
        pass
    
def update_scale_label(val):
    #print(val)
    #print(scale.get())
    #print(str(int(float(scale.get()))))
    scale_label.config(text=str(int(float(scale.get()))))

#GUI
 # Initialise figure
figure = matplotlib.pyplot.figure(figsize=(7, 7))
#ax = figure.add_axes([0, 0, 1, 1])

# Initialise data
data_geo = read_data(geo)

# Initialise w0
w0 = None

# Create the tkinter window
a = tk.Tk()

# Create a canvas to display the figure
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=root)
#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a scale
#scale = ttk.Scale(root, from_=1, to=10, command=update)


# Create a scale
scale = ttk.Scale(a, from_=0, to=100, command=update_scale_label)
# Create a Label widget to display scale value
scale_label = ttk.Label(a, text=str(scale.get()))

# Create a Label widget to display scale value
#scale_label = ttk.Label(root, text='Move the scale slider to choose a power and see an image.')
#scale_label.pack()

# Create a Button widget and link this with the exiting function
exit_button = ttk.Button(a, text="Exit", command=exiting)


# Pack widgets so they are visible.
scale.pack()
scale_label.pack()
exit_button.pack()

# Exit if the window is closed.
a.protocol('WM_DELETE_WINDOW', exiting)

# Start the GUI
a.mainloop()   