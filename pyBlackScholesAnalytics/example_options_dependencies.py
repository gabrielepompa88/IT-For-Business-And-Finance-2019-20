import numpy as np

from market.market import MarketEnvironment
from options.options import PlainVanillaOption, DigitalOption
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

def options_parameters_factory(parameter_name):
    
    param_dict = {"S": np.linspace(50, 150, 2000), 
                  "tau": np.linspace(0.0,1.0,1000)[::-1],
                  "sigma": np.linspace(0.0, 0.6, 1000),
                  "r": np.linspace(0.0, 0.1, 1000)}
    
    return {parameter_name: param_dict[parameter_name]}

def dependency_label(dependency_type, opt_type):

    call_put_label = r"Call$(" + dependency_type + ")$" if opt_type == "call"\
                     else r"Put$(" + dependency_type + ")$"
        
    return r"Black-Scholes price " + call_put_label

def dependency_title(opt, dependency_type):

    # plot common title
    common_title = opt.get_info() + "\n" + "Market at emission: " + opt.get_mkt_info()

    # complete title
    title = r"Price dependency Vs $" + dependency_type + r"$ for a " + common_title
    
    return title

def main():

    # option price dependencies example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)

    # define option style and type
    opt_style = "plain_vanilla" # "digital"
    opt_type = "call" # "call"  
    option = option_factory(market_env, opt_style, opt_type)
    print(option)

    # select dependency type
    for dependency_type in ["tau"]: #["S", "tau", "sigma", "r"]:
          
        # keyboard parameter and corresponding range to test
        param = options_parameters_factory(dependency_type)
        
        # price vector for the given parameter range in input
        opt_price = option.price(**param)
        
        # x-axis label
        x_label = r"$" + dependency_type +"$"
        
        # y-axis label
        y_label = dependency_label(dependency_type, opt_type)
        
        # plot title
        title = dependency_title(option, dependency_type)
        
        # plot
        plot(x=param[dependency_type], f=opt_price, 
             x_label=x_label, f_label=y_label, 
             title=title)  
        
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

