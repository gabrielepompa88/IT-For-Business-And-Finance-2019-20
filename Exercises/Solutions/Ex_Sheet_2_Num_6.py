"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_3.py

Description: This script generate an array and change sign to some values.
"""

import numpy as np

def changeSign(a, startInd, endInd):
    """
    Function changeSign(a, startInd, endInd) change the sign of values of array
    'a' between indexes 'startInd' and 'endInd'
    
    Parameters:
        a (numpy.ndarray): input array
        startInd (int): first index to be changed in sign.    
        endInd (int): last index to be changed in sign.    

    Returns:
        a (numpy.ndarray): input array changed, returned in output
    """
    
    for i in np.arange(len(a)):
        if (i >= startInd) & (i <= endInd):
            a[i] = -a[i]

    return a

def main():
    """
    Function main() defines a three Numy arrays, the first made of 10 zeros, 
    the second made of 10 ones and the last one made of 10 fives.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test array
    arr = np.arange(21)
    firstIndToChange = 9
    lastIndToChange = 15
    
    # change sign
    arrChanged = changeSign(arr, firstIndToChange, lastIndToChange)
    
    
    # Print section
    print("original array = {}".format(arr))
    print("array with changed sign = {}".format(arrChanged))
    
    
if __name__ == "__main__":
    main()
