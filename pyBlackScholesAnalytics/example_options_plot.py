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
    
    # Vanilla Call price plot at t
    plotter.plot(t=[emission_date], plot_metrics="price", plot_details=True)

    # Vanilla Call P&L plot at t
    plotter.plot(t=[emission_date], plot_metrics="PnL")

    # Vanilla Call price plot at another date-string date
    plotter.plot(t="01-06-2020", plot_metrics="price", plot_details=True)

    # Vanilla Call P&L plot at another date-string date
    plotter.plot(t="01-06-2020", plot_metrics="PnL")

    # emission/expiration date of the option
    expiration_date = option.get_T()
    print(expiration_date)
    
#    # a date-range of 5 valuation dates between t and T-10d
#    multiple_valuation_dates = pd.date_range(start=emission_date, 
#                                             end=expiration_date - pd.Timedelta(days=10), 
#                                             periods=5)
#    print(multiple_valuation_dates)
    
    multiple_valuation_dates = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    print(multiple_valuation_dates)
    
    # Vanilla Call price plot at multiple dates
    plotter.plot(t=multiple_valuation_dates, plot_metrics="price")

    # Vanilla Call price surface plot
    plotter.plot(t=multiple_valuation_dates, plot_metrics="price", 
                 surf_plot=True)

    # Vanilla Call price surface plot (rotate)
    # Underlying value side
    # focus on: time-decay at original Emission level (S=90)
    plotter.plot(t=multiple_valuation_dates, plot_metrics="price", 
                 surf_plot=True, view=(0,180))

    # Vanilla Call price surface plot (rotate)
    # Date side
    # focuse on: underlying value dependency
    plotter.plot(t=multiple_valuation_dates, plot_metrics="price", 
                 surf_plot=True, view=(0,-90))
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

