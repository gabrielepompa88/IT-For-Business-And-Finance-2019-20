"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 24-Mar-2020
File name: Ex_Sheet_3_Num_4.py

Description: This script computes the mean, standard deviation, skewness and 
             kurtosis of the data of a given normally-distributed series.
"""

import numpy as np
import pandas as pd


def main():
    """
    Function main() computes the mean, standard deviation, skewness and 
    kurtosis of the data of a given normally-distributed series.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # parameters
    mu = 10
    sigma = 1.0
    N = 10
    
    # test series
    s = pd.Series(data=np.random.normal(loc=mu, scale=sigma, size=N))
    
    # calculations (all calculations are one-line. No need for dedicated functions)  
    s_mean = s.mean()
    s_std = s.std()
    s_skewness = s.skew()
    s_kurtosis = s.kurtosis()
    
    # Print section ('\n' is to print on the next line)
    print("s: \n{}".format(s))
    print("mean: {}".format(s_mean))
    print("standard deviation: {}".format(s_std))    
    print("skewness: {}".format(s_skewness))   
    print("kurtosis: {}".format(s_kurtosis))   
    
if __name__ == "__main__":
    main()
