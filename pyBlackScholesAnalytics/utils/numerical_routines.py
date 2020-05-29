"""
Author: Gabriele Pompa (gabriele.pompa@gmail.com)

Date: 21-May-2020
File name: numerical_routines.py
"""

# ----------------------- standard imports ---------------------------------- #
# for NumPy arrays
import numpy as np

# ----------------------- sub-modules imports ------------------------------- #

from utils.utils import *

#-----------------------------------------------------------------------------#

class NumericalGreeks:
    
    def __init__(self, FinancialObject, epsilon=1e-4, method="price"):
        
        self.opt = FinancialObject
        self.f = getattr(FinancialObject, method)
        self.__eps = epsilon
        
    def get_epsilon(self):
        return self.__eps
    
    def set_epsilon(self, eps=1e-4):
        self.__eps=eps
                
    def delta(self, S0=None, **kwargs):
        S0 = self.opt.get_S() if S0 is None else S0
        return (self.f(S=S0+self.get_epsilon(), **kwargs) - self.f(S=S0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon())

    def gamma(self, S0=None, **kwargs):
        S0 = self.opt.get_S() if S0 is None else S0
        return (self.f(S=S0-self.get_epsilon(), **kwargs) - 2.0*self.f(S=S0, **kwargs) + self.f(S=S0+self.get_epsilon(), **kwargs))/(self.get_epsilon()*self.get_epsilon())
    
    def vega(self, sigma0=None, **kwargs):
        sigma0 = self.opt.get_sigma() if sigma0 is None else sigma0
        if is_iterable(sigma0):
            return np.array([(self.f(sigma=vol0+self.get_epsilon(), **kwargs) - self.f(sigma=vol0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon()) for vol0 in sigma0])
        else:
            return (self.f(sigma=sigma0+self.get_epsilon(), **kwargs) - self.f(sigma=sigma0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon())

    def theta(self, tau0=None, **kwargs):
        tau0 = self.opt.get_tau() if tau0 is None else tau0
        if is_iterable(tau0):
            return -np.array([(self.f(tau=ttm0+self.get_epsilon(), **kwargs) - self.f(tau=ttm0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon()) for ttm0 in tau0])/365.0
        else:
            return -((self.f(tau=tau0+self.get_epsilon(), **kwargs) - self.f(tau=tau0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon()))/365.0

    def rho(self, r0=None, **kwargs):
        r0 = self.opt.get_r() if r0 is None else r0
        if is_iterable(r0):
            return np.array([(self.f(r=sr0+self.get_epsilon(), **kwargs) - self.f(r=sr0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon()) for sr0 in r0])*0.01
        else:
            return ((self.f(r=r0+self.get_epsilon(), **kwargs) - self.f(r=r0-self.get_epsilon(), **kwargs))/(2*self.get_epsilon()))*0.01
