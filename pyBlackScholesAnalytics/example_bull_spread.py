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
    expiration_date = bull_spread_ptf.get_T()
    print(expiration_date)
    
    for time_kind in ['date', 'tau']:
        
        if time_kind == 'date':
    
            # time-parameter as a date-range of 5 valuation dates between t and T-10d
            multiple_valuation_dates = pd.date_range(start=valuation_date, 
                                                     end=expiration_date - pd.Timedelta(days=20), 
                                                     periods=5)
        else:
            
            # (alternatively) time-parameter as a list of times-to-maturity
            multiple_valuation_dates = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    
        print(multiple_valuation_dates)
    
        
        #
        # Bull-Spread plot (multiple dates)
        #
        
        # price
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="price")
        
        # P&L
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="PnL")
    
        #
        # Bull-Spread price surface plot 
        #
        
        # price
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="price", 
                                     surf_plot=True)
    
        # PnL
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="PnL", 
                                     surf_plot=True)
    
        #
        # Bull-Spread price surface plot 
        # Underlying value side
        # focus on: time-decay at original Emission level (S=90)
        # 
    
        # price
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="price", 
                                     surf_plot=True, view=(0,180))
    
        # PnL
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="PnL", 
                                     surf_plot=True, view=(0,180))

        #
        # Bull-Spread price surface plot 
        # Date side
        # focuse on: underlying value dependency
        #
    
        # price
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="price", 
                                     surf_plot=True, view=(0,-90))
    
        # PnL
        bull_spread_ptf_plotter.plot(t=multiple_valuation_dates, plot_metrics="PnL", 
                                     surf_plot=True, view=(0,-90))
        
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

