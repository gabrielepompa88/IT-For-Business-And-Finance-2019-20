import numpy as np
import pandas as pd

from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption

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
    S_vector = [90, 100, 110]
    m = len(S_vector)
    
    # tau: a date-range of 5 valuation dates between t and T-10d
    n = 5
    valuation_date = option.get_t()
    expiration_date = option.get_T()
    t_vector = pd.date_range(start=valuation_date, 
                             end=expiration_date-pd.Timedelta(days=10), 
                             periods=n)    
    # sigma
    sigma_vector = [0.1, 0.2, 0.3, 0.4, 0.5]
    sigma_grid = np.array([0.1*(1.0 + i) for i in range(m*n)]).reshape(m,n)
    
    # r
    r_vector = [0.0, 0.01, 0.025, 0.03, 0.04, 0.05]
    r_grid = np.array([0.01*(1.0 + i) for i in range(m*n)]).reshape(m,n)

    cases_dict = {
            "0": {"parameters": {"S": S_vector[0],
                                 "t": t_vector[0],
                                 "sigma": 0.1,
                                 "r": 0.01,
                                 "np_output": np_output},
                  "info": "Case 0 - all scalar parameters"
                  },
            "1.1_S": {"parameters": {"S": S_vector,
                                   "t": t_vector[0],
                                   "sigma": 0.1,
                                   "r": 0.01,
                                   "np_output": np_output},
                    "info": "Case 1.1 - (S vector, other scalar)"
                  },
            "1.2_S": {"parameters": {"S": S_vector,
                                   "t": t_vector[0],
                                   "sigma": 0.1,
                                   "r": [0.01*(1.0 + i) for i in range(m)],
                                   "np_output": np_output},
                    "info": "Case 1.2 - (S vector, t scalar, sigma scalar, r vector as S)"
                  },
            "1.3_S": {"parameters": {"S": S_vector,
                                   "t": t_vector[0],
                                   "sigma": [0.1*(1.0 + i) for i in range(m)],
                                   "r": 0.01,
                                   "np_output": np_output},
                    "info": "Case 1.3 - (S vector, t scalar, sigma vector as S, r scalar)"
                  },
            "1.4_S": {"parameters": {"S": S_vector,
                                   "t": t_vector[0],
                                   "sigma": [0.1*(1.0 + i) for i in range(m)],
                                   "r": [0.01*(1.0 + i) for i in range(m)],
                                   "np_output": np_output},
                    "info": "Case 1.4 - (S vector, t scalar, sigma vector as S, r vector as S)"
                  },
            "1.1_t": {"parameters": {"S": S_vector[0],
                                   "t": t_vector,
                                   "sigma": 0.1,
                                   "r": 0.01,
                                   "np_output": np_output},
                    "info": "Case 1.1 - (t vector, other scalar)"
                  },
            "1.2_t": {"parameters": {"S": S_vector[0],
                                   "t": t_vector,
                                   "sigma": 0.1,
                                   "r": [0.01*(1.0 + i) for i in range(n)],
                                   "np_output": np_output},
                    "info": "Case 1.2 - (S scalar, t vector, sigma scalar, r vector as t)"
                  },
            "1.3_t": {"parameters": {"S": S_vector[0],
                                   "t": t_vector,
                                   "sigma": [0.1*(1.0 + i) for i in range(n)],
                                   "r": 0.01,
                                   "np_output": np_output},
                    "info": "Case 1.3 - (S scalae, t vector, sigma vector as t, r scalar)"
                  },
            "1.4_t": {"parameters": {"S": S_vector[0],
                                   "t": t_vector,
                                   "sigma": [0.1*(1.0 + i) for i in range(n)],
                                   "r": [0.01*(1.0 + i) for i in range(n)],
                                   "np_output": np_output},
                    "info": "Case 1.4 - (S scalar, t vector, sigma vector as t, r vector as t)"
                  },
            "2.1": {"parameters": {"S": S_vector,
                                   "t": t_vector,
                                   "sigma": 0.1,
                                   "r": 0.01,
                                   "np_output": np_output},
                    "info": "Case 2.1 - (S and t vector, other scalar)"
                  },
            "2.2_sigma": {"parameters": {"S": S_vector,
                                   "t": t_vector,
                                   "sigma": sigma_grid,
                                   "r": 0.01,
                                   "np_output": np_output},
                    "info": "Case 2.2 - (S and t vector, sigma grid as Sxt, r scalar)"
                  },
            "2.3_r": {"parameters": {"S": S_vector,
                                   "t": t_vector,
                                   "sigma": 0.1,
                                   "r": r_grid,
                                   "np_output": np_output},
                    "info": "Case 2.3 - (S and t vector, sigma scalar, r grid as Sxt)"
                  },
            "2.4": {"parameters": {"S": S_vector,
                                   "t": t_vector,
                                   "sigma": sigma_grid,
                                   "r": r_grid,
                                   "np_output": np_output},
                    "info": "Case 2.4 - (S and t vector, sigma grid as Sxt, r grid as Sxt)"
                  }
    }
    
    return cases_dict[case]["parameters"], cases_dict[case]["info"]

def main():

    #
    # option (underlying, time-parameter) instantiation example
    # with focus on other iterable parameters: (volatility, short-rate)
    #
    
    # if np_output is True, the output will be np.ndarray, otherwise pd.DataFrame    
    np_output = False # True
    
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    # define option style and type
    opt_style = "plain_vanilla" # "digital"
    opt_type = "call" # "put"   
    option = option_factory(market_env, opt_style, opt_type)
    print(option)
    
    # loop over different cases:
#    for case in ["0", "1.1_S", "1.2_S", "1.3_S", "1.4_S", \
#                      "1.1_t", "1.2_t", "1.3_t", "1.4_t", \
#                      "2.1", "2.2_sigma", "2.3_r", "2.4"]:
    
    for case in ["2.4"]:
        
        # get parameters dictionary for case considered
        param_dict, case_info = get_param_dict(option, np_output, case)
    
        print("\n--------------------------------------------\n")
        print("\n" + case_info + "\n")
        
        print("Parameters:")
        print("S: {}".format(param_dict["S"]))
        print("t: {}".format(param_dict["t"]))
        print("sigma: {}".format(param_dict["sigma"]))
        print("r: {}\n".format(param_dict["r"]))
        
        print("Metrics:")
        print("Payoff:\n", option.payoff(**param_dict))
        print("\nPrice upper limit:\n", option.price_upper_limit(**param_dict))
        print("\nPrice lower limit:\n", option.price_lower_limit(**param_dict))
        print("\nPrice:\n", option.price(**param_dict))
        print("\nP&L:\n", option.PnL(**param_dict))
        print("\nImplied Volatility (expected iv:\n{}):\n".format(param_dict["sigma"]), 
              option.implied_volatility(**param_dict))
        print("\nDelta:\n", option.delta(**param_dict))
        print("\nTheta:\n", option.theta(**param_dict))
        print("\nGamma:\n", option.gamma(**param_dict))
        print("\nVega:\n", option.vega(**param_dict))
        print("\nRho:\n", option.rho(**param_dict))

#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    