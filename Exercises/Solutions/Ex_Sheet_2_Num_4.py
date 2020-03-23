"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_4.py

Description: This script creates an array of numbers from 30 to 70.
"""

import numpy as np

def rangeArray(first, last):
    """
    Function initArray(first last) initializes a NumPy array of numbers from
    'first' to 'last'
    
    Parameters:
        first (float): first number of the array.    
        last (float): first number of the array.    

    Returns:
        None
    """
    
    return np.arange(first, last+1)
    

def main():
    """
    Function main() defines an array of numbers from 30 to 70.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # boundaries of the array
    n = 30
    m = 70
    
    # array generated
    arr = rangeArray(n,m)
        
    # Print section
    print("Array from {} to {}: {}".format(n, m, arr))
    
    
if __name__ == "__main__":
    main()
