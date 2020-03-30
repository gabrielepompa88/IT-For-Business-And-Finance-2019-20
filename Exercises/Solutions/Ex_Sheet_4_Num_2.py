"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 30-Mar-2020
File name: Ex_Sheet_4_Num_2.py

Description: This script filters rows of a given DataFrame based on value and 
             smaller-or-equal condition applied to the first column. 
             Then, select second and last columns.
"""

import numpy as np
import pandas as pd


def main():
    """
    Function main() filters rows of a given DataFrame based on value and 
    smaller-or-equal condition applied to the first column. 
    Then, select second and last columns.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test DataFrame
    rows = 10
    cols = 5
    
    mat_decimal = np.array([[i**k for i in np.linspace(0,2,rows)] for k in range(1,cols+1)]).T
    x_axis = [i for i in np.linspace(0,2,10)]
        
    df_decimal = pd.DataFrame(data = mat_decimal,
                              index = x_axis, 
                              columns=['x', 'x^2', 'x^3', 'x^4', 'x^5'])
    value = 1.5
    
    # calculations (all calculations are one-line. No need for dedicated functions)  
    df_decimal_rows_filtered = df_decimal[df_decimal['x'] <= value]
    df_decimal_rows_and_cols_filtered = df_decimal_rows_filtered.iloc[:, [1,-1]]
    
    # Print section ('\n' is to print on the next line)
    print("df_decimal \n{}".format(df_decimal))     
    print("df_decimal_rows_filtered \n{}".format(df_decimal_rows_filtered)) 
    print("df_decimal_rows_and_cols_filtered \n{}".format(df_decimal_rows_and_cols_filtered)) 
        
if __name__ == "__main__":
    main()
