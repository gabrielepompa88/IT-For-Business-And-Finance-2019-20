import pandas as pd

from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption
from plotter.plotter import OptionPlotter

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

    print(option.price())
    print(option.PnL())
      
    #     
    # Case 2: (S scalar, tau scalar) other values
    #
    print("\nCase 2: (S scalar, tau scalar) other values \n")
    
    # valuation date time-parameter as datetime object
    valuation_date = option.get_t()
    print(valuation_date)
    
    print(option.price(S=100, t=valuation_date))
    print(option.PnL(S=100, t=valuation_date))

    # valuation date time-parameter as date String
    valuation_date = "01-06-1988"
    print(valuation_date)

    print(option.price(S=100, t=valuation_date))
    print(option.PnL(S=100, t=valuation_date))

    # time-to-maturity time-parameter 
    ttm = option.get_tau()
    print(ttm)

    print(option.price(S=100, tau=ttm))
    print(option.PnL(S=100, tau=ttm))

    #     
    # Case 3: (S vector, tau scalar) tau is left default (0.7014...)
    #
    print("\nCase 3: (S vector, tau scalar) tau is left default (0.7014...) \n")

    print(option.price(S=[90, 100]))
    print(option.PnL(S=[90, 100]))
    
    #     
    # Case 4: (S scalar, tau vector) S is left default (90)
    #    
    print("\nCase 4: (S scalar, tau vector) S is left default (90) \n")

    expiration_date = option.get_T()
    print(expiration_date)
    
    # a date-range of 5 valuation dates between t and T-10d
    multiple_valuation_dates = pd.date_range(start=valuation_date, 
                                             end=expiration_date, 
                                             periods=4)

    print(multiple_valuation_dates)
    
    print(option.price(t=multiple_valuation_dates))
    print(option.PnL(t=multiple_valuation_dates))

    #     
    # Case 5: (S vector, tau vector) 
    #
    print("\nCase 5: (S vector, tau vector) \n")
    
    print(option.price(S=[90, 100], t=multiple_valuation_dates))
    print(option.PnL(S=[90, 100], t=multiple_valuation_dates))
    
    print(option.price(S=[90, 100], t=["01-06-2020", "01-08-2020", "01-10-2020"]))
    print(option.PnL(S=[90, 100], t=["01-06-2020", "01-08-2020", "01-10-2020"]))

    print(option.price(S=[90, 100], t=[0.5, 0.6, 0.7]))
    print(option.PnL(S=[90, 100], t=[0.5, 0.6, 0.7]))
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

