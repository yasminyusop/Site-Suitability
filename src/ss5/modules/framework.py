# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:09:58 2023

@author: gy22fybm
"""

def combine(x, y, z, wx, wy, wz):
    """
    Multiplies weights to individual suitability factors then adds the
    weighted factors together.
   
    Suitability = (Weight1 x Factor1) + (Weight2 x Factor2) 
                    + (Weight3 x Factor3)

    Parameters
    ----------
    x : Suitability factor 1 (list of lists)
    y : Suitability factor 2 (list of lists)
    z : Suitability factor 3 (list of lists)
    wx : Weight for factor 1 (integer)
    wy : Weight for factor 2 (integer)
    wz : Weight for factor 3 (integer)

    Returns
    -------
    result : list of lists

    """
    result = []
    for r in range(len(x)):
        rr = []
        result.append(rr)
        for c in range(len(x[0])):
            rr.append(x[r][c]*wx + y[r][c]*wy + z[r][c]*wz)
    return result
    

def rescale(data):
    """
    Standardised scales to (0,255):
        1. Find max and min value
        2. Rescale to (0,255) using
            ((data - min value) / (max value - min value)) * 255          

    Parameters
    ----------
    data : data to be rescaled (list of lists)

    Returns
    -------
    output : rescaled data to (0,255) : list of lists
    """
   
    max_data = 0
    for row in data:
        max_row = max(row)
        for val in row:
            max_data = max(max_data, max_row)
    #print("max", max_data)
   
    # Find min value
    min_data = 0
    for row in data:
        min_row = min(row)
        for val in row:
            min_data = min(min_data, min_row)
    #print("min", min_data) 
    
    # Rescale to (0,255)
    output = []
    for row in data:
        row_output = []
        for val in row:
            row_output.append((val - min_data) / (max_data - min_data) * 255)
        output.append(row_output)
    
    return output 