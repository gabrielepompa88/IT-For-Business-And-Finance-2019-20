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
    opt_style = "digital" # "plain_vanilla" # "digital"
    opt_type = "call" # "put"   
    option = option_factory(market_env, opt_style, opt_type)
    print(option)
        
    # option plotter instance
    plotter = OptionPlotter(option)
        
    # valuation date of the option
    emission_date = option.get_t()
            
    # select metrics to plot
    for plot_metrics in ["price", "PnL", "delta", "theta", "gamma", "vega", "rho"]:
        
        for time_kind in ['date', 'tau']:

            # set time-parameter to plot
            multiple_valuation_dates = get_time_parameter(option, kind=time_kind)
            print(multiple_valuation_dates)
                    
            # Surface plot
            plotter.plot(t=multiple_valuation_dates, plot_metrics=plot_metrics, 
                         surf_plot=True)
        
            # Surface plot (rotate) - Underlying value side
            plotter.plot(t=multiple_valuation_dates, plot_metrics=plot_metrics, 
                         surf_plot=True, view=(0,180))
        
            # Price surface plot (rotate) - Date side
            plotter.plot(t=multiple_valuation_dates, plot_metrics=plot_metrics, 
                         surf_plot=True, view=(0,-90))
            
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

