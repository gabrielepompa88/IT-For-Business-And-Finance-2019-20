import numpy as np

from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption
from utils.numeric_routines import NumericGreeks
from utils.utils import plot

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

def label_dispatcher(option_type):
    
    labels = {"call": "_{Call}",
              "put": "_{Put}"}
    
    return labels[option_type]

def main():

    # numeric delta and gamma example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)

    # define option style and type
    opt_style = "plain_vanilla" # "digital"
    opt_type = "call" # "put"  
    option = option_factory(market_env, opt_style, opt_type)
    print(option)

    # plot common title
    common_title = option.get_info() + "\n" + "Market at emission: " + option.get_mkt_info()
    
    # option type plot suffix 
    suffix = label_dispatcher(opt_type)
    
    # numeric greeks instance
    NumGreeks = NumericGreeks(option)
    
    # underlying range at which compute greeks
    S_range = np.linspace(50, 150, 2000)
    
    # numeric delta
    delta_numerical = NumGreeks.delta(S0=S_range)
    
    # delta plot
    plot(x=S_range, f=delta_numerical, x_label=r"$S$", f_label=r"$\Delta"+suffix+"(S)$", 
         title=r"Numeric Delta of a " + common_title)
    
    # numeric gamma
    gamma_numerical = NumGreeks.gamma(S0=S_range)
    
    # gamma plot
    plot(x=S_range, f=gamma_numerical, x_label=r"$S$", f_label=r"$\Gamma(S)$", 
         title=r"Numeric Gamma of a " + common_title)  
    
    # numeric theta
    theta_numerical = NumGreeks.theta(S=S_range)
    
    # theta plot
    plot(x=S_range, f=theta_numerical, x_label=r"$S$", f_label=r"$\Theta"+suffix+"(S)$",
         title=r"Numeric Theta of a " + common_title)
    
    # numeric vega
    vega_numerical = NumGreeks.vega(S=S_range)
    
    # vega plot
    plot(x=S_range, f=vega_numerical, x_label=r"$S$", f_label=r"Vega$(S)$", 
         title=r"Numeric Vega of a " + common_title)

    # numeric rho
    rho_numerical = NumGreeks.rho(S=S_range)
    
    # rho plot
    plot(x=S_range, f=rho_numerical, x_label=r"$S$", f_label=r"$\rho"+suffix+"(S)$", 
         title=r"Numeric Rho of a " + common_title)
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

