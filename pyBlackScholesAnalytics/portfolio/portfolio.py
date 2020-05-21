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
        
        # initialize underlying value, strikes and times-to-maturity attributes
        self.__S = None
        self.__K = np.array([])
        self.__tau = np.array([])
        self.is_multi_horizon = False
        
    def __repr__(self):
        return self.get_info()
    
    # getters
    def get_info(self):
        return self.__info
    
    def get_mkt_info(self):
        return self.__mkt_info
    
    def get_K(self):
        return self.__K
    
    def get_S(self):
        return self.__S

    def get_tau(self):
        return self.__tau
    
    def get_composition(self):
        return self.__composition
    
    # setters
    def set_S(self, S):
        self.__S = S
        
    # composition method
    def add_instrument(self, FinancialInstrument, position):
        
        long_short = 'Long' if position > 0 else 'Short'
        instrument_info = long_short + " {} ".format(abs(position)) + FinancialInstrument.get_info()
        
        self.__composition.append({"instrument": FinancialInstrument,
                                   "position":   position,
                                   "info":       instrument_info})
        
        # update portfolio info strings
        self.__update_info(FinancialInstrument, position)
        
        # update portfolio attributes
        self.__update_S(FinancialInstrument)
        self.__update_K(FinancialInstrument)
        self.__update_tau(FinancialInstrument)
    
    # private method to update the info
    def __update_info(self, fin_inst, pos):
        self.__info += self.__composition[-1]["info"] + "\n"
        if self.__mkt_info is None:
            self.__mkt_info = fin_inst.get_mkt_info()
            
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
        # check if the portfolio is a multi-horizon portfolio
        if len(self.__tau) > 1:
            self.is_multi_horizon = True
                    
    def __check_time_parameter(self, *args, **kwargs):
        
        # time parameter:
        time_param = args[1] if len(args) > 1 \
                        else kwargs['tau'] if 'tau' in kwargs \
                            else (kwargs['t'] if 't' in kwargs else None)
        
        # check that no multiple time parameters in input
        if is_iterable_not_string(time_param):
            raise NotImplementedError("No multiple time parameters allowed: {} given in input.".format(time_param))
            
        # check that time parameter is not a time-to-maturity if the portfolio is multi-horizon:
        if self.is_multi_horizon and is_numeric(time_param):
            raise NotImplementedError("No time-to-maturity time parameter allowed for multi-horizon \n{} \ntau={} given in input"\
                                      .format(self, time_param))  
            
    # portfolio "payoff", that is expiration value
    def payoff(self, *args, **kwargs):
        """
        Returns the portfolio payoff as the scalar product (i.e. sum of elementwise products) 
        between single instrument payoffs and positions.
        
        As single instruments .payoff(), can be called with single/multiple 'S' and single 't' or 'tau'. 
        """
           
        # check time parameter
        self.__check_time_parameter(*args, **kwargs)
              
        if self.get_composition(): 

            # single instrument payoffs and positions
            payoffs = np.array([inst["instrument"].payoff(*args, **kwargs) for inst in self.get_composition()])
            positions = np.array([inst["position"] for inst in self.get_composition()])
            
            return positions.dot(payoffs)
            
        else: # if portfolio is empty returns 0
            
            return 0.0  
        
    # portfolio value (called 'price' as for single options, to implement polymorphism)
    def price(self, *args, **kwargs):
        """
        Returns the portfolio value as the scalar product (i.e. sum of elementwise products) 
        between single instrument prices and positions.
        
        As single instruments .price(), can be called with single/multiple 'S' and single 't' or 'tau'. 
        """
        
        # check time parameter
        self.__check_time_parameter(*args, **kwargs)
                                      
        if self.get_composition(): 

            # single instrument prices and positions
            prices = np.array([inst["instrument"].price(*args, **kwargs) for inst in self.get_composition()])
            positions = np.array([inst["position"] for inst in self.get_composition()])
            
            return positions.dot(prices)
            
        else: # if portfolio is empty returns 0
            
            return 0.0  
        
    # portfolio P&L
    def PnL(self, *args, **kwargs):
        """
        Returns the portfolio Profit & Loss as the scalar product (i.e. sum of elementwise products) 
        between single instrument P&Ls and positions.
        
        As single instruments .PnL(), can be called with single/multiple 'S' and single 't' or 'tau'. 
        """
                
        # check time parameter
        self.__check_time_parameter(*args, **kwargs)
                                      
        if self.get_composition(): 

            # single instrument P&Ls and positions
            pnls = np.array([inst["instrument"].PnL(*args, **kwargs) for inst in self.get_composition()])
            positions = np.array([inst["position"] for inst in self.get_composition()])
            
            return positions.dot(pnls)
            
        else: # if portfolio is empty returns 0
            
            return 0.0  
