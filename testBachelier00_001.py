import numpy as np
import math
from scipy.stats import norm
import time


class qlMarketData(object):

    def __init__(self, SF, r, q, vol):
        self.m_SF = SF
        self.m_r = r
        self.m_q = q
        self.m_vol = vol
        
        
class qlBachelier00(object):
    """
    ccalculate (S-K)^{+} where S is normal distribution.

    KX : strike.
    MT : maturity.
    CP : call(0) or put(1).
    """

    def __init__(self, KX, MT, CP):
        self.m_KX = KX
        self.m_MT = MT
        self.m_CP = CP


    def calcPrice_0(self, md):
        vrt = md.m_vs*math.sqrt(self.m_MT)
        moneyness = md.m_SFs-self.m_KX
        price = 0.0

        d1 = moneyness/vrt

        if self.m_CP == 0:
            price = (md.m_SFs-self.m_KX) * fnorm.qlStdNormCdf(d1) + \
                vrt * fnorm.qlStdNormPdf(d1)
        else:
            price = (self.m_KX-md.m_SFs) * fnorm.qlStdNormCdf(-d1) + \
                vrt * fnorm.qlStdNormPdf(d1)

        return math.exp(-md.m_rs*self.m_MT)*price


    def calcPrice_np(self, md):
        vrt = md.m_vol*np.sqrt(self.m_MT)
        moneyness = md.m_SF-self.m_KX
        price = 0.0

        d1 = moneyness/vrt

        if self.m_CP == 0:
            price = (md.m_SF-self.m_KX) * norm.cdf(d1) + \
                vrt * norm.pdf(d1)
        else:
            price = (self.m_KX-md.m_SF) * norm.cdf(-d1) + \
                vrt * norm.pdf(d1)

        return np.exp(-md.m_r*self.m_MT)*price
    
    
def doit001():
    
    S0 = 100
    K = 100
    r = 0.04
    vol = 0.20
    T = 5.248633879781421
    CP = 1
    
    ns=1000000
    SS=S0*np.ones(ns)
    md=qlMarketData(SS, r, 0.0, vol)
    
    bos=qlBachelier00(K, T, CP)

    tic=time.time()
    
    bos.calcPrice_np(md)

    toc=time.time()
    print('FEL _np in {:.4f} seconds'.format(toc-tic))
    
    
   
if __name__ == '__main__':
    
    doit001()
    
