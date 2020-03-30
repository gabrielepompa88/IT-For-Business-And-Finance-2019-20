"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 30-Mar-2020
File name: Ex_Sheet_4_Num_1.py

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
    magic_matrix = np.array([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10 , 5], [9, 6, 15, 4]])

    df_magic = pd.DataFrame(data=magic_matrix, 
                            index=['Row_' + str(i) for i in range(1,5)],
                            columns=['Col_' + str(i) for i in range(1,5)])
    
    col_wise_sum = df_magic.sum()
    row_wise_sum = df_magic.sum(axis=1)
    main_diag_sum = np.diag(df_magic).sum()
    other_diag_sum = np.diag(np.fliplr(df_magic)).sum()
    
    # Print section ('\n' is to print on the next line)
    print("df_magic \n{}".format(df_magic))   
    print("Sum of each row \n{}".format(col_wise_sum))
    print("Sum of each column \n{}".format(row_wise_sum))
    print("Sum of the main diagonal \n{}".format(main_diag_sum))
    print("Sum of the other diagonal \n{}".format(other_diag_sum))
    
        
if __name__ == "__main__":
    main()
