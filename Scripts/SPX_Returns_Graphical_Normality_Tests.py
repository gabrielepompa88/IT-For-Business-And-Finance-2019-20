"""
Author: Gabriele Pompa
mail: gabriele.pompa@unisi.it

Date: 11-Apr-2020
File name: SPX_Returns_Graphical_Normality_Tests.py

Description: This script provides some graphical evidence against normality of
S&P500 returns using data since Jan 1st, 1985.
"""

import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def importData(ticker):
    """
    Utility function importData(ticker) returns the close price data for 
    'ticker' Stock.
    
    Parameters:
        ticker (String): desired Stock ticker,

    Returns:
        closePriceTicker (pd.DataFrame): close prices of 'ticker' Stock.
        
    """
    
    dataFolderPath = "../Data"
    filePath = os.path.join(dataFolderPath, "Securities_Close_Price_Dataset.csv")
    closePriceAllStocks = pd.read_csv(filepath_or_buffer = filePath, index_col = 0, parse_dates = True)
    closePriceTicker = closePriceAllStocks.loc[:, ticker].dropna()
    
    return closePriceTicker

def getLogRets(df):
    """
    Utility function getLogRets(df) computes one-period log-returns of DataFrame
    'df'.
    
    Parameters:
        dfRets (pd.DataFrame): level data,

    Returns:
        logRetsDf (pd.DataFrame): log-returns,
        
    """
    logRetsDf = np.log(df/df.shift(periods=1))  
    
    return logRetsDf

def resampleRets(dfRets, days):
    """
    Function resampleRets(dfRets, days) gets in input the 'dfRets' DataFrame
    of log-returns and the resampling frequency String 'days'. It then returns
    the dfRets resampled, using a .sum() aggregation to compute compound returns
    over a horizon of 'days'. It drops NaNs.
    
    Parameters:
        dfRets (pd.DataFrame): log-returns,
        days (String): resampling frequency.

    Returns:
        resampledRets (pd.DataFrame): log-returns resampled,
        
    """    
    
    resampledRets = dfRets.resample(rule=days+'B', label='right', closed='right').sum().dropna()
    
    return resampledRets

def normalFit(dfRets):
    """
    Function normalFit(dfRets) gets in input the 'dfRets' DataFrame
    of log-returns. It then:
        - makes a normal fit of dfRets;
        - compute the normal pdf, with fit mean and std, over a uniform grid of returns;
        - computes higher sample moments: skewness and (excess) kurtosis
    
    Parameters:
        dfRets (pd.DataFrame): log-returns,
    
    Returns:
        fitRes (Dict): normal fit results, from normalFit() function;
        
    """    
        
    # normal fit
    mu_fit, sigma_fit = stats.norm.fit(dfRets.values)

    # create a uniform grid of points between minimum and maximum values of dfRets
    num_points = dfRets.shape[0]
    df_unif_grid = np.linspace(dfRets.min(), dfRets.max(), num_points)
    
    # fit normal pdf
    pdf_fit = stats.norm.pdf(df_unif_grid, loc=mu_fit, scale=sigma_fit)
    
    # higher sample moments
    sample_skewness = dfRets.skew()
    sample_kurtosis = dfRets.kurtosis()
    
    # wrapping output in a Dict
    fitRes = {'mu_fit':    mu_fit, 
              'sigma_fit': sigma_fit,
              'sample_skew':  sample_skewness,
              'sample_kurt':  sample_kurtosis,
              'returns_grid': df_unif_grid,
              'pdf(returns_grid)': pdf_fit}
    
    return fitRes

def makePlots(dfRets, fitRes, days):
    """
    Function makePlots(dfRets, fitRes, days) gets in input the 'dfRets' DataFrame
    of log-returns, the normal fit results Dict 'fitRes' and the resampling 
    frequency String 'days'. It then:
        - makes a normalized histogram of dfRets, using a number of bins = sqrt(number of data);
        - compares the histogram with the best normal fit;
        - makes a Q-Q plot of dfRets quantiles, against normal hypothesis.
    
    Parameters:
        dfRets (pd.DataFrame): log-returns,
        fitRes (Dict): normal fit results, from normalFit() function;
        days (String): resampling frequency.
    
    Returns:
        None
        
    """    
    
    fig, axs = plt.subplots(figsize=(20,6), nrows=1, ncols=2)
    
    # Histogram
    bin_num = math.ceil(math.sqrt(dfRets.shape[0]))
    axs[0].hist(x=dfRets.values, bins=bin_num, density=True, histtype='bar', ec='black',
                label="Empirical (skew={:.2f}, excess kurt={:.2f})".format(fitRes['sample_skew'], fitRes['sample_kurt']))
    
    axs[0].plot(fitRes['returns_grid'], fitRes['pdf(returns_grid)'], '--', lw=2, 
                label="Normal fit $N(z;\mu={:.2f}, \sigma={:.2f})$ pdf".format(fitRes['mu_fit'], fitRes['sigma_fit']))
    
    axs[0].set_title("Histogram of S&P500 log-returns ({} days resample)".format(days), fontsize=20)
    axs[0].set_xlabel("Returns", fontsize=20)
    axs[0].set_ylabel("Frequency", fontsize=20)
    axs[0].set_xlim(-0.2, 0.4)
    axs[0].set_ylim(0.0, 26)
    axs[0].legend(loc='upper right', ncol=1, fontsize=12)
    
    
    # Q-Q plot
    stats.probplot(x=dfRets.values, dist='norm', plot=axs[1])
    axs[1].set_title("Q-Q plot of S&P500 log-returns ({} days resample) against Normal distribution".format(days))
    axs[1].set_xlabel("Theoretical Quantiles", fontsize=20)
    axs[1].set_ylabel("Sample Quantiles", fontsize=20)
    axs[1].set_xlim(-4, 4)
    axs[1].set_ylim(-0.4, 0.4)
    
    fig.tight_layout()
    plt.show()
    
def main():
    """
    Function main():
        - defines a list of resampling frequencies: resamplingFreqList;
        - gets stock data, using importData() function;
        - computes log-returns, using getLogRets() function; 
        - resamples log-returns, using resampleRets() function;
        - makes a normal fit of log-returns, using normalFit() function;
        - makes two plots, a histogram and a Q-Q plot, using makePlots() function;
    
    Parameters:
        None
    
    Returns:
        None
        
    """    
    
    # resampling business days
    resamplingFreqList = [5, 21, 63, 126, 252]
    
    # get single ticker data: here S&P500
    closePrice = importData('^GSPC')
    
    # compute log returns
    dfRets = getLogRets(closePrice)
    
    # loop over desired resampling frequencies
    for d in resamplingFreqList:
        
        # resampling
        resampledDfRets = resampleRets(dfRets, str(d))
        
        # normal fit
        fitResults = normalFit(resampledDfRets)
        
        # make histogram and Q-Q plot
        makePlots(resampledDfRets, fitResults, d)

if __name__ == "__main__":
    main()
