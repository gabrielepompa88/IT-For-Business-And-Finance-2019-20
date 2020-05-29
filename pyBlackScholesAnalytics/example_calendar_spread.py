import pandas as pd

from market.market import MarketEnvironment
from portfolio.portfolio import Portfolio
from options.options import PlainVanillaOption
from plotter.plotter import PortfolioPlotter


def main():
    
    # Calendar-Spread implementation example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    # options expirations
    T_short = "31-05-2020"
    T_long = "30-08-2020"
    
    # current underlying level
    S_t = market_env.get_S()

    # calendar-spread portfolio initialized (as empty portfolio)   
    calendar_spread_ptf = Portfolio(name="Calendar Spread Strategy")
    print(calendar_spread_ptf)

    # T_short-call
    Vanilla_Call_short = PlainVanillaOption(market_env, T=T_short, K=S_t)
    print(Vanilla_Call_short)
    
    # T_long-call
    Vanilla_Call_long = PlainVanillaOption(market_env, T=T_long, K=S_t)
    print(Vanilla_Call_long)

    # creation of Calendar-Spread portfolio strategy   
    calendar_spread_ptf.add_instrument(Vanilla_Call_short, -1)    
    calendar_spread_ptf.add_instrument(Vanilla_Call_long, 1)
    print(calendar_spread_ptf)
    
    # portfolio plotter instance
    calendar_spread_ptf_plotter = PortfolioPlotter(calendar_spread_ptf)
    
    # Calendar-Spread price plot
    calendar_spread_ptf_plotter.plot(t=T_short, plot_metrics="price", plot_details=True)

    # Calendar-Spread P&L plot
    calendar_spread_ptf_plotter.plot(t=T_short, plot_metrics="PnL", plot_details=True)
    
    # current date 
    valuation_date = market_env.get_t()
    print(valuation_date)
        
    # a date-range of 5 valuation dates between t and T_short
    multiple_valuation_dates = pd.date_range(start=valuation_date, 
                                             end=T_short, 
                                             periods=5)
    
    print(multiple_valuation_dates)
    
    # Calendar-Spread price plot (multiple dates)
    calendar_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="price", n=500)

    # Calendar-Spread P&L plot (multiple dates)
    calendar_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="PnL", n=500)
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

