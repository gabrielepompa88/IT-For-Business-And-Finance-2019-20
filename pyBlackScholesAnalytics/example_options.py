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
    # option instantiation example
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
    
    # 
    # Case 1: (S scalar, tau scalar) default values
    #    
    print("\n--------------------------------------------\n")
    print("Case 1: (S scalar, tau scalar) default values \n")
        
    print("S (default): {}\n".format(option.get_S()))
    print("tau (default): {}\n".format(option.get_tau()))
    
    print("Payoff:\n", option.payoff(np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(np_output=np_output))
    print("Price:\n", option.price(np_output=np_output))
    print("P&L:\n", option.PnL(np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(np_output=np_output))
    print("Delta:\n", option.delta(np_output=np_output))
    print("Theta:\n", option.theta(np_output=np_output))
    print("Gamma:\n", option.gamma(np_output=np_output))
    print("Vega:\n", option.vega(np_output=np_output))
    print("Rho:\n", option.rho(np_output=np_output))
      
    #     
    # Case 2: (S scalar, tau scalar) other values
    #
    print("\n--------------------------------------------\n")
    print("\nCase 2: (S scalar, tau scalar) input values \n")
    
    S_scalar = 100
    print("S_scalar: {}\n".format(S_scalar))

    # valuation date time-parameter as datetime object
    print("\n----------------\n")    
    print("\n--- Case 2.1 ---\n")    
    t_scalar = option.get_t()
    print("t_scalar (dt obj): ", t_scalar)
    
    print("Payoff:\n", option.payoff(S=S_scalar, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Price:\n", option.price(S=S_scalar, t=t_scalar, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Delta:\n", option.delta(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Theta:\n", option.theta(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Vega:\n", option.vega(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Rho:\n", option.rho(S=S_scalar, t=t_scalar, np_output=np_output))

    # valuation date time-parameter as date String
    print("\n----------------\n")    
    print("\n--- Case 2.2 ---\n")    
    t_scalar = "01-06-2020"
    print("t_scalar (str): ", t_scalar)

    print("Payoff:\n", option.payoff(S=S_scalar, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Price:\n", option.price(S=S_scalar, t=t_scalar, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Delta:\n", option.delta(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Theta:\n", option.theta(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Vega:\n", option.vega(S=S_scalar, t=t_scalar, np_output=np_output))
    print("Rho:\n", option.rho(S=S_scalar, t=t_scalar, np_output=np_output))

    # time-to-maturity time-parameter 
    print("\n----------------\n")    
    print("\n--- Case 2.3 ---\n")    
    tau_scalar = 0.5
    print("tau_scalar (Float): ", tau_scalar)

    print("Payoff:\n", option.payoff(S=S_scalar, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Price:\n", option.price(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Delta:\n", option.delta(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Theta:\n", option.theta(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Vega:\n", option.vega(S=S_scalar, tau=tau_scalar, np_output=np_output))
    print("Rho:\n", option.rho(S=S_scalar, tau=tau_scalar, np_output=np_output))

    #     
    # Case 3: (S vector, tau scalar) tau is left default (0.7014...)
    #
    print("\n--------------------------------------------\n")
    print("\nCase 3: (S vector, tau scalar) tau is left default (0.7014...) \n")

    S_vector = [90, 100, 110]
    
    print("S_vector: {}\n".format(S_vector))
    print("tau (default): {}\n".format(option.get_tau()))

    print("Payoff:\n", option.payoff(S=S_vector, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_vector, np_output=np_output))
    print("Delta:\n", option.delta(S=S_vector, np_output=np_output))
    print("Theta:\n", option.theta(S=S_vector, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_vector, np_output=np_output))
    print("Vega:\n", option.vega(S=S_vector, np_output=np_output))
    print("Rho:\n", option.rho(S=S_vector, np_output=np_output))
    
    #     
    # Case 4: (S scalar, tau vector) S is left default (90)
    #    
    print("\n--------------------------------------------\n")
    print("\nCase 4: (S scalar, tau vector) S is left default (90) \n")

    print("S (default): {}\n".format(option.get_S()))

    
    # a date-range of 5 valuation dates between t and T-10d
    valuation_date = option.get_t()
    expiration_date = option.get_T()
    t_range = pd.date_range(start=valuation_date, 
                            end=expiration_date, 
                            periods=5)

    print("t ([t...T] pd.date_range): {}\n".format(t_range))
    
    print("Payoff:\n", option.payoff(t=t_range, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(t=t_range, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(t=t_range, np_output=np_output))
    print("Price:\n", option.price(t=t_range, np_output=np_output))
    print("P&L:\n", option.PnL(t=t_range, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(t=t_range, np_output=np_output))
    print("Delta:\n", option.delta(t=t_range, np_output=np_output))
    print("Theta:\n", option.theta(t=t_range, np_output=np_output))
    print("Gamma:\n", option.gamma(t=t_range, np_output=np_output))
    print("Vega:\n", option.vega(t=t_range, np_output=np_output))
    print("Rho:\n", option.rho(t=t_range, np_output=np_output))

    #     
    # Case 5: (S vector, tau vector) 
    #
    print("\n--------------------------------------------\n")
    print("\nCase 5: (S vector, tau vector) \n")
 
    print("S_vector: {}\n".format(S_vector))
 
    # time-parameter as pd.date_range
    print("\n----------------\n")    
    print("\n--- Case 5.1 ---\n")    
    print("t ([t...T] pd.date_range): {}\n".format(t_range))
    
    print("Payoff:\n", option.payoff(S=S_vector, t=t_range, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, t=t_range, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, t=t_range, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, t=t_range, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, t=t_range, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_vector, t=t_range, np_output=np_output))
    print("Delta:\n", option.delta(S=S_vector, t=t_range, np_output=np_output))
    print("Theta:\n", option.theta(S=S_vector, t=t_range, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_vector, t=t_range, np_output=np_output))
    print("Vega:\n", option.vega(S=S_vector, t=t_range, np_output=np_output))
    print("Rho:\n", option.rho(S=S_vector, t=t_range, np_output=np_output))
    
    # time-parameter as List of date Strings
    print("\n----------------\n")    
    print("\n--- Case 5.2 ---\n")    
    t_list = ["10-07-2020", "11-09-2020", "06-08-2020", "15-10-2020", "01-06-2020"] # order doesn't matter
    print("t ([date_str_1, ..., date_str_N] List of str): {}\n".format(t_list))
    
    print("Payoff:\n", option.payoff(S=S_vector, t=t_list, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, t=t_list, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, t=t_list, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, t=t_list, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, t=t_list, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_vector, t=t_list, np_output=np_output))
    print("Delta:\n", option.delta(S=S_vector, t=t_list, np_output=np_output))
    print("Theta:\n", option.theta(S=S_vector, t=t_list, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_vector, t=t_list, np_output=np_output))
    print("Vega:\n", option.vega(S=S_vector, t=t_list, np_output=np_output))
    print("Rho:\n", option.rho(S=S_vector, t=t_list, np_output=np_output))

    # time-parameter as List of times-to-maturity
    print("\n----------------\n")    
    print("\n--- Case 5.3 ---\n")    
    tau_list = [0.3, 0.4, 0.5, 0.6, 0.7]
    print("tau_vector (List of Float): {}\n".format(tau_list))

    print("Payoff:\n", option.payoff(S=S_vector, tau=tau_list, np_output=np_output))
    print("Price upper limit:\n", option.price_upper_limit(S=S_vector, tau=tau_list, np_output=np_output))
    print("Price lower limit:\n", option.price_lower_limit(S=S_vector, tau=tau_list, np_output=np_output))
    print("Price:\n", option.price(S=S_vector, tau=tau_list, np_output=np_output))
    print("P&L:\n", option.PnL(S=S_vector, tau=tau_list, np_output=np_output))
    print("Implied Volatility (expected iv={}):\n".format(option.get_sigma()), 
          option.implied_volatility(S=S_vector, tau=tau_list, np_output=np_output))
    print("Delta:\n", option.delta(S=S_vector, tau=tau_list, np_output=np_output))
    print("Theta:\n", option.theta(S=S_vector, tau=tau_list, np_output=np_output))
    print("Gamma:\n", option.gamma(S=S_vector, tau=tau_list, np_output=np_output))
    print("Vega:\n", option.vega(S=S_vector, tau=tau_list, np_output=np_output))
    print("Rho:\n", option.rho(S=S_vector, tau=tau_list, np_output=np_output))
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

