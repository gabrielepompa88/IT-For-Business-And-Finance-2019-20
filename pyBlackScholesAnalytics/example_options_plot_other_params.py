import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

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

def options_x_axis_parameters_factory(option, parameter_name):
    
    param_dict = {"S": option.get_S(), 
                  "K": option.get_K(),
                  "sigma": option.get_sigma(),
                  "r": option.get_r()}
    
    return {parameter_name: param_dict[parameter_name]}

def get_time_parameter(option, kind='date'):
    
    # date time-parameter
    if kind == 'date':
        
        # valuation date of the option
        emission_date = option.get_t()
    
        # emission/expiration date of the option
        expiration_date = option.get_T()
        
        # time-parameter as a date-range of 5 valuation dates between t and T-10d
        time_parameter = pd.date_range(start=emission_date, 
                                       end=expiration_date - pd.Timedelta(days=20),
                                       periods=5)
        
    # time-to-maturity time parameter    
    else: 
        
        # time-parameter as a list of times-to-maturity
        time_parameter = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
        
    return time_parameter

def main():
    
    # vanilla call implementation example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    # define option style and type
    opt_style = "plain_vanilla" # "digital"
    opt_type = "call" # "put"   
    option = option_factory(market_env, opt_style, opt_type)
    print(option)
        
    # option plotter instance
    plotter = OptionPlotter(option)
        
    # valuation date of the option
    emission_date = option.get_t()
    print(emission_date)
    
    # select dependency to plot as x-axis of the plot
    for dependency_type in ["S", "K", "sigma", "r"]:
    
        # keyboard parameter and corresponding range to test
        x_axis_dict = options_x_axis_parameters_factory(option, dependency_type)    
        
        # select metrics to plot
        for plot_metrics in ["price", "PnL", "delta", "theta", "gamma", "vega", "rho"]:
            
            plot_details_flag = True if plot_metrics == "price" else False
            
            # Plot at t
            plotter.plot(**x_axis_dict, t=[emission_date], 
                         plot_metrics=plot_metrics, plot_details=plot_details_flag)
        
            # Plot at another date-string date
            plotter.plot(**x_axis_dict, t="01-06-2020", 
                         plot_metrics=plot_metrics, plot_details=plot_details_flag)
            
            # multi-time plot available only if S or K parameters are chosen for x-axis.
            # This, because if t/tau is a vector, sigma/r are expected to be either scalar
            # or vectors with shape constrained to be the same of the t/tau shape 
            # to be distributed accordigly. See EuropeanOption.price() docstring
            if dependency_type in ["S", "K"]:
    
                for time_kind in ['date', 'tau']:
        
                    # set time-parameter to plot
                    multiple_valuation_dates = get_time_parameter(option, kind=time_kind)
                    print(multiple_valuation_dates)
                
                    # Plot at multiple dates
                    plotter.plot(**x_axis_dict, t=multiple_valuation_dates, 
                                 plot_metrics=plot_metrics)
        
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

