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

def main():

    #
    # option instantiation example with combinations of iterable parameters
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
    
    #
    # iterable parameters
    #
    
    # S
    S_vector = [90, 100, 110]
    
    # tau: a date-range of 5 valuation dates between t and T-10d
    valuation_date = option.get_t()
    expiration_date = option.get_T()
    t_vector = pd.date_range(start=valuation_date, 
                             end=expiration_date, 
                             periods=5)
    
    # sigma
    sigma_vector = [0.0, 0.1, 0.2, 0.3]
    
    # r
    r_vector = [0.0, 0.01, 0.025, 0.03, 0.04, 0.05]
    
    #
    # 1 - (S,t) iterables
    #

    print("\nCase 1 - (S vector, t vector) \n")
 
    print("S_vector: {}\n".format(S_vector))
    print("t_vector: {}\n".format(t_vector))
    
    print("Payoff:\n", option.payoff(S=S_vector, t=t_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, t=t_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, t=t_vector, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, t=t_vector, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, t=t_vector, np_output=np_output))
    
    #
    # 2 - (S,sigma) iterables
    #

    print("\nCase 2 - (S vector, sigma vector) \n")
 
    print("S_vector: {}\n".format(S_vector))
    print("sigma_vector: {}\n".format(sigma_vector))
    
    print("Payoff:\n", option.payoff(S=S_vector, sigma=sigma_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, sigma=sigma_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, sigma=sigma_vector, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, sigma=sigma_vector, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, sigma=sigma_vector, np_output=np_output))

    #
    # 3 - (S, r) iterables
    #

    print("\nCase 3 - (S vector, r vector) \n")
 
    print("S_vector: {}\n".format(S_vector))
    print("r_vector: {}\n".format(r_vector))
    
    print("Payoff:\n", option.payoff(S=S_vector, r=r_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, r=r_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, r=r_vector, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, r=r_vector, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, r=r_vector, np_output=np_output))

    #
    # 4 - (t, sigma) iterables
    #

    print("\nCase 4 - (t vector, sigma vector) \n")
 
    print("t_vector: {}\n".format(t_vector))
    print("sigma_vector: {}\n".format(sigma_vector))
    
    print("Payoff:\n", option.payoff(t=t_vector, sigma=sigma_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(t=t_vector, sigma=sigma_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(t=t_vector, sigma=sigma_vector, np_output=np_output))
    print("Price:\n", option.price(t=t_vector, sigma=sigma_vector, np_output=np_output))
    print("P&L:\n", option.PnL(t=t_vector, sigma=sigma_vector, np_output=np_output))

    #
    # 5 - (t, r) iterables
    #

    print("\nCase 5 - (t vector, r vector) \n")
 
    print("t_vector: {}\n".format(t_vector))
    print("r_vector: {}\n".format(r_vector))
    
    print("Payoff:\n", option.payoff(t=t_vector, r=r_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(t=t_vector, r=r_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(t=t_vector, r=r_vector, np_output=np_output))
    print("Price:\n", option.price(t=t_vector, r=r_vector, np_output=np_output))
    print("P&L:\n", option.PnL(t=t_vector, r=r_vector, np_output=np_output))

    #
    # (sigma, r) iterables
    #

    print("\nCase 6 - (sigma vector, r vector) \n")
 
    print("sigma_vector: {}\n".format(sigma_vector))
    print("r_vector: {}\n".format(r_vector))
    
    print("Payoff:\n", option.payoff(sigma=sigma_vector, r=r_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(sigma=sigma_vector, r=r_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(sigma=sigma_vector, r=r_vector, np_output=np_output))
    print("Price:\n", option.price(sigma=sigma_vector, r=r_vector, np_output=np_output))
    print("P&L:\n", option.PnL(sigma=sigma_vector, r=r_vector, np_output=np_output))
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

