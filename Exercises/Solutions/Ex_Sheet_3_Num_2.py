"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 24-Mar-2020
File name: Ex_Sheet_3_Num_2.py

Description: This script create a subset of a given series based on value and 
             greater-or-equal condition.
"""

import numpy as np
import pandas as pd


def main():
    """
    Function main() create a subset of a given series based on value and 
    greater-or-equal condition.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test series
    s = pd.Series(data=[i**2 for i in np.arange(1,11)])
    value = 10
    
    # calculations (all calculations are one-line. No need for dedicated functions)  
    s_filtered = s[s >= value]
    
    # Print section ('\n' is to print on the next line)
    print("s: \n{}".format(s))
    print("s_filtered \n{}".format(s_filtered))
    
if __name__ == "__main__":
    main()
