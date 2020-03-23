"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 23-Mar-2020
File name: Ex_Sheet_2_Num_7.py

Description: This script creates matrices with diagonal and off-diagonal elements set.
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
    Function main() generates a 4x4 matrix with zeros onthe main diagonal and ones otherwise.
    It uses function iniMatrix as in Ex_Sheet_2_Num_5.py
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test variables
    size = 4
    diagVal = 0
    offDiagVal = 1
    
    # matrix generated
    matrix = initMatrix(n=size, diagonalValue=diagVal, offDiagonalValue=offDiagVal)
        
    # Print section ('\n' is to print on the next line)
    print("matrix: \n {}".format(matrix))
    
    
if __name__ == "__main__":
    main()
