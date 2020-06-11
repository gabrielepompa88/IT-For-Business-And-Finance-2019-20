import numpy as np

from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption
from utils.numeric_routines import NumericGreeks
from utils.utils import plot_compare

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

def greeks_factory(ObjWithGreeksMethod, greek_type):
    
    greeks_dispatcher = {"delta": ObjWithGreeksMethod.delta,
                         "theta": ObjWithGreeksMethod.theta,
                         "gamma": ObjWithGreeksMethod.gamma,
                         "vega":  ObjWithGreeksMethod.vega,
                         "rho":   ObjWithGreeksMethod.rho
    }
    
    return greeks_dispatcher[greek_type]
    
def greeks_label_factory(greek_type, opt_type, kind):

    labels_dispatcher = {"delta": r"\Delta^{" + kind + "}_{" + opt_type + "}(S)",
                         "theta": r"\Theta^{" + kind + "}_{" + opt_type + "}(S)",
                         "gamma": r"\Gamma^{" + kind + "}_{" + opt_type + "}(S)",
                         "vega":  r"Vega^{" + kind + "}_{" + opt_type + "}(S)",
                         "rho":  r"\rho^{" + kind + "}_{" + opt_type + "}(S)"
    }
    
    return labels_dispatcher[greek_type]

def main():

    # numeric Vs analytic greeks example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)

    # define option style and type
    opt_style = "plain_vanilla" # "digital"
    opt_type = "call" # "put"  
    option = option_factory(market_env, opt_style, opt_type)
    print(option)
    
    # select greek
    greek_type = "theta"
    
    # plot common title
    common_title = option.get_info() + "\n" + "Market at emission: " + option.get_mkt_info()
    
    # underlying range at which compute greeks
    S_range = np.linspace(50, 150, 2000)
    
    # analytic greek
    greek_analytic = greeks_factory(option, greek_type)(S=S_range)

    # numeric greeks instance
    NumGreeks = NumericGreeks(option)
    
    # numeric greek
    greek_numeric = greeks_factory(NumGreeks, greek_type)(S=S_range)
    
    # labels
    label_numeric = greeks_label_factory(greek_type, opt_type, kind="num")
    label_analytic = greeks_label_factory(greek_type, opt_type, kind="exact")
    
    
    # comparison
    plot_compare(S_range, f=greek_numeric, f_ref=greek_analytic, 
                 f_label=label_numeric, f_ref_label=label_analytic,
                 x_label="S",
                 title=r"Numeric Vs Exact " + greek_type + " comparison for a \n" + common_title)
    
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

