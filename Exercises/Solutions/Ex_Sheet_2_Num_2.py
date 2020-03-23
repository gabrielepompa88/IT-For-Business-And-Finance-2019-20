"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_2.py

Description: This script computes prints indexes and values of an array.
"""

import numpy as np

def printArray(a):
    """
    Function printArray(a) prints indexes and values of array a.
    
    Parameters:
        a (numpy.ndarray): input array.
    
    Returns:
        None
    """
    
    for i, ai in enumerate(a):
        print("Index i = {} - Value a[i] = {}".format(i, ai))


def main():
    """
    Function main() defines a NumPy array and computes the product of its elements.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test array
    arr = np.array([17, 5, -10, 8, -2])
    
    # print function
    printArray(arr)
    
    
if __name__ == "__main__":
    main()
