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
    
    # option instantiation example
    
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    option = option_factory(market_env, "plain_vanilla", "call")
#    option = option_factory(market_env, "plain_vanilla", "put")
#    option = option_factory(market_env, "digital", "call")
#    option = option_factory(market_env, "digital", "put")
    print(option)
    
    # 
    # Case 1: (S scalar, tau scalar) default values
    #    
    print("Case 1: (S scalar, tau scalar) default values \n")
    
    print("S (default): {}\n".format(option.get_S()))
    print("tau (default): {}\n".format(option.get_tau()))
    
    print("Price:\n", option.price())
    print("P&L:\n", option.PnL())
      
    #     
    # Case 2: (S scalar, tau scalar) other values
    #
    print("\nCase 2: (S scalar, tau scalar) input values \n")
    
    S_scalar = 100
    print("S_scalar: {}\n".format(S_scalar))

    # valuation date time-parameter as datetime object
    print("\n--- Case 2.1 ---\n")    
    t_scalar = option.get_t()
    print("t_scalar (dt obj): ", t_scalar)
    
    print("Price:\n", option.price(S=S_scalar, t=t_scalar))
    print("P&L:\n", option.PnL(S=S_scalar, t=t_scalar))

    # valuation date time-parameter as date String
    print("\n--- Case 2.2 ---\n")    
    t_scalar = "01-06-2020"
    print("t_scalar (str): ", t_scalar)

    print("Price:\n", option.price(S=S_scalar, t=t_scalar))
    print("P&L:\n", option.PnL(S=S_scalar, t=t_scalar))

    # time-to-maturity time-parameter 
    print("\n--- Case 2.3 ---\n")    
    tau_scalar = 0.5
    print("tau_scalar (str): ", tau_scalar)

    print("Price:\n", option.price(S=S_scalar, tau=tau_scalar))
    print("P&L:\n", option.PnL(S=S_scalar, tau=tau_scalar))

    #     
    # Case 3: (S vector, tau scalar) tau is left default (0.7014...)
    #
    print("\nCase 3: (S vector, tau scalar) tau is left default (0.7014...) \n")

    S_vector = [90, 100, 110]
    
    print("S_vector: {}\n".format(S_vector))
    print("tau (default): {}\n".format(option.get_tau()))

    print("Price:\n", option.price(S=S_vector))
    print("P&L:\n", option.PnL(S=S_vector))
    
    #     
    # Case 4: (S scalar, tau vector) S is left default (90)
    #    
    print("\nCase 4: (S scalar, tau vector) S is left default (90) \n")

    print("S (default): {}\n".format(option.get_S()))

    
    # a date-range of 5 valuation dates between t and T-10d
    valuation_date = option.get_t()
    expiration_date = option.get_T()
    t_range = pd.date_range(start=valuation_date, 
                            end=expiration_date, 
                            periods=5)

    print("t ([t...T] pd.date_range): {}\n".format(t_range))
    
    print("Price:\n", option.price(t=t_range))
    print("P&L:\n", option.PnL(t=t_range))

    #     
    # Case 5: (S vector, tau vector) 
    #
    print("\nCase 5: (S vector, tau vector) \n")
 
    print("S_vector: {}\n".format(S_vector))
 
    # time-parameter as pd.date_range
    print("\n--- Case 5.1 ---\n")    
    print("t ([t...T] pd.date_range): {}\n".format(t_range))
    
    print("Price:\n", option.price(S=S_vector, t=t_range))
    print("P&L:\n", option.PnL(S=S_vector, t=t_range))
    
    # time-parameter as List of date Strings
    print("\n--- Case 5.2 ---\n")    
    t_list = ["01-06-2020", "01-07-2020", "01-08-2020", "01-09-2020", "01-10-2020"]
    print("t ([date_str_1, ..., date_str_N] List of str): {}\n".format(t_list))
    
    print("Price:\n", option.price(S=S_vector, t=t_list))
    print("P&L:\n", option.PnL(S=S_vector, t=t_list))

    # time-parameter as List of times-to-maturity
    print("\n--- Case 5.3 ---\n")    
    tau_list = [0.3, 0.4, 0.5, 0.6, 0.7]

    print("Price:\n", option.price(S=S_vector, tau=tau_list))
    print("P&L:\n", option.PnL(S=S_vector, tau=tau_list))
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

