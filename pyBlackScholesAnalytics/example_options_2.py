import numpy as np
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
    S_vector = [90, 100, 110]
    mS = len(S_vector)
    
    # K
    K_vector = [75, 85, 90, 95, 105, 115]
    mK = len(K_vector)

    # tau: a date-range of 5 valuation dates between t and T-10d
    n = 5
    valuation_date = option.get_t()
    expiration_date = option.get_T()
    t_vector = pd.date_range(start=valuation_date, 
                             end=expiration_date-pd.Timedelta(days=10), 
                             periods=n)    
    # sigma
    sigma_grid_S = np.array([0.1*(1.0 + i) for i in range(mS*n)]).reshape(n,mS)
    sigma_grid_K = np.array([0.1*(1.0 + i) for i in range(mK*n)]).reshape(n,mK)
    
    # r
    r_grid_S = np.array([0.01*(1.0 + i) for i in range(mS*n)]).reshape(n,mS)
    r_grid_K = np.array([0.01*(1.0 + i) for i in range(mK*n)]).reshape(n,mK)

    cases_dict = {
            "0": {"parameters": {"S": S_vector[0],
                                 "K": K_vector[0],
                                 "t": t_vector[0],
                                 "sigma": 0.1,
                                 "r": 0.01,
                                 "np_output": np_output},
                  "info": "Case 0 - all scalar parameters"
                  },
            "1.1_S": {"parameters": {"S": S_vector,
                                     "K": K_vector[0],
                                     "t": t_vector[0],
                                     "sigma": 0.1,
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 1.1_S - (S vector, other scalar)"
                  },
            "1.2_S": {"parameters": {"S": S_vector,
                                     "K": K_vector[0],
                                     "t": t_vector[0],
                                     "sigma": 0.1,
                                     "r": [0.01*(1.0 + i) for i in range(mS)],
                                     "np_output": np_output},
                    "info": "Case 1.2_S - (S vector, K scalar, t scalar, sigma scalar, r vector as S)"
                  },
            "1.3_S": {"parameters": {"S": S_vector,
                                     "K": K_vector[0],
                                     "t": t_vector[0],
                                     "sigma": [0.1*(1.0 + i) for i in range(mS)],
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 1.3_S - (S vector, K scalar, t scalar, sigma vector as S, r scalar)"
                  },
            "1.4_S": {"parameters": {"S": S_vector,
                                     "K": K_vector[0],
                                     "t": t_vector[0],
                                     "sigma": [0.1*(1.0 + i) for i in range(mS)],
                                     "r": [0.01*(1.0 + i) for i in range(mS)],
                                     "np_output": np_output},
                    "info": "Case 1.4_S - (S vector, K scalar, t scalar, sigma vector as S, r vector as S)"
                  },
            "1.1_K": {"parameters": {"S": S_vector[0],
                                     "K": K_vector,
                                     "t": t_vector[0],
                                     "sigma": 0.1,
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 1.1_K - (K vector, other scalar)"
                  },
            "1.2_K": {"parameters": {"S": S_vector[0],
                                     "K": K_vector,
                                     "t": t_vector[0],
                                     "sigma": 0.1,
                                     "r": [0.01*(1.0 + i) for i in range(mK)],
                                     "np_output": np_output},
                    "info": "Case 1.2_S - (S scalar, K vector, t scalar, sigma scalar, r vector as K)"
                  },
            "1.3_K": {"parameters": {"S": S_vector[0],
                                     "K": K_vector,
                                     "t": t_vector[0],
                                     "sigma": [0.1*(1.0 + i) for i in range(mK)],
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 1.3_K - (S scalar, K vector, t scalar, sigma vector as K, r scalar)"
                  },
            "1.4_K": {"parameters": {"S": S_vector[0],
                                     "K": K_vector,
                                     "t": t_vector[0],
                                     "sigma": [0.1*(1.0 + i) for i in range(mK)],
                                     "r": [0.01*(1.0 + i) for i in range(mK)],
                                     "np_output": np_output},
                    "info": "Case 1.4_K - (S scalar, K vector, t scalar, sigma vector as K, r vector as K)"
                  },
            "1.1_t": {"parameters": {"S": S_vector[0],
                                     "K": K_vector[0],
                                     "t": t_vector,
                                     "sigma": 0.1,
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 1.1_t - (t vector, other scalar)"
                  },
            "1.2_t": {"parameters": {"S": S_vector[0],
                                     "K": K_vector[0],
                                     "t": t_vector,
                                     "sigma": 0.1,
                                     "r": [0.01*(1.0 + i) for i in range(n)],
                                     "np_output": np_output},
                    "info": "Case 1.2_t - (S scalar, K scalar, t vector, sigma scalar, r vector as t)"
                  },
            "1.3_t": {"parameters": {"S": S_vector[0],
                                     "K": K_vector[0],
                                     "t": t_vector,
                                     "sigma": [0.1*(1.0 + i) for i in range(n)],
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 1.3_t - (S scalar, K scalar, t vector, sigma vector as t, r scalar)"
                  },
            "1.4_t": {"parameters": {"S": S_vector[0],
                                     "K": K_vector[0],
                                     "t": t_vector,
                                     "sigma": [0.1*(1.0 + i) for i in range(n)],
                                     "r": [0.01*(1.0 + i) for i in range(n)],
                                     "np_output": np_output},
                    "info": "Case 1.4_t - (S scalar, K scalar, t vector, sigma vector as t, r vector as t)"
                  },
            "2.1_S": {"parameters": {"S": S_vector,
                                     "K": K_vector[0],
                                     "t": t_vector,
                                     "sigma": 0.1,
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 2.1_S - (S and t vector, other scalar)"
                  },
            "2.1_K": {"parameters": {"S": S_vector[0],
                                     "K": K_vector,
                                     "t": t_vector,
                                     "sigma": 0.1,
                                     "r": 0.01,
                                     "np_output": np_output},
                    "info": "Case 2.1_K - (K and t vector, other scalar)"
                  },
            "2.2_S_sigma": {"parameters": {"S": S_vector,
                                           "K": K_vector[0],
                                           "t": t_vector,
                                           "sigma": sigma_grid_S,
                                           "r": 0.01,
                                           "np_output": np_output},
                    "info": "Case 2.2_S_sigma - (S and t vector, K scalar, sigma grid as Sxt, r scalar)"
                  },
            "2.2_K_sigma": {"parameters": {"S": S_vector[0],
                                           "K": K_vector,
                                           "t": t_vector,
                                           "sigma": sigma_grid_K,
                                           "r": 0.01,
                                           "np_output": np_output},
                    "info": "Case 2.2_K_sigma - (S scalar, K and t vector, sigma grid as Kxt, r scalar)"
                  },
            "2.3_S_r": {"parameters": {"S": S_vector,
                                       "K": K_vector[0],
                                       "t": t_vector,
                                       "sigma": 0.1,
                                       "r": r_grid_S,
                                       "np_output": np_output},
                    "info": "Case 2.3_S_r - (S and t vector, K scalar, sigma scalar, r grid as Sxt)"
                  },
            "2.3_K_r": {"parameters": {"S": S_vector[0],
                                       "K": K_vector,
                                       "t": t_vector,
                                       "sigma": 0.1,
                                       "r": r_grid_K,
                                       "np_output": np_output},
                    "info": "Case 2.3_K_r - (S scalar, K and t vector, sigma scalar, r grid as Kxt)"
                  },
            "2.4_S": {"parameters": {"S": S_vector,
                                     "K": K_vector[0],
                                     "t": t_vector,
                                     "sigma": sigma_grid_S,
                                     "r": r_grid_S,
                                     "np_output": np_output},
                    "info": "Case 2.4_S - (S and t vector, K scalar, sigma grid as Sxt, r grid as Sxt)"
                  },
            "2.4_K": {"parameters": {"S": S_vector[0],
                                     "K": K_vector,
                                     "t": t_vector,
                                     "sigma": sigma_grid_K,
                                     "r": r_grid_K,
                                     "np_output": np_output},
                    "info": "Case 2.4_K - (S scalar, K and t vector, sigma grid as Kxt, r grid as Kxt)"
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
    opt_style = "plain_vanilla" # "plain_vanilla" # "digital"
    opt_type = "call" # "call" # "put"   
    option = option_factory(market_env, opt_style, opt_type)
    print(option)
    
    # loop over different cases:
#    for case in ["0", "1.1_S", "1.2_S", "1.3_S", "1.4_S", \
#                      "1.1_t", "1.2_t", "1.3_t", "1.4_t", \
#                      "2.1", "2.2_sigma", "2.3_r", "2.4"]:

    for case in ['0', '1.1_S', '1.2_S', '1.3_S', '1.4_S', \
                      '1.1_K', '1.2_K', '1.3_K', '1.4_K', \
                      '1.1_t', '1.2_t', '1.3_t', '1.4_t', \
                      '2.1_S', '2.1_K', '2.2_S_sigma', '2.2_K_sigma', \
                      '2.3_S_r', '2.3_K_r', \
                      '2.4_S', '2.4_K']:
        
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
        print("\nImplied Volatility - Newton method (expected iv:\n{}):\n".format(param_dict["sigma"]), 
              option.implied_volatility(**param_dict))
        param_dict["minimization_method"] = "Least-Squares"
        print("\nImplied Volatility - Least-Squares constrained method (expected iv:\n{}):\n".format(param_dict["sigma"]), 
              option.implied_volatility(**param_dict))
        print("\nDelta:\n", option.delta(**param_dict))
        print("\nTheta:\n", option.theta(**param_dict))
        print("\nGamma:\n", option.gamma(**param_dict))
        print("\nVega:\n", option.vega(**param_dict))
        print("\nRho:\n", option.rho(**param_dict))

#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    