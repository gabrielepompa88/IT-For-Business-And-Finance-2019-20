"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 24-Mar-2020
File name: Ex_Sheet_3_Num_5.py

Description: This script computes the mean, standard deviation of the data of 
a given log-normally-distributed series.
"""

import numpy as np
import pandas as pd


def main():
    """
    Function main() computes the mean, standard deviation of the data of a 
    given log-normally-distributed series.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # parameters
    mu = np.log(30)
    sigma = np.log(1.1)
    N = 10
    
    # test series
    s = pd.Series(data=np.random.lognormal(mean=mu, sigma=sigma, size=N))
    
    # calculations (all calculations are one-line. No need for dedicated functions)  
    s_mean = s.mean()
    s_std = s.std()
    
    # Print section ('\n' is to print on the next line)
    print("s: \n{}".format(s))
    print("mean: {}".format(s_mean))
    print("standard deviation: {}".format(s_std))    
    
if __name__ == "__main__":
    main()
