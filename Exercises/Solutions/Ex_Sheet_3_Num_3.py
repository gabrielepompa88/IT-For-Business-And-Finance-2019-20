"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 24-Mar-2020
File name: Ex_Sheet_3_Num_3.py

Description: This script changes the indexing of a given series.
"""

import pandas as pd


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
    
    # renaming of the index
    s_reindexed = s.rename(index = {i: i**2 for i in s.index})
    
    # Print section ('\n' is to print on the next line)
    print("s: \n{}".format(s))
    print("s_reindexed: \n{}".format(s_reindexed))
    
if __name__ == "__main__":
    main()
