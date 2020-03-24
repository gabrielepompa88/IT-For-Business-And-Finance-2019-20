"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 24-Mar-2020
File name: Ex_Sheet_3_Num_3.py

Description: This script changes the indexing of a given series.
"""

import copy # for copy.deepcopy()
import pandas as pd


def squaredIndex(ser):
    """
    Function squaredIndex(ser) returns series 'ser' reindexed according to
    the square of the elements of its own index
    
    Parameters:
        ser (pandas.Series): series to reindex
        
    Returns:
        ser (pandas.Series): reindexed series
        
    """
    
    ser.index = [i**2 for i in ser.index]
    
    return ser

def main():
    """
    Function main() changes the indexing of a given series.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test series
    s = pd.Series(data=[2, 4, 6, 8, 10])
    
    # calculations : copy.deepopy(s) makes a copy of s to pass it to squaredIndex
    # This is crucial, otherwise not only s_reindexed will have the new index,
    # but also s. Try to remove it and just 
    #
    # s_reindexed = squaredIndex(s)
    # 
    # to see how the printed indexes change...
    s_reindexed = squaredIndex(copy.deepcopy(s))
    
    # Print section ('\n' is to print on the next line)
    print("s: \n{}".format(s))
    print("s_reindexed: \n{}".format(s_reindexed))
    
if __name__ == "__main__":
    main()
