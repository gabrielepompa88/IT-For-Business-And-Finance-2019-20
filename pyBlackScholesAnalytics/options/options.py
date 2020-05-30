"""
Author: Gabriele Pompa (gabriele.pompa@gmail.com)
Date: 20-May-2020
File name: options.py
"""

# ----------------------- standard imports ---------------------------------- #
# for NumPy arrays
import numpy as np

# for Pandas Series and DataFrame
import pandas as pd

# for statistical functions
from scipy import stats

# for some mathematical functions
import math

# for date management
import datetime as dt

# for warning messages
import warnings

# ----------------------- sub-modules imports ------------------------------- #

from utils.utils import *

#-----------------------------------------------------------------------------#

class EuropeanOption:
    """
    EuropeanOption abstract class: an interface setting the template for any option with european-style exercise.
    It uses a MarketEnvironment object to define the current market conditions under which the option is modeled. 
    This class is not meant to be instantiated.
    
    Attributes:
    -----------
        mkt_env (MarketEnvironment): Instance of MarketEnvironment class
        type (str):                  Optional. Type of the option. Can be either 'call' or 'put';
        S_t (float):                 'S' attribute of mkt_env.
        K (float):                   Optional. Strike price;
        t (str; dt.datetime):        't' attribute of mkt_env.
        T (str; dt.datetime):        Optional. Expiration date. Can be either a "dd-mm-YYYY" String or a dt.datetime object
        tau (float):                 time to maturity in years, computed as tau=T-t by time_to_maturity() method
        r (float):                   'r' attribute of mkt_env.
        sigma (float):               'sigma' attribute of mkt_env.

    Public Methods:
    --------
    
        time_to_maturity: float
            Computes the time-to-maturity of the option.
        
        process_input_parameters: float
            Parses underlying, time, volatility and short-rate parameters, 
            discriminating between time-to-maturity and valuation date
            time parameter.
    
        d1_and_d2: flaot, float
            Computes the d1 and d2 terms of Black-Scholes pricing formula

        PnL: float
            Computes the P&L of the option.

    Template Methods:
    --------   
    
        getters for all common attributes
        
        setters for common attributes, not belonging to mkt_env
        
        payoff: float
            Template method for payoff. Raises NotImplementedError if called.

        price_upper_limit: float 
            Template method for upper limit. Raises NotImplementedError if called.

        price_lower_limit: float 
            Template method for lower limit. Raises NotImplementedError if called.
            
        price: float
            Template method for price. Raises NotImplementedError if called.

    """

    def __init__(self, mkt_env, option_type='call', K=100.0, T="31-12-2020"):
        
        print("Initializing the EuropeanOption!")

        # option type check
        if option_type not in ['call', 'put']:
            raise NotImplementedError("Option Type: '{}' does not exist!".format(option_type))
        
        self.__type  = option_type
        self.__S     = mkt_env.get_S()
        self.__K     = K
        self.__t     = mkt_env.get_t()
        self.__T     = date_string_to_datetime_obj(T)
        self.__tau   = self.time_to_maturity()
        self.__r     = mkt_env.get_r()
        self.__sigma = mkt_env.get_sigma()
        
        # empty initial price of the option
        self.__initial_price = None
               
        # empty informations dictionary
        self.__docstring_dict = {}        
        
    # string representation method template
    def __repr__(self):
        raise NotImplementedError()
    
    # getters
    def get_type(self):
        return self.__type

    def get_S(self):
        return self.__S
    
    def get_K(self):
        return self.__K
    
    def get_t(self):
        return self.__t

    def get_T(self):
        return self.__T

    def get_tau(self):
        return self.__tau

    def get_r(self):
        return self.__r
    
    def get_sigma(self):
        return self.__sigma
        
    def get_initial_price(self):
        return NotImplementedError()
    
    # doctring getter template
    def get_docstring(self, label):
        raise NotImplementedError()

    # setters
    def set_type(self, option_type):
        self.__type = option_type
        
        # option type check
        if option_type not in ['call', 'put']:
            raise NotImplementedError("Option Type: '{}' does not exist!".format(option_type))
            
    def set_K(self, K):
        self.__K = K
    
    def set_T(self, T):
        self.__T = date_string_to_datetime_obj(T)
        # update time to maturity, given changed T, to keep internal consistency
        self.__update_tau() 
    
    def set_tau(self, tau):
        self.__tau = tau
        # update expiration date, given changed tau, to keep internal consistency
        self.__update_T()
        
    # update methods (private)
    def __update_tau(self):
        self.__tau = self.time_to_maturity()

    def __update_T(self):
        self.__T = self.__t + dt.timedelta(days=math.ceil(self.__tau*365))

    # utility methods
    def time_to_maturity(self, *args, **kwargs):
        """
        Utility method to compute time-to-maturity
        """
        
        # parsing optional parameters
        t = args[0] if len(args) > 0 else kwargs['t'] if 't' in kwargs else self.get_t()
        T = args[1] if len(args) > 1 else kwargs['T'] if 'T' in kwargs else self.get_T()
        
        # convert to dt.datetime objects, if needed
        t = date_string_to_datetime_obj(t)
        T = date_string_to_datetime_obj(T)
        
        # compute and return time to maturity (in years)
        return (T-t).days / 365.0
    
    def process_input_parameters(self, *args, **kwargs):
        """
        Utility method to parse underlying, time, volatility and short-rate parameters
        """

        # underlying value 
        S = args[0] if len(args) > 0 else kwargs['S'] if 'S' in kwargs else self.get_S()
        
        # homogenize underlying in input
        S = homogenize(S)
                    
        # time parameter:
        time_param = args[1] if len(args) > 1 \
                     else kwargs['tau'] if 'tau' in kwargs \
                        else (kwargs['t'] if 't' in kwargs else None)
                                
        # time parameter interpretation (and homogenization) according to its type        
        # case 1: no time-parameter in input
        if time_param is None:
            tau = time_param = self.get_tau()
        # case 2: valid time-to-maturity in input
        elif is_numeric(time_param):
            time_param = homogenize(time_param)
            tau = time_param
        # case 3: valuation date in input, to be converted into time-to-maturity
        elif is_date(time_param):
            time_param = homogenize(time_param, sort_func=date_string_to_datetime_obj)
            tau = self.time_to_maturity(t=time_param)
        # error case: the time parameter in input has a data-type that is not recognized
        else: 
            raise TypeError("Type {} of input time parameter not recognized".format(type(time_param)))
                    
        # squeeze output flag
        np_output = kwargs['np_output'] if 'np_output' in kwargs else True
        
        # make S and tau coordinated np.ndarray or pd.DataFrames, 
        # if necessary creating a (S, tau) grid
        S, tau = coordinate(x=S, y=tau, np_output=np_output, 
                            col_labels=S, ind_labels=time_param)

        # checking whether any value in S is smaller than zero. Works if S is scalar too.
        if np.any(S < 0):
            warnings.warn("Warning: S = {} < 0 value encountered".format(S))

        # checking whether any value in tau is smaller than zero. Works if tau is scalar too.
        if np.any(tau < 0):
            warnings.warn("Warning: tau = {} < 0 value encountered".format(tau))
            
        # underlying volatility 
        sigma = kwargs['sigma'] if 'sigma' in kwargs else self.get_sigma()

        # short rate
        r = kwargs['r'] if 'r' in kwargs else self.get_r()
        
        return {"S": S, 
                "tau": tau, 
                "sigma": sigma, 
                "r": r, 
                "np_output": np_output}
    
    # d1 and d2 terms
    def d1_and_d2(self, *args, **kwargs):
        """
        Utility method to compute d1 and d2 terms of Black-Scholes pricing formula
        """
        
        # parsing optional parameters
        S     = args[0] if len(args) > 0 else kwargs['S'] if 'S' in kwargs else self.get_S()
        tau   = args[1] if len(args) > 1 else kwargs['tau'] if 'tau' in kwargs else self.get_tau()
        K     = args[2] if len(args) > 2 else kwargs['K'] if 'K' in kwargs else self.get_K()
        r     = args[3] if len(args) > 3 else kwargs['r'] if 'r' in kwargs else self.get_r()
        sigma = args[4] if len(args) > 4 else kwargs['sigma'] if 'sigma' in kwargs else self.get_sigma()
            
        # compute d1 and d2
        d1 = (np.log(S/K) + (r + 0.5 * sigma ** 2) * tau) / (sigma * np.sqrt(tau))
        d2 = d1 - sigma * np.sqrt(tau)

        return d1, d2
    
    # payoff template
    def payoff(self):
        raise NotImplementedError()     
        
    # upper price limit template
    def price_upper_limit(self):
        raise NotImplementedError()     

    # lower price limit template
    def price_lower_limit(self):
        raise NotImplementedError()     
        
    # price template
    def price(self):
        raise NotImplementedError()
        
    # profit and loss calculation calculation - with optional *args and **kwargs parameters
    def PnL(self, *args, **kwargs):
        """
        Can be called using (underlying, time-parameter), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
            
        - time-parameter can be specified either as the 2nd positional argument or as keyboard argument 't' or 'tau'. 
          It's value can be:
        
            - Empty: .get_tau() is used,
            - A valuation date (e.g. t='15-05-2020'): either a 'dd-mm-YYYY' String or a dt.datetime object
            - A time-to-maturity value (e.g. tau=0.5)
        """
                
        # if tau==0, this is the P&L at option's expiration, that is the PnL if the option is kept until maturity
        # it is computed as:
        # P&L = payoff - initial price
        #
        # if tau > 0, this is the P&L as if the option position is closed before maturity, when the time-to-maturity is tau
        # it is computed as:
        # P&L = current price - initial price
        #
        # the choice between payoff and current price is delegated to .price() method
        return self.price(*args, **kwargs) - scalarize(self.get_initial_price())
            
#-----------------------------------------------------------------------------#
        
class PlainVanillaOption(EuropeanOption):
    """
    PlainVanillaOption class implementing payoff and pricing of plain-vanilla call and put options.
    Inherits from EuropeanOption base-class. Put price is calculated using put-call parity
    
    Attributes:
    -----------
        mkt_env (MarketEnvironment): Instance of MarketEnvironment class
        type (str):                  From 'type' attribute of EuropeanOption base class.
        S_t (float):                 'S' attribute of mkt_env.
        K (float):                   From 'K' attribute of EuropeanOption base class.
        t (str; dt.datetime):        't' attribute of mkt_env.
        T (str; dt.datetime):        From 'T' attribute of EuropeanOption base class.
        tau (float):                 time to maturity in years, computed as tau=T-t by time_to_maturity() method
        r (float):                   'r' attribute of mkt_env.
        sigma (float):               'sigma' attribute of mkt_env.
    
    Public Methods:
    --------   

        public methods inherited from EuropeanOption class

        payoff: float
            Overridden method. Computes the payoff of the option and returns it

        price_upper_limit: float 
            Overridden method. Returns the upper limit for a vanilla option price.

        price_lower_limit: float 
            Overridden method. Returns the lower limit for a vanilla option price.
            
        price: float
            Overridden method. Computes the exact price of the option and returns it
            
    Usage: 
    --------   
        - default: PlainVanillaOption(mkt_env) is equivalent to 
                   PlainVanillaOption(mkt_env, option_type='call', K=100.0, T="31-12-2020")

        - general: PlainVanillaOption(mkt_env, option_type='call' or 'put' String, K=Float, T="DD-MM-YYYY" String)

    where: mkt_env is a MarketEnvironment instance.
    """
    
    # initializer with optional *args and **kwargs parameters
    def __init__(self, *args, **kwargs):  
        
        # calling the EuropeanOption initializer
        super(PlainVanillaOption, self).__init__(*args, **kwargs)
        
        # info strings
        self.__info = r"Plain Vanilla {} [K={:.1f}, T={} (tau={:.2f}y)]".format(self.get_type(), self.get_K(), datetime_obj_to_date_string(self.get_T()), self.get_tau())
        self.__mkt_info = r"[S_t={:.1f}, r={:.1f}%, sigma={:.1f}%, t={}]".format(self.get_S(), self.get_r()*100, self.get_sigma()*100, datetime_obj_to_date_string(self.get_t()))
        
        # initial price of the option (as scalar value)
        self.__initial_price = self.price()
        
        # informations dictionary
        self.__docstring_dict = {
            'call':{
                'price_upper_limit': r"Upper limit: $S_t$",
                'payoff':            r"Payoff: $max(S-K, 0)$",
                'price_lower_limit': r"Lower limit: $max(S_t - K e^{-r \tau}, 0)$"
            },
            'put': {
                'price_upper_limit': r"Upper limit: $K e^{-r \tau}$",
                'payoff':            r"Payoff: $max(K-S, 0)$",
                'price_lower_limit': r"Lower limit: $max(K e^{-r \tau} - S_t, 0)$"}
        }
                
    def __repr__(self):
        return r"PlainVanillaOption('{}', S_t={:.1f}, K={:.1f}, t={}, T={}, tau={:.2f}y, r={:.1f}%, sigma={:.1f}%)".\
                format(self.get_type(), self.get_S(), self.get_K(), self.get_t().strftime("%d-%m-%Y"), 
                       self.get_T().strftime("%d-%m-%Y"), self.get_tau(), self.get_r()*100, self.get_sigma()*100)
    
    # getters
    def get_info(self):
        return self.__info
    
    def get_mkt_info(self):
        return self.__mkt_info
    
    def get_initial_price(self):
        return self.__initial_price

    def get_docstring(self, label):
        return self.__docstring_dict[self.get_type()][label] 
    
    # payoff calculation - with optional *args and **kwargs parameters
    def payoff(self, *args, **kwargs):
        """
        Can be called using (underlying), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
        """
        
        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)
        
        # underlying value
        S = param_dict["S"]
                
        # call case
        if self.get_type() == 'call':
            return self.__call_payoff(S)
        # put case
        else:
            return self.__put_payoff(S)
                
    def __call_payoff(self, S):
        # np.maximum(arr, x) returns the array of the maximum between each
        # element of arr and x
        return np.maximum(S - self.get_K(), 0.0)

    def __put_payoff(self, S):
        return np.maximum(self.get_K() - S, 0.0)
        
    # upper price limit - with optional *args and **kwargs parameters
    def price_upper_limit(self, *args, **kwargs):
        """
        Can be called using (underlying, time-parameter, short-rate), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
            
        - time-parameter can be specified either as the 2nd positional argument or as keyboard argument 't' or 'tau'. 
          It's value can be:
        
            - Empty: .get_tau() is used,
            - A valuation date (e.g. t='15-05-2020'): either a 'dd-mm-YYYY' String or a dt.datetime object
            - A time-to-maturity value (e.g. tau=0.5)

        - short-rate can be specified as keyboard argument 'r'. 
          It's value can be:
        
            - Empty: .get_r() is used,
            - A short-rate value (e.g. 0.05 for 5% per year)
        """

        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)
        
        # underlying value, time-to-maturity and short-rate
        S = param_dict["S"]
        tau = param_dict["tau"]
        r = param_dict["r"]

        if self.get_type() == 'call':
            # call case
            return self.__call_price_upper_limit(S)
        else:
            # put case
            return self.__put_price_upper_limit(S, tau, r)
            
    def __call_price_upper_limit(self, S):
        return S
    
    def __put_price_upper_limit(self, S, tau, r):
        return self.get_K()*np.exp(-r * tau)

    # lower price limit - with optional *args and **kwargs parameters
    def price_lower_limit(self, *args, **kwargs):
        """
        Can be called using (underlying, time-parameter, short-rate), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
            
        - time-parameter can be specified either as the 2nd positional argument or as keyboard argument 't' or 'tau'. 
          It's value can be:
        
            - Empty: .get_tau() is used,
            - A valuation date (e.g. t='15-05-2020'): either a 'dd-mm-YYYY' String or a dt.datetime object
            - A time-to-maturity value (e.g. tau=0.5)

        - short-rate can be specified as keyboard argument 'r'. 
          It's value can be:
        
            - Empty: .get_r() is used,
            - A short-rate value (e.g. 0.05 for 5% per year)
        """

        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)

        # underlying value, time-to-maturity and short-rate
        S = param_dict["S"]
        tau = param_dict["tau"]
        r = param_dict["r"]
                                       
        # call case
        if self.get_type() == 'call':
            return self.__call_price_lower_limit(S, tau, r)
        # put case
        else:
            return self.__put_price_lower_limit(S, tau, r)
            
    def __call_price_lower_limit(self, S, tau, r):
        # np.maximum(arr, x) returns the array of the maximum between each
        # element of arr and x
        return np.maximum(S - self.get_K()*np.exp(-r * tau), 0.0)
        
    def __put_price_lower_limit(self, S, tau, r):
        return np.maximum(self.get_K()*np.exp(-r * tau) - S, 0.0)
                                       
    # price calculation - with optional *args and **kwargs parameters
    def price(self, *args, **kwargs):
        """
        Can be called using (underlying, time-parameter, sigma, short-rate), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
            
        - time-parameter can be specified either as the 2nd positional argument or as keyboard argument 't' or 'tau'. 
          It's value can be:
        
            - Empty: .get_tau() is used,
            - A valuation date (e.g. t='15-05-2020'): either a 'dd-mm-YYYY' String or a dt.datetime object
            - A time-to-maturity value (e.g. tau=0.5)

        - sigma can be specified as keyboard argument 'sigma'. 
          It's value can be:
        
            - Empty: .get_sigma() is used,
            - A volatility value (e.g. 0.2 for 20% per year)

        - short-rate can be specified as keyboard argument 'r'. 
          It's value can be:
        
            - Empty: .get_r() is used,
            - A short-rate value (e.g. 0.05 for 5% per year)
        """
                       
        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)

        # underlying value, time-to-maturity and short-rate
        S = param_dict["S"]
        tau = param_dict["tau"]
        sigma = param_dict["sigma"]
        r = param_dict["r"]
        np_output = param_dict["np_output"]
        
        #
        # for tau==0 output the payoff, otherwise price
        #
        
        if np_output:
            # initialize an empty structure to hold prices
            price = np.empty_like(S, dtype=float)
            # filter positive times-to-maturity
            tau_pos = tau > 0
        else:
            # initialize an empty structure to hold prices
            price = pd.DataFrame(index=S.index, columns=S.columns)
            # filter positive times-to-maturity
            tau_pos = tau.iloc[:,0] > 0
        
        # call case
        if self.get_type() == 'call':
            # tau > 0 case
            price[tau_pos] = self.__call_price(S[tau_pos], tau[tau_pos], sigma, r)
            # tau == 0 case
            price[~tau_pos] = self.__call_payoff(S[~tau_pos])  
        # put case
        else:
            # tau > 0 case
            price[tau_pos] = self.__put_price(S[tau_pos], tau[tau_pos], sigma, r)
            # tau == 0 case
            price[~tau_pos] = self.__put_payoff(S[~tau_pos])  
            
        return price
          
    def __call_price(self, S, tau, sigma, r):
        
        # get d1 and d2 terms
        d1, d2 = self.d1_and_d2(S, tau, sigma=sigma, r=r)

        # get strike price    
        K = self.get_K()
        
        # compute price
        price = S * stats.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * tau) * stats.norm.cdf(d2, 0.0, 1.0)
                           
        return price
    
    def __put_price(self, S, tau, sigma, r):
        """ Put price from Put-Call parity relation: Call + Ke^{-r*tau} = Put + S"""
        return self.__call_price(S, tau, sigma, r) + self.get_K() * np.exp(-r * tau) - S     
    
#-----------------------------------------------------------------------------#

class DigitalOption(EuropeanOption):
    """
    DigitalOption class implementing payoff and pricing of digital call and put options.
    Inherits from EuropeanOption base-class. Put price is calculated using put-call parity
    
    Attributes:
    -----------
        mkt_env (MarketEnvironment): Instance of MarketEnvironment class
        Q (float):                   cash amount
        type (str):                  From 'type' attribute of EuropeanOption base class.
        S_t (float):                 'S' attribute of mkt_env.
        K (float):                   From 'K' attribute of EuropeanOption base class.
        t (str; dt.datetime):        't' attribute of mkt_env.
        T (str; dt.datetime):        From 'T' attribute of EuropeanOption base class.
        tau (float):                 time to maturity in years, computed as tau=T-t by time_to_maturity() method
        r (float):                   'r' attribute of mkt_env.
        sigma (float):               'sigma' attribute of mkt_env.
    
    Public Methods:
    --------   
 
        public methods inherited from EuropeanOption class

        payoff: float
            Overridden method. Computes the payoff of the option and returns it

        price_upper_limit: float 
            Overridden method. Returns the upper limit for a vanilla option price.

        price_lower_limit: float 
            Overridden method. Returns the lower limit for a vanilla option price.
            
        price: float
            Overridden method. Computes the exact price of the option and returns it, using call_price() or put_price()

    Usage: 
    --------   
        - default: DigitalOption(mkt_env) is equivalent to 
                   DigitalOption(mkt_env, cash_amount=1.0, option_type='call', K=100.0, T="31-12-2020")

        - general: DigitalOption(mkt_env, cash_amount=Float, option_type='call' or 'put' String, K=Float, T="DD-MM-YYYY" String)

    where: mkt_env is a MarketEnvironment instance.
    """

    # initializer with optional *args and **kwargs parameters and default cash_amount
    # default keyword arguments (like cash_amount here) must go after args list argument in function def
    def __init__(self, *args, cash_amount=1.0, **kwargs):  
        
        # calling the EuropeanOption initializer
        super(DigitalOption, self).__init__(*args, **kwargs)
        
        # amount of cash in case of payment
        self.__Q = cash_amount    
        
        # info strings
        self.__info = r"CON {} [K={:.1f}, T={} (tau={:.2f}y), Q={:.1f}]".format(self.get_type(), self.get_K(), datetime_obj_to_date_string(self.get_T()), self.get_tau(), self.get_Q())
        self.__mkt_info = r"[S_t={:.1f}, r={:.1f}%, sigma={:.1f}%, t={}]".format(self.get_S(), self.get_r()*100, self.get_sigma()*100, datetime_obj_to_date_string(self.get_t()))
        
        # initial price of the option
        self.__initial_price = self.price()

        # informations dictionary
        self.__docstring_dict = {
            'call':{
                'price_upper_limit': r"Upper limit: $Q e^{-r \tau}$",
                'payoff':            r"Payoff: $Q$ $I(S > K)$",
                'price_lower_limit': r"Lower limit: $0$"
            },
            'put': {
                'price_upper_limit': r"Upper limit: $Q e^{-r \tau}$",
                'payoff':            r"Payoff: $Q$ $I(S \leq K)$",
                'price_lower_limit': r"Lower limit: $0$"}
        }        
                
    def __repr__(self):
        return r"DigitalOption('{}', cash={:.1f}, S_t={:.1f}, K={:.1f}, t={}, T={}, tau={:.2f}y, r={:.1f}%, sigma={:.1f}%)".\
                format(self.get_type(), self.get_Q(), self.get_S(), self.get_K(), self.get_t().strftime("%d-%m-%Y"), 
                       self.get_T().strftime("%d-%m-%Y"), self.get_tau(), self.get_r()*100, self.get_sigma()*100)
    
    # getters
    def get_info(self):
        return self.__info
    
    def get_mkt_info(self):
        return self.__mkt_info
    
    def get_Q(self):
        return self.__Q
    
    def get_initial_price(self):
        return self.__initial_price
    
    # docstring getter
    def get_docstring(self, label):
        return self.__docstring_dict[self.get_type()][label] 
    
    # setters
    def set_Q(self, cash_amount):
        self.__Q = cash_amount
    
    # payoff calculation - with optional *args and **kwargs parameters
    def payoff(self, *args, **kwargs):
        """
        Can be called using (underlying), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
        """
        
        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)
        
        # underlying value
        S = param_dict["S"]
        
        # call case
        if self.get_type() == 'call':
            return self.__call_payoff(S)
        # put case
        else:
            return self.__put_payoff(S)
            
    def __call_payoff(self, S):
        # np.heaviside(arr, x) returns
        #
        # 0 if arr < 0
        # x if arr == 0
        # 1 if arr > 0
        return np.heaviside(S - self.get_K(), 0.0)

    def __put_payoff(self, S):
        return np.heaviside(self.get_K() - S, 1.0)
        
    # upper price limit - with optional *args and **kwargs parameters
    def price_upper_limit(self, *args, **kwargs):
        """
        Can be called using (underlying, time-parameter, short-rate), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
            
        - time-parameter can be specified either as the 2nd positional argument or as keyboard argument 't' or 'tau'. 
          It's value can be:
        
            - Empty: .get_tau() is used,
            - A valuation date (e.g. t='15-05-2020'): either a 'dd-mm-YYYY' String or a dt.datetime object
            - A time-to-maturity value (e.g. tau=0.5)

        - short-rate can be specified as keyboard argument 'r'. 
          It's value can be:
        
            - Empty: .get_r() is used,
            - A short-rate value (e.g. 0.05 for 5% per year)
        """

        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)
        
        # underlying value, time-to-maturity and short-rate
        S = param_dict["S"]
        tau = param_dict["tau"]
        r = param_dict["r"]
        
        # the same for call and put
        return self.get_Q()*np.exp(-r * tau)
        
    # lower price limit - with optional *args and **kwargs parameters
    def price_lower_limit(self, *args, **kwargs):
        """
        Can be called using (underlying), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
       """

        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)
        
        # underlying value
        S = param_dict["S"]
        
        # the same for call and put
        return 0.0*S

    # price calculation - with optional *args and **kwargs parameters
    def price(self, *args, **kwargs):
        """
        Can be called using (underlying, time-parameter, sigma, short-rate), where:

        - underlying can be specified either as the 1st positional argument or as keyboard argument 'S'. 
          It's value can be:
        
            - Empty: .get_S() is used,
            - A number (e.g. S=100),
            - A List of numbers
            
        - time-parameter can be specified either as the 2nd positional argument or as keyboard argument 't' or 'tau'. 
          It's value can be:
        
            - Empty: .get_tau() is used,
            - A valuation date (e.g. t='15-05-2020'): either a 'dd-mm-YYYY' String or a dt.datetime object
            - A time-to-maturity value (e.g. tau=0.5)

        - sigma can be specified as keyboard argument 'sigma'. 
          It's value can be:
        
            - Empty: .get_sigma() is used,
            - A volatility value (e.g. 0.2 for 20% per year)

        - short-rate can be specified as keyboard argument 'r'. 
          It's value can be:
        
            - Empty: .get_r() is used,
            - A short-rate value (e.g. 0.05 for 5% per year)
        """
                       
        # process input parameters
        param_dict = self.process_input_parameters(*args, **kwargs)

        # underlying value, time-to-maturity and short-rate
        S = param_dict["S"]
        tau = param_dict["tau"]
        sigma = param_dict["sigma"]
        r = param_dict["r"]
        np_output = param_dict["np_output"]
        
        #
        # for tau==0 output the payoff, otherwise price
        #
        
        if np_output:
            # initialize an empty structure to hold prices
            price = np.empty_like(S, dtype=float)
            # filter positive times-to-maturity
            tau_pos = tau > 0
        else:
            # initialize an empty structure to hold prices
            price = pd.DataFrame(index=S.index, columns=S.columns)
            # filter positive times-to-maturity
            tau_pos = tau.iloc[:,0] > 0

        # call case
        if self.get_type() == 'call':
            # tau > 0 case
            price[tau_pos] = self.__call_price(S[tau_pos], tau[tau_pos], sigma, r)
            # tau == 0 case
            price[~tau_pos] = self.__call_payoff(S[~tau_pos])  
        # put case
        else:
            # tau > 0 case
            price[tau_pos] = self.__put_price(S[tau_pos], tau[tau_pos], sigma, r)
            # tau == 0 case
            price[~tau_pos] = self.__put_payoff(S[~tau_pos])  
        
        return price
          
    def __call_price(self, S, tau, sigma, r):
                
        Q = self.get_Q()
        
        # get d2 term
        _, d2 = self.d1_and_d2(S, tau, sigma=sigma, r=r)

        price = Q * np.exp(-r * tau) * stats.norm.cdf(d2, 0.0, 1.0)

        return price
    
    def __put_price(self, S, tau, sigma, r):
        """ Put price from Put-Call parity relation: CON_Call + CON_Put = Qe^{-r*tau}"""
        return self.get_Q() * np.exp(- r * tau) - self.__call_price(S, tau, sigma, r)        
