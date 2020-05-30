import pandas as pd

from market.market import MarketEnvironment
from options.options import PlainVanillaOption
from plotter.plotter import OptionPlotter


def main():
    
    # vanilla call implementation example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    Vanilla_Call = PlainVanillaOption(market_env)
    print(Vanilla_Call)
        
    # option plotter instance
    plotter = OptionPlotter(Vanilla_Call)
    
    # valuation date of the option
    emission_date = Vanilla_Call.get_t()
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
    expiration_date = Vanilla_Call.get_T()
    print(expiration_date)
    
    # a date-range of 5 valuation dates between t and T-10d
    multiple_valuation_dates = pd.date_range(start=emission_date, 
                                             end=expiration_date - pd.Timedelta(days=10), 
                                             periods=5)
    
    # Vanilla Call price plot at multiple dates
    plotter.plot(t=multiple_valuation_dates, plot_metrics="price")
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

