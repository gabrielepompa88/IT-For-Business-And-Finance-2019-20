"""
Author: Gabriele Pompa (gabriele.pompa@gmail.com)

Date: 20-May-2020
File name: portfolio.py
"""

# ----------------------- standard imports ---------------------------------- #
# for NumPy arrays
import numpy as np

# ----------------------- sub-modules imports ------------------------------- #

from utils.utils import *

#-----------------------------------------------------------------------------#

class Portfolio:
    """
    Portfolio class modeling a portfolio of options. It implements an aggregation of EuropeanOption sub-classes 
    defining the .add_instrument() composition method which takes in input a FinancialInstrument (either PlainVanillaOption or 
    DigitalOption) to be added to the portfolio.
    
    Attributes:
    -----------
    
        composition (List of Dicts): List of Dicts, each describing a single constituent FinancialInstrument, together
                                     with the position the portfolio is holding on it.
        info and mkt_info (Strings): information labels on portfolio and constituent instruments.
        S (Float):                   underlying value when the portfolio is formed.
        K (np.ndarray):              Strikes of constituent options.
        tau (np.ndarray):            Time(s) to maturity of constituent options, when the portfolio is formed.
        is_multi_horizon (Bool):     True if constituent options have different expiration dates.
        
    Public Methods:
    --------
    
        getters for all attributes
        
        setters for common attributes, not belonging to mkt_env
        
        payoff: float
            Computes the payoff of the portfolio.

        price: float
            Computes the value of the portfolio.

        PnL: float
            Computes the P&L of the portfolio.
    """
    
    def __init__(self, name="Dummy"):
        
        # initialize an empty portfolio
        self.__composition = []
        
        # initialize empty info strings
        self.__info = "{} Portfolio: \n".format(name)
        self.__mkt_info = None
        
        # initialize valuation date, underlying value, strikes and times-to-maturity attributes
        self.__t = None
        self.__T = np.array([])
        self.__S = None
        self.__K = np.array([])
        self.__tau = np.array([])
        self.is_multi_horizon = False
        self.is_empty = True
        
    def __repr__(self):
        return self.get_info()
    
    # 
    # getters
    #
    
    def get_info(self):
        return self.__info
    
    def get_mkt_info(self):
        return self.__mkt_info
    
    def get_t(self):
        return self.__t
    
    def get_T(self):
        return scalarize(self.__T)

    def get_K(self):
        return self.__K
    
    def get_S(self):
        return self.__S

    def get_tau(self):
        return self.__tau
    
    def get_composition(self):
        return self.__composition
    
    #
    # setters
    #
    
    def set_t(self, t):
        self.__t = t
        
    def set_S(self, S):
        self.__S = S
        
    #
    # Composition method
    #
    
    def add_instrument(self, FinancialInstrument, position):

        if self.is_empty:
            self.is_empty = False
        
        long_short = 'Long' if position > 0 else 'Short'
        instrument_info = long_short + " {} ".format(abs(position)) + FinancialInstrument.get_info()
        
        self.__composition.append({"instrument": FinancialInstrument,
                                   "position":   position,
                                   "info":       instrument_info})
            
        # update portfolio info strings
        self.__update_info(FinancialInstrument, position)
        
        # update portfolio attributes
        self.__update_t(FinancialInstrument)
        self.__update_T(FinancialInstrument)
        self.__update_S(FinancialInstrument)
        self.__update_K(FinancialInstrument)
        self.__update_tau(FinancialInstrument)
    
    # 
    # Private methods
    #
    
    def __update_info(self, fin_inst, pos):
        self.__info += self.__composition[-1]["info"] + "\n"
        if self.__mkt_info is None:
            self.__mkt_info = fin_inst.get_mkt_info()
            
    def __update_t(self, fin_inst):
        if self.get_t() is None:
            self.set_t(fin_inst.get_t())
        else:
            if self.get_t() != fin_inst.get_t():
                raise ValueError("No multiple valuation dates in input allowed: \n\n current: {}, \n\n other given input: {}"\
                                      .format(self, self.get_t(), fin_inst.get_t()))
    
    def __update_T(self, fin_inst):
        expiration_dates = np.append(self.get_T(), fin_inst.get_T())
        # filter only distinct strikes
        self.__T = iterable_to_numpy_array(np.unique(expiration_dates), sort_func=date_string_to_datetime_obj)
        # check if the portfolio is a multi-horizon portfolio
        if len(self.__T) > 1:
            self.is_multi_horizon = True
            
    def __update_S(self, fin_inst):
        if self.get_S() is None:
            self.set_S(fin_inst.get_S())
            
    def __update_K(self, fin_inst):
        # append new instrument strike
        strikes = np.append(self.get_K(), fin_inst.get_K())
        # filter only distinct strikes
        self.__K = np.unique(strikes)

    def __update_tau(self, fin_inst):
        # append new instrument tau
        times_to_maturity = np.append(self.get_tau(), fin_inst.get_tau())
        # filter only distinct times-to-maturity
        self.__tau = np.unique(times_to_maturity)
        # consistency check
        if (len(self.__tau) > 1) and (not self.is_multi_horizon):
            raise AttributeError("Multi-horizon portfolio not properly handled: \n \tau = {}"\
                                 .format(self.__tau)) 
    
    def check_parameters(self, *args, **kwargs):
        """"Check both x-axis and time dimensional parameters."""
        
        # check x-axis
        self.__check_x_axis(self, *args, **kwargs)

        # check time parameter
        self.__check_time_parameter(self, *args, **kwargs)
            
    def __check_x_axis(self, *args, **kwargs):
        """Check that no Strike-price variable is used to span the x-axis. 
        This is something not well defined for portfolio with multi-strike options constituents,
        and admissible but no so meaningful for single-strike portfolios (e.g. calendar spreads).
        We decided to disallow tout-court the feature."""
        
        if "K" in kwargs:
            raise NotImplementedError("No Strike-price pricing parameter allowed.")
                          
    def __check_time_parameter(self, *args, **kwargs):
        """"Check that multi-horizon portfolio do not get time(s)-to-maturity as input time parameter"""
        
        # time parameter:
        time_param = args[1] if len(args) > 1 \
                        else kwargs['tau'] if 'tau' in kwargs \
                            else (kwargs['t'] if 't' in kwargs else None)
        
        # Case of no time parameter in input allowed: sigma x r grid case
        if time_param is not None:
            
            # check that time parameter is not a time-to-maturity if the portfolio is multi-horizon:
            if self.is_multi_horizon and is_numeric(time_param):
                raise TypeError("No time-to-maturity time parameter allowed for multi-horizon portfolio \n\n tau={} given in input"\
                                .format(self, time_param))  
            
    #
    # Public methods
    #

    def time_to_maturity(self, *args, **kwargs):
        """
        Utility method to compute time-to-maturity of the portfolio, 
        if possible (that is, if the portfolio is not multi-horizon and if it's
        not empty. Method taken from an instrument.
        """
        
        if self.is_empty:
            raise NotImplementedError("No time-to-maturity defined for empty portfolio") 
        elif self.is_multi_horizon:
            raise NotImplementedError("No time-to-maturity defined for multi-horizon portfolio")  
        else:
            return self.get_composition()[0]["instrument"].time_to_maturity(*args, **kwargs)
            
    def payoff(self, *args, **kwargs):
        """
        Returns the portfolio payoff as the scalar product (i.e. sum of elementwise products) 
        between single instrument payoffs and positions.
        
        As single instruments .payoff(), can be called with single/multiple 'S'. 
        """
           
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio payoff is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].payoff(*args, **kwargs) for inst in self.get_composition()])
              
    def price(self, *args, **kwargs):
        """
        Returns the portfolio value as the scalar product (i.e. sum of elementwise products) 
        between single instrument prices and positions.
        
        As single instruments .price(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
        
        # check parameters
        self.check_parameters(*args, **kwargs)
        
        # portfolio price is the sum position * instrument_price
        return sum([inst["position"]*inst["instrument"].price(*args, **kwargs) for inst in self.get_composition()])
                                      
    def PnL(self, *args, **kwargs):
        """
        Returns the portfolio Profit & Loss as the scalar product (i.e. sum of elementwise products) 
        between single instrument P&Ls and positions.
        
        As single instruments .PnL(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
                
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio P&L is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].PnL(*args, **kwargs) for inst in self.get_composition()])

    def delta(self, *args, **kwargs):
        """
        Returns the portfolio Delta as the scalar product (i.e. sum of elementwise products) 
        between single instrument Deltas and positions.
        
        As single instruments .delta(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
                
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio delta is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].delta(*args, **kwargs) for inst in self.get_composition()])

    def theta(self, *args, **kwargs):
        """
        Returns the portfolio Theta as the scalar product (i.e. sum of elementwise products) 
        between single instrument Thetas and positions.
        
        As single instruments .theta(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
                
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio theta is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].theta(*args, **kwargs) for inst in self.get_composition()])

    def gamma(self, *args, **kwargs):
        """
        Returns the portfolio Gamma as the scalar product (i.e. sum of elementwise products) 
        between single instrument Gammas and positions.
        
        As single instruments .gamma(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
                
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio gamma is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].gamma(*args, **kwargs) for inst in self.get_composition()])

    def vega(self, *args, **kwargs):
        """
        Returns the portfolio Vega as the scalar product (i.e. sum of elementwise products) 
        between single instrument Vegas and positions.
        
        As single instruments .vega(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
                
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio vega is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].vega(*args, **kwargs) for inst in self.get_composition()])

    def rho(self, *args, **kwargs):
        """
        Returns the portfolio Rho as the scalar product (i.e. sum of elementwise products) 
        between single instrument Rhos and positions.
        
        As single instruments .rho(), can be called with single/multiple 'S' and single/multiple 't' or 'tau'. 
        """
                
        # check parameters
        self.check_parameters(*args, **kwargs)

        # portfolio rho is the sum position * instrument_payoff
        return sum([inst["position"]*inst["instrument"].rho(*args, **kwargs) for inst in self.get_composition()])
