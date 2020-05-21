import numpy as np

from market.market import MarketEnvironment
from options.options import PlainVanillaOption
from utils.numerical_routines import NumericalGreeks
from utils.utils import plot

def main():

    # numeric delta and gamma example
            
    # default market environment
    market_env = MarketEnvironment()
    print(market_env)

    # plain-vanilla call instance
    Vanilla_Call = PlainVanillaOption(market_env)
    print(Vanilla_Call)
    
    # numerical greeks instance
    NumGreeks = NumericalGreeks(Vanilla_Call)
    
    # underlying range at which compute greeks
    S_range = np.linspace(50, 150, 1000)
    
    # numeric delta
    delta_numerical = NumGreeks.delta(S0=S_range)
    
    # delta plot
    plot(x=S_range, f=delta_numerical, x_label=r"$S$", f_label=r"$\Delta_{call}(S)$", 
         f_up=np.ones(len(S_range)), f_up_label=r"Upper bound",
         f_down=np.zeros(len(S_range)), f_down_label=r"Lower bound",
         title=r"Numerical Delta of a plain-vanilla Call")
    
    # numeric gamma
    gamma_numerical = NumGreeks.gamma(S0=S_range)
    
    # gamma plot
    plot(x=S_range, f=gamma_numerical, x_label=r"$S$", f_label=r"$\Gamma_{call}(S)$", 
         title=r"Numerical Gamma of a plain-vanilla Call ($\epsilon=1e-4$ default)")
    
    # epsilon reduction: 1e-4 --> 1e-5
    NumGreeks = NumericalGreeks(Vanilla_Call, epsilon=1e-5)
    
    # numeric gamma
    gamma_numerical = NumGreeks.gamma(S0=S_range)
    
    # gamma plot
    plot(x=S_range, f=gamma_numerical, x_label=r"$S$", f_label=r"$\Gamma_{call}(S)$", 
         title=r"Numerical Gamma of a plain-vanilla Call ($\epsilon=1e-5$)")
    
    # epsilon further reduction: 1e-5 --> 1e-6
    NumGreeks = NumericalGreeks(Vanilla_Call, epsilon=1e-6)
    
    # numeric gamma
    gamma_numerical = NumGreeks.gamma(S0=S_range)
    
    # gamma plot
    plot(x=S_range, f=gamma_numerical, x_label=r"$S$", f_label=r"$\Gamma_{call}(S)$", 
         title=r"Numerical Gamma of a plain-vanilla Call ($\epsilon=1e-6$)")
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

