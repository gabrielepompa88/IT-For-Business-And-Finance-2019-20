"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 30-Mar-2020
File name: Ex_Sheet_4_Num_4.py

Description: This script defines a DataFrame of two columns, one log-normal and 
the other normally distributed and verifies consistency.
"""

import numpy as np
import pandas as pd
import matplotlib.pylab as plt


def main():
    """
    Function main() define a DataFrame of 10^5 rows and 2 columns. 
    The first column, labelled `'X'`, is made of log-normal i.i.d. random
    numbers generated according to the following first two moments of the 
    underlying normal distribution: mean $\mu = 0.1$ and $\sigma = 1.1$ of the 
    underlying normal distribution. The second column, labelled `'Y = ln(X)'`, 
    is computed as the (elementwise) natural logarithm of column `'X'`. The 
    consistency of the random number generation is verified computing mean and
    standard deviation of column `'Y = ln(X)'`. Finally, two histograms, one 
    for each column are produced.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # parameters
    mu = 0.1
    sigma = 1.1
    N = int(10**6)
    
    # DataFrame of log-normal iid numbers
    df = pd.DataFrame(data=np.random.lognormal(mean=mu, sigma=sigma, size=N), 
                      columns=['X'])
    
    # new column of natural logarithms of 'X' column
    df['Y = ln(X)'] = np.log(df['X'])
    
    # calculations (all calculations are one-line. No need for dedicated functions)  
    y_mean = df['Y = ln(X)'].mean()
    y_std = df['Y = ln(X)'].std()
    
    # Print section ('\n' is to print on the next line)
    print("df.head() \n{}".format(df.head()))     # .head() method prints the first 5 few rows
    print("mean of Y=ln(X): {}".format(y_mean))
    print("standard deviation of Y=ln(X): {}".format(y_std))    
    
    # plot
    ax = df['X'].hist(bins=100, range=[0,20])
    ax.set_xlabel('X', fontsize=15) 
    ax.set_ylabel('counts', fontsize=15) 
    plt.show()
    
    ax = df['Y = ln(X)'].hist(bins=100)
    ax.set_xlabel('Y=ln(X)', fontsize=15) 
    ax.set_ylabel('counts', fontsize=15) 
    plt.show()
    
if __name__ == "__main__":
    main()
