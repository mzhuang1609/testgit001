import numpy as np
from scipy.stats import norm
import time


class qlMarketData(object):

    def __init__(self, SF, r, q, vol):
        self.m_SF = SF
        self.m_r = r
        self.m_q = q
        self.m_vol = vol
        
        
class qlBlackScholes73(object):
    """
    calculate (S-K)^{+} where S is lognormal.

    KX : strike.
    MT : maturity.
    CP : call(0) or put(1).
    """

    def __init__(self, KX, MT, CP):
        self.m_KX = KX
        self.m_MT = MT
        self.m_CP = CP


    def calcPrice_np(self, md):
        vrt = md.m_vol * np.sqrt(self.m_MT)
        logMoneyness = np.log(md.m_SF / self.m_KX)
        d1 = (logMoneyness + (md.m_r - md.m_q) * self.m_MT) / vrt + \
            0.5 * vrt
        d2 = d1 - vrt
        price = 0.0

        df = np.exp(-md.m_r * self.m_MT)
        qt = np.exp(-md.m_q * self.m_MT)

        if self.m_CP == 0:
            price = md.m_SF * qt * norm.cdf(d1) - \
                self.m_KX * df * norm.cdf(d2)
        else:
            price = -md.m_SF * qt * norm.cdf(-d1) + \
                self.m_KX * df * norm.cdf(-d2)

        return price
    

def doit001():
    
    S0 = 100
    K = 100
    r = 0.08
    q = 0.04
    vol = 0.20
    T = 5.248633879781421
    CP = 1
    
    ns=1000000
    SS=S0*np.ones(ns)
    md=qlMarketData(SS, r, q, vol)
    
    bos=qlBlackScholes73(K, T, CP)

    tic=time.time()
    
    bos.calcPrice_np(md)
       
    toc=time.time()
    print('calculation done in {:.4f} seconds'.format(toc-tic))
    
    
if __name__ == '__main__':
    
    doit001()
