"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 24-Mar-2020
File name: Ex_Sheet_3_Num_1.py

Description: This script implements addition, subtraction, multiplication and 
             division of two Pandas Series.
"""

import pandas as pd


def main():
    """
    Function main() implements addition, subtraction, multiplication and 
    division of two Pandas Series.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test series
    s1 = pd.Series(data=[2, 4, 6, 8, 10])
    s2 = pd.Series(data=[1, 3, 5, 7, 9])
    
    # calculations (all calculations are one-line. No need for dedicated functions)  
    s_1plus2 = s1 + s2
    s_1minus2 = s1 - s2
    s_1times2 = s1 * s2
    s_1over2 = s1 / s2
    
    # Print section ('\n' is to print on the next line)
    print("s1: \n{}".format(s1))
    print("s2 \n{}".format(s2))
    print("s1+s2 \n{}".format(s_1plus2))
    print("s1-s2 \n{}".format(s_1minus2))
    print("s1*s2 \n{}".format(s_1times2))    
    print("s1/s2 \n{}".format(s_1over2))    
    
if __name__ == "__main__":
    main()
