import pandas as pd

from utils.utils import date_string_to_datetime_obj
from market.market import MarketEnvironment
from options.options import PlainVanillaOption
from portfolio.portfolio import Portfolio

def main():

    #
    # portfolio instantiation example
    #
    
    # if np_output is True, the output will be np.ndarray, otherwise pd.DataFrame    
    np_output = False # True
        
    # default market environment
    market_env = MarketEnvironment(t="01-06-2020")
    print(market_env)

    # underlying values to test
    S_vector = [60, 90, 120]
    print("S_vector: {}\n".format(S_vector))
    
    # options maturities
    T_call = "31-12-2020"
    T_put = "30-06-2021"
    
    # options strikes
    K_put = 80
    K_call = 110
    
    # portfolio options positions
    call_pos = 2
    put_pos = -5

    # a date-range of 5 valuation dates between t and the nearest maturity
    t_range = pd.date_range(start=market_env.get_t(), 
                            end=min(T_call, T_put, key=date_string_to_datetime_obj), 
                            periods=5)

    print("t ([t...T] pd.date_range): {}\n".format(t_range))

    #
    # Step 0: empty portfolio initialized
    #
    
    ptf = Portfolio()
    print(ptf)
    
    #
    # Step 1: adding 2 long plain-vanilla call contracts
    #
    
    # plain-vanilla call option
    call = PlainVanillaOption(market_env, K=K_call, T=T_call)
    print(call)
        
    # adding contract to portfolio  
    ptf.add_instrument(call, call_pos)
    print(ptf)

    # portfolio value
    print("\nPortfolio Value:\n", ptf.price(S=S_vector, t=t_range, np_output=np_output))

    # verification with benchmark value
    bechmark_value = call_pos * call.price(S=S_vector, t=t_range, np_output=np_output)
    print("\nbenchmark value:\n", bechmark_value) 

    # portfolio P&L
    print("\nPortfolio P&L:\n", ptf.PnL(S=S_vector, t=t_range, np_output=np_output))
    
    # verification with benchmark P&L
    benchmark_pnl = call_pos * call.PnL(S=S_vector, t=t_range, np_output=np_output)      
    print("\nbenchmark P&L:\n", benchmark_pnl)
    
    #
    # Step 2: adding 5 short plain-vanilla put contracts
    #
    
    # plain-vanilla put option
    put = PlainVanillaOption(market_env, option_type="put", K=K_put, T=T_put)
    print(put)
    
    # adding contract to portfolio  
    ptf.add_instrument(put, put_pos)
    print(ptf)
    
    # portfolio value
    print("\nPortfolio Value:\n", ptf.price(S=S_vector, t=t_range, np_output=np_output))
    
    # verification with benchmark value
    benchmark_value = call_pos * call.price(S=S_vector, t=t_range, np_output=np_output) + \
                      put_pos * put.price(S=S_vector, t=t_range, np_output=np_output)
    print("\nbenchmark value:\n", benchmark_value) 

    # portfolio P&L
    print("\nPortfolio P&L:\n", ptf.PnL(S=S_vector, t=t_range, np_output=np_output))
    
    # verification with benchmark P&L
    call_pos * call.PnL(S=S_vector, t=t_range, np_output=np_output) + \
                                put_pos * put.PnL(S=S_vector, t=t_range, np_output=np_output)                         
    print("\nbenchmark P&L:\n", benchmark_pnl)
    
#----------------------------- usage example ---------------------------------#
if __name__ == "__main__":
    
    main()    

