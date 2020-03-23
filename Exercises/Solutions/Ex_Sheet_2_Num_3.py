"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_3.py

Description: This script generate three different arrays.
"""

import numpy as np

def initArray(value, length):
    """
    Function initArray(value, length) initializes a NumPy array of len 'length'
    filled with the same value 'value'
    
    Parameters:
        value (float): scalar value to fill the array.    
        length (int): length of the array.    

    Returns:
        None
    """
    
    if value == 1:
        return np.ones(length)
    else:
        return np.zeros(length) + value 
    
    # alternative version: this version is equivalent, but an addition is in 
    # general more efficient than a multiplication, that's why I would slightly
    # prefer the choice above.
    #
    # if value == 0:
    #    return np.zeros(length)
    # else:
    #     return np.ones(length)*value 
    

def main():
    """
    Function main() defines a three Numy arrays, the first made of 10 zeros, 
    the second made of 10 ones and the last one made of 10 fives.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # arrays
    tenZeros = initArray(0, 10)
    tenOnes = initArray(1, 10)
    tenFives = initArray(5, 10)
    
    # Print section
    print("Array of 10 zeros = {}".format(tenZeros))
    print("Array of 10 ones  = {}".format(tenOnes))
    print("Array of 10 fives = {}".format(tenFives))
    
    
if __name__ == "__main__":
    main()
