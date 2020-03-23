"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_4.py

Description: This script creates matrices with diagonal and off-diagonal values set
"""

import numpy as np

def initMatrix(n, diagonalValue, offDiagonalValue):
    """
    Function initMatrix(diagonalValue, offDiagonalValue) initializes a square 
    matrix of with 'n' rows and cols filled with value 'diagonalValue' on the 
    main diagonal and with 'offDiagonalValue' elsewhere.
    
    Parameters:
        n (int): order of the matrix 'M'
        diagonalValue (float): value on the diagonal of the matrix 'M'    
        offDiagonalValue (float): value off the diagonal of the matrix 'M'    

    Returns:
        M (numpy.ndarray): 2-dimensional array created as per above  
    """
    
    # nxn identity matrix
    I = np.eye(n)

    return diagonalValue*I + offDiagonalValue*(1-I)
    

def main():
    """
    Function main() first a 3x3 identity matrix and then 3x3 matrix filled with
    2 on the diagonal and 1 otherwise
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test variables
    size = 3
    diagVal = 2
    offDiagVal = 1
    
    # matrix generated
    identityMatrix = np.eye(size) # equivalent to initMatrix(size, 1, 0) but of course more efficient
    otherMatrix = initMatrix(n=size, diagonalValue=diagVal, offDiagonalValue=offDiagVal)
        
    # Print section ('\n' is to print on the next line)
    print("Identity matrix: \n {}".format(identityMatrix))
    print("Other matrix: \n {}".format(otherMatrix))
    
    
if __name__ == "__main__":
    main()
