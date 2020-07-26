import numpy as np
import scipy.stats as si
from sympy.stats import Normal, cdf



class BlackAndScholesModel:
    def euro_vanilla(S, K, T, r, sigma, option = 'call'):

        #S: spot price
        #K: strike price
        #T: time to maturity
        #r: interest rate
        #sigma: volatility of underlying asset

        if T==0:
            if option=="call":
                if S-K>0:
                    return S-K
                return 0


            else:
                if K-S>0:
                    return K-S
                return 0



        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
        if option == 'call':
            result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
        if option == 'put':
            result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
        return result




