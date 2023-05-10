# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:09:58 2023

@author: gy22fybm
"""

def weight(data, weight):    
    """
    Applies weights to individual suitability factors.
   
    Weighted factor = Factor x Weight
    
    Parameters
    ----------
    data1 : Input data source (list of lists)
    data2 : Output data name (list of lists)
    weight : Weight of the factor (integer)

    Returns
    -------
    weighted suitability factor : list of lists

    """
    w_data = []
    for row in data:
        w_row = []
        for val in row:
            w_row.append(val*weight)
        w_data.append(w_row)
    return w_data

def combine(x, y, z, wx, wy, wz):
    result = []
    for r in range(len(x)):
        rr = []
        result.append(rr)
        for c in range(len(x[0])):
            rr.append(x[r][c]*wx + y[r][c]*wy + z[r][c]*wz)
    return result
    

def rescale(suit):
    """
    Standardised scales to (0,255):
        1. Find max value
        2. Rescale to (0,255) using
            (data / max value) * 255

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
        
    # Rescale to (0,255)
    suit_map = []
    for row in suit:
        row_suit = []
        for val in row:
            row_suit.append((val / max_suit) * 255)
        suit_map.append(row_suit)
    
    return suit_map 