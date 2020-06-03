import pandas as pd

from market.market import MarketEnvironment
from portfolio.portfolio import Portfolio
from options.options import PlainVanillaOption
from plotter.plotter import PortfolioPlotter


def main():
    
    # Bull-Spread implementation example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)
    
    # options strikes
    K_long = 80
    K_short = 110

    # bull-spread portfolio initialized (as empty portfolio)   
    bull_spread_ptf = Portfolio(name="Bull Spread Strategy")
    print(bull_spread_ptf)

    # 80-call
    Vanilla_Call_long = PlainVanillaOption(market_env, K=K_long, T='31-12-2021')
    print(Vanilla_Call_long)
    
    # 110-call
    Vanilla_Call_short = PlainVanillaOption(market_env, K=K_short, T='31-12-2021')
    print(Vanilla_Call_short)

    # creation of bull-spread portfolio strategy   
    bull_spread_ptf.add_instrument(Vanilla_Call_long, 1)
    bull_spread_ptf.add_instrument(Vanilla_Call_short, -1)    
    print(bull_spread_ptf)
    
    # portfolio plotter instance
    bull_spread_ptf_plotter = PortfolioPlotter(bull_spread_ptf)
    
    # Bull-Spread price plot
    bull_spread_ptf_plotter.plot(t='01-06-2020', plot_metrics="price", plot_details=True)

    # Bull-Spread P&L plot
    bull_spread_ptf_plotter.plot(t='01-06-2020', plot_metrics="PnL", plot_details=True)
    
    # valuation date of the portfolio
    valuation_date = bull_spread_ptf.get_t()
    print(valuation_date)
    
    # expiration date of the option
    expiration_date = Vanilla_Call_long.get_T()
    print(expiration_date)
    
    # a date-range of 5 valuation dates between t and T-10d
    multiple_valuation_dates = pd.date_range(start=valuation_date, 
                                             end=expiration_date - pd.Timedelta(days=10), 
                                             periods=5)
    
    print(multiple_valuation_dates)
    
    # Bull-Spread price plot (multiple dates)
    bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="price")

    # Bull-Spread P&L plot (multiple dates)
    bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="PnL")
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

