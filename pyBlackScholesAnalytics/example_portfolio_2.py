import numpy as np
import pandas as pd
import warnings

from utils.utils import date_string_to_datetime_obj
from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption
from portfolio.portfolio import Portfolio

warnings.filterwarnings("ignore")

def option_factory(mkt_env, plain_or_digital, option_type, **kwargs):

    option_dispatcher = {
            "plain_vanilla": {"call": PlainVanillaOption(mkt_env, **kwargs),
                              "put":  PlainVanillaOption(mkt_env, option_type="put", **kwargs)
                             },
            "digital": {"call": DigitalOption(mkt_env, **kwargs),
                        "put":  DigitalOption(mkt_env, option_type="put", **kwargs)
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
    sigma_axis = np.array([0.1*(0 + i) for i in range(3)])
    sigma_grid_S = np.array([0.1*(0 + i) for i in range(mS*n)]).reshape(n,mS)
    sigma_grid_K = np.array([0.1*(0 + i) for i in range(mK*n)]).reshape(n,mK)
    
    # r
    r_axis = np.array([0.01*(0 + i) for i in range(3)])
    r_grid_S = np.array([0.01*(0 + i) for i in range(mS*n)]).reshape(n,mS)
    r_grid_K = np.array([0.01*(0 + i) for i in range(mK*n)]).reshape(n,mK)

    cases_dict = {
            "All_scalar": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector[0],
                                         "sigma": 0.1,
                                         "r": 0.01,
                                         "np_output": np_output},
                  "info": "Case 0 - all scalar parameters"
                  },
            "S": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector[0],
                                         "sigma": 0.1,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case S - (S vector, other scalar)"
                  },
            "S.sigma_distributed": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector[0],
                                         "sigma": [0.1*(0 + i) for i in range(mS)],
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case S.sigma_distributed - (S vector, K scalar, t scalar, sigma distributed along S, r scalar)"
                  },
            "S.r_distributed": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector[0],
                                         "sigma": 0.1,
                                         "r": [0.01*(0 + i) for i in range(mS)],
                                         "np_output": np_output},
                    "info": "Case S.r_distributed - (S vector, K scalar, t scalar, sigma scalar, r distributed along S)"
                  },
            "S.sigma_and_r_distributed": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector[0],
                                         "sigma": [0.1*(0 + i) for i in range(mS)],
                                         "r": [0.01*(0 + i) for i in range(mS)],
                                         "np_output": np_output},
                    "info": "Case S.sigma_and_r_distributed - (S vector, K scalar, t scalar, sigma distributed along S, r distributed along S)"
                  },
            "K": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector[0],
                                         "sigma": 0.1,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case K - (K vector, other scalar)"
                  },
            "K.sigma_distributed": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector[0],
                                         "sigma": [0.1*(0 + i) for i in range(mK)],
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case K.sigma_distributed - (S scalar, K vector, t scalar, sigma distributed along K, r scalar)"
                  },
            "K.r_distributed": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector[0],
                                         "sigma": 0.1,
                                         "r": [0.01*(0 + i) for i in range(mK)],
                                         "np_output": np_output},
                    "info": "Case S.r_distributed - (S scalar, K vector, t scalar, sigma scalar, r distributed along K)"
                  },
            "K.sigma_and_r_distributed": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector[0],
                                         "sigma": [0.1*(0 + i) for i in range(mK)],
                                         "r": [0.01*(0 + i) for i in range(mK)],
                                         "np_output": np_output},
                    "info": "Case K.sigma_and_r_distributed - (S scalar, K vector, t scalar, sigma distributed along K, r distributed along K)"
                  },
            "t": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case t - (t vector, other scalar)"
                  },
            "t.sigma_distributed": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": [0.1*(0 + i) for i in range(n)],
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case t.sigma_distributed - (S scalar, K scalar, t vector, sigma distributed along t, r scalar)"
                  },
            "t.r_distributed": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": [0.01*(0 + i) for i in range(n)],
                                         "np_output": np_output},
                    "info": "Case t.r_distributed - (S scalar, K scalar, t vector, sigma scalar, r distributed along t)"
                  },
            "t.sigma_and_r_distributed": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": [0.1*(0 + i) for i in range(n)],
                                         "r": [0.01*(0 + i) for i in range(n)],
                                         "np_output": np_output},
                    "info": "Case t.sigma_and_r_distributed - (S scalar, K scalar, t vector, sigma distributed along t, r distributed along t)"
                  },
            "S.t": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case S.t - (S and t vector, other scalar)"
                  },
            "S.t.sigma_distributed_as_Sxt_grid": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": sigma_grid_S,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case S.t.sigma_distributed_as_Sxt_grid - (S and t vector, K scalar, sigma distributed as Sxt grid, r scalar)"
                  },
            "S.t.r_distributed_as_Sxt_grid": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": r_grid_S,
                                         "np_output": np_output},
                    "info": "Case S.t.r_distributed_as_Sxt_grid - (S and t vector, K scalar, sigma scalar, r distributed as Sxt grid)"
                  },
            "S.t.sigma_and_r_distributed_as_Sxt_grid": {"parameters": 
                                        {"S": S_vector,
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": sigma_grid_S,
                                         "r": r_grid_S,
                                         "np_output": np_output},
                    "info": "Case S.t.sigma_and_r_distributed_as_Sxt_grid - (S and t vector, K scalar, sigma distributed as Sxt grid, r distributed as Sxt grid)"
                  },
            "K.t": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case K.t - (K and t vector, other scalar)"
                  },
            "K.t.sigma_distributed_as_Kxt_grid": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector,
                                         "sigma": sigma_grid_K,
                                         "r": 0.01,
                                         "np_output": np_output},
                    "info": "Case K.t.sigma_distributed_as_Kxt_grid - (S scalar, K and t vector, sigma distributed as Kxt grid, r scalar)"
                  },
            "K.t.r_distributed_as_Kxt_grid": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": r_grid_K,
                                         "np_output": np_output},
                    "info": "Case K.t.r_distributed_as_Kxt_grid - (S scalar, K and t vector, sigma scalar, r distributed as Kxt grid)"
                  },
            "K.t.sigma_and_r_distributed_as_Kxt_grid": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector,
                                         "t": t_vector,
                                         "sigma": sigma_grid_K,
                                         "r": r_grid_K,
                                         "np_output": np_output},
                    "info": "Case K.t.sigma_and_r_distributed_as_Kxt_grid - (S scalar, K and t vector, sigma distributed as Kxt grid, r distributed as Kxt grid)"
                  },
            # if we want to have the x-axis spanned by sigma or r, we have to explicitly
            # ask for it, using "sigma_axis" or "r_axis" flags. Otherwise, sigma and r
            # parameters are interpreted as parameters to be distributed along the 
            # other(s) axis (and require length/shape match)
            "t.sigma_axis": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": sigma_axis,
                                         "r": 0.01,
                                         "np_output": np_output,
                                         "sigma_axis": True},
                    "info": "Case t.sigma_axis - (S scalar, K scalar, t vector, sigma vector axis, r scalar)"
                  },
            "t.r_axis": {"parameters": 
                                        {"S": S_vector[0],
                                         "K": K_vector[0],
                                         "t": t_vector,
                                         "sigma": 0.1,
                                         "r": r_axis,
                                         "np_output": np_output,
                                         "r_axis": True},
                    "info": "Case t.r_axis - (S scalar, K scalar, t vector, sigma scalar, r vector axis)"
                  }
    }
    
    return cases_dict[case]["parameters"], cases_dict[case]["info"]

def main():

    #
    # portfolio instantiation example
    #
    
    # if np_output is True, the output will be np.ndarray, otherwise pd.DataFrame    
    np_output = False # True
        
    # default market environment
    market_env = MarketEnvironment(t="01-06-2020")
    print(market_env)

    # underlying values to test
    S_vector = [60, 90, 120]
    print("S_vector: {}\n".format(S_vector))
    
    # options maturities
    T_call = "31-12-2020"
    T_put = "30-06-2021"
    
    # options strikes
    K_put = 80
    K_call = 110
    
    # portfolio options positions
    call_pos = 2
    put_pos = -5

    #
    # Step 0: empty portfolio initialized
    #
    
    ptf = Portfolio()
    print(ptf)
    
    #
    # Step 1: adding 2 long plain-vanilla call contracts
    #
    
    # plain-vanilla call option
    opt1_style = "plain_vanilla" # "digital"
    opt1_type = "call" # "put"   
    call = option_factory(market_env, opt1_style, opt1_type, K=K_call, T=T_call)
    print(call)
    
    # adding contract to portfolio  
    ptf.add_instrument(call, call_pos)
    print(ptf)
    
    #
    # Step 2: adding 5 short plain-vanilla put contracts
    #

    # plain-vanilla put option
    opt2_style = "plain_vanilla" # "digital"
    opt2_type = "put" # "call"   
    put = option_factory(market_env, opt2_style, opt2_type, K=K_put, T=T_put)
    print(put)
    
    # plain-vanilla put option
    put = PlainVanillaOption(market_env, option_type="put", K=K_put, T=T_put)
    print(put)
    
    # adding contract to portfolio  
    ptf.add_instrument(put, put_pos)
    print(ptf)
    
    #
    # Step 3: portfolio evaluation
    #
    

#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    