"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_1.py

Description: This script computes the product of elements in a NumPy array.
"""

import numpy as np

def arrayMul(a):
    """
    Function arrayMul(a) computes and returns the product of elements in NumPy array a.
    
    Parameters:
        a (numpy.ndarray): input array.
    
    Returns:
        prod (float): product of the elements of array a.
    """
    
    # initialization for variable prod
    prod = 1.0
    
    for element in a:
        prod *= element # a *= b is equivalent to a = a * b
    
    return prod


def main():
    """
    Function main() defines a NumPy array and computes the product of its elements.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test array
    arr = np.array([10, 20, 30])
    
    # product of the elements in the array
    product = arrayMul(arr)
    
    # alternative computation - using the .prod() method
    productBuiltIn = arr.prod()
    
    # Print section
    print("Array = {} - Product of its elements = {}".format(arr, product))
    print("Array = {} - Product of its elements using .prod() = {}".format(arr, productBuiltIn))    

if __name__ == "__main__":
    main()