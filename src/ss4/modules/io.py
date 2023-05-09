# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:04:16 2023

@author: gy22fybm
"""
import csv

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
    Writes data into a file in CSV format

    Parameters
    ----------
    filename : file path 
    data : list of lists

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