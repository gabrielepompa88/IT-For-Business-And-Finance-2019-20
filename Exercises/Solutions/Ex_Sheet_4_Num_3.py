"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 30-Mar-2020
File name: Ex_Sheet_4_Num_3.py

Description: This script changes the indexing of a given DataFrame.
"""

import numpy as np
import pandas as pd


def main():
    """
    Function main() changes the indexing of a given DataFrame.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test DataFrame
    rows = 10
    cols = 5
    
    mat = np.array([[i**k for i in range(1,rows+1)] for k in range(1,cols+1)]).T
    dates = pd.date_range('2020-01-01', periods=rows, freq='B')
        
    df = pd.DataFrame(data=mat, 
                      index=dates, 
                      columns=['x', 'x^2', 'x^3', 'x^4', 'x^5'])

    # new index to use
    new_dates = pd.date_range('1988-06-01', periods=rows, freq='D')
    
    # renaming of the index
    df = df.rename(index = {old_d: new_d for old_d, new_d in zip(df.index, new_dates)})
    
    # Print section ('\n' is to print on the next line)
    print("df.head() \n{}".format(df.head()))     # .head() method prints the first 5 few rows
    
if __name__ == "__main__":
    main()
