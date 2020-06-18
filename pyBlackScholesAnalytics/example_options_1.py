import pandas as pd
import warnings

from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption

warnings.filterwarnings("ignore")

def option_factory(mkt_env, plain_or_digital, option_type):

    option_dispatcher = {
            "plain_vanilla": {"call": PlainVanillaOption(mkt_env),
                              "put":  PlainVanillaOption(mkt_env, option_type="put")
                             },
            "digital": {"call": DigitalOption(mkt_env),
                        "put":  DigitalOption(mkt_env, option_type="put")
                       }
    }
    
    return option_dispatcher[plain_or_digital][option_type]

def get_param_dict(option, np_output, case):
    
    # S
    S_scalar = 100
    S_vector = [90, 100, 110]
    
    # tau: several possibilities
    t_scalar_dt = option.get_t()
    t_scalar_string = "01-06-2020"
    tau_scalar = 0.5
    valuation_date = option.get_t()
    expiration_date = option.get_T()
    t_range = pd.date_range(start=valuation_date, 
                            end=expiration_date-pd.Timedelta(days=10),
                            periods=5)
    t_list = ["10-07-2020", "11-09-2020", "06-08-2020", "15-10-2020", "01-06-2020"] # order doesn't matter
    tau_list = [0.3, 0.4, 0.5, 0.6, 0.7]

    cases_dict = {
            "1": {"parameters": {"np_output": np_output},
                  "info": "Case 1: (S scalar, t scalar) default values"
                  },
            "2.1": {"parameters": {"S": S_scalar, 
                                   "t": t_scalar_dt,
                                   "np_output": np_output},
                  "info": "Case 2.1: (S scalar, t scalar as dt obj)"
                  },
            "2.2": {"parameters": {"S": S_scalar, 
                                   "t": t_scalar_string,
                                   "np_output": np_output},
                  "info": "Case 2.2: (S scalar, t scalar as string)"
                  },
            "2.3": {"parameters": {"S": S_scalar, 
                                   "tau": tau_scalar,
                                   "np_output": np_output},
                  "info": "Case 2.3: (S scalar, t scalar as time-to-maturity)"
                  },
            "2.4": {"parameters": {"S": S_vector, 
                                   "np_output": np_output},
                  "info": "Case 2.4: (S vector, t left default)"
                  },
            "2.5": {"parameters": {"t": t_range, 
                                   "np_output": np_output},
                  "info": "Case 2.5: (S left default, t vector as pd.date_range)"
                  },
            "3.1": {"parameters": {"S": S_vector,
                                   "t": t_range, 
                                   "np_output": np_output},
                  "info": "Case 3.1: (S vector, t vector as pd.date_range)"
                  },
            "3.2": {"parameters": {"S": S_vector,
                                   "t": t_list, 
                                   "np_output": np_output},
                  "info": "Case 3.2: (S vector, t vector as list of strings)"
                  },
            "3.3": {"parameters": {"S": S_vector,
                                   "tau": tau_list, 
                                   "np_output": np_output},
                  "info": "Case 3.3: (S vector, t vector as list of times-to-maturity)"
                  },
    }

    return cases_dict[case]["parameters"], cases_dict[case]["info"]

def main():

    #
    # option (underlying, time-parameter) instantiation example
    #
    
    # if np_output is True, the output will be np.ndarray, otherwise pd.DataFrame    
    np_output = False # True
    
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    # define option style and type
    opt_style = "plain_vanilla" # "digital" # "plain_vanilla"
    opt_type = "call" # "put"   
    option = option_factory(market_env, opt_style, opt_type)
    print(option)
    
    # loop over different cases:
    for case in ["1", "2.1", "2.2", "2.3", "2.4", "2.5", \
                      "3.1", "3.2", "3.3"]:    

        # get parameters dictionary for case considered
        param_dict, case_info = get_param_dict(option, np_output, case)
    
        print("\n--------------------------------------------\n")
        print("\n" + case_info + "\n")
        
        print("Parameters:")
        print("S: {}".format(param_dict["S"] if "S" in param_dict else option.get_S()))
        print("t: {}".format(param_dict["t"] if "t" in param_dict else option.get_tau()))
        print("sigma: {}".format(param_dict["sigma"] if "sigma" in param_dict else option.get_sigma()))
        print("r: {}\n".format(param_dict["r"] if "r" in param_dict else option.get_r()))

        print("Metrics:")
        print("Payoff:\n", option.payoff(**param_dict))
        print("\nPrice upper limit:\n", option.price_upper_limit(**param_dict))
        print("\nPrice lower limit:\n", option.price_lower_limit(**param_dict))
        print("\nPrice:\n", option.price(**param_dict))
        print("\nP&L:\n", option.PnL(**param_dict))
        print("\nImplied Volatility - Newton method (expected iv:\n{}):\n".format(option.get_sigma()),
              option.implied_volatility(**param_dict))
        param_dict["minimization_method"] = "Least-Squares"
        print("\nImplied Volatility - Least-Squares constrained method (expected iv:\n{}):\n".format(option.get_sigma()), 
              option.implied_volatility(**param_dict))
        print("\nDelta:\n", option.delta(**param_dict))
        print("\nTheta:\n", option.theta(**param_dict))
        print("\nGamma:\n", option.gamma(**param_dict))
        print("\nVega:\n", option.vega(**param_dict))
        print("\nRho:\n", option.rho(**param_dict))
  
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

