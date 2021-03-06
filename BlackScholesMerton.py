import numpy as np
from scipy.stats import norm

def BSM_d1(S, K, r, q, sigma, tau):
    ''' Computes d1 for the Black Merton Scholes formula '''
    d1 = 1.0*(np.log(1.0 * S/K) + (r - q + sigma**2/2) * tau) / (sigma * np.sqrt(tau))
    return d1

def BSM_d2(S, K, r, q, sigma, tau):
    ''' Computes d2 for the Black Merton Scholes formula '''
    d2 = 1.0*(np.log(1.0 * S/K) + (r - q - sigma**2/2) * tau) / (sigma * np.sqrt(tau))
    return d2

def BSM_price(type_option, S, K, r, q, sigma, T, t=0):
    ''' Computes the Black Merton Scholes price for a 'call' or 'put' option '''
    tau = T - t
    d1 = BSM_d1(S, K, r, q, sigma, tau)
    d2 = BSM_d2(S, K, r, q, sigma, tau)
    if type_option == 'call':
        price = S * np.exp(-q * tau) * norm.cdf(d1) - K * np.exp(-r * tau) * norm.cdf(d2)
    elif type_option == 'put':
        price = K * np.exp(-r * tau) * norm.cdf(-d2) - S * np.exp(-q * tau) * norm.cdf(-d1) 
    return price

def BSM_delta(type_option, S, K, r, q, sigma, T, t=0):
    ''' Computes the delta for a call or a put. '''
    tau = T - t
    d1 = BSM_d1(S, K, r, q, sigma, tau)
    if type_option == 'call':
        delta = np.exp(-q * tau) * norm.cdf(d1)
    elif type_option == 'put':
        delta = np.exp(-q * tau) * (norm.cdf(d1) - 1)
    return delta