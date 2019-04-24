import sys, platform, os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pandas as pd
import scipy.integrate as integrate



def Eofz(z,w,om):

    E = np.sqrt(om*(1+z)**3.+(1-om)*(1+z)**(3.*(1+w)))

    return E

def metal_xi(z):

    xi = 0.015*((1+z)**2.7)/(1+((1+z)/2.9)**5.6)

    return xi

def metal_psi(z,w,om,H0):

    numerator   = metal_xi(z)
    denominator = H0*Eofz(z,w,om)*(1+z)

    psi = numerator/denominator 

    return psi

def getsys(z):
    
    metal_R  = 0.27#data.loc[data.parameter=='metal_R','mean'].values[0]
    metal_y  = 0.02#data.loc[data.parameter=='metal_y','mean'].values[0]
    H0       = 68.#data.loc[data.parameter=='H0*','mean'].values[0]
    ombh2    = 0.05*(H0/100)**2.#data.loc[data.parameter=='omegabh2','mean'].values[0]
    w        = -1
    om       = 0.3
    Gconst   = 4.30091e-3
    Zsun     = 0.0134
    rhoc     = (3*H0**2.)/(8.*3.14159*Gconst)
    omegab   = ombh2/(H0/100)**2.


       #TEST
       #ztest   = np.linspace(0,5,100)
       #psitest = np.zeros(len(ztest))
       #for ind in range(100):
       #    psitest[ind] = metal_psi(ztest[ind],w,om,H0)
       #plt.figure()
       #plt.plot(ztest,psitest)
       #plt.show()
       #exit()

    metal_rhostar = (1-metal_R)*integrate.quad(metal_psi,z,np.inf,args=(w,om,H0))[0]
    metal_Zb      = metal_y*(metal_rhostar/(omegab*rhoc))*(3.0857e13/(3600*24*365.25))
       
    #sys = -2.5*np.log10((1-0.18*metal_Zb)/(Zsun*(1-metal_Zb/Zsun)))-0.191
    sys = -2.5*np.log10(1.-0.18*(metal_Zb/Zsun)*(1.-0.10*metal_Zb/Zsun))-0.191
    return sys




plotred = np.linspace(0.01,3,1000)


sys = np.empty(len(plotred))
for ind in range(len(plotred)):
    sys[ind] = getsys(plotred[ind])
plt.figure()
plt.plot(plotred,sys)


plt.ylabel(r'$\Delta M_b$')
plt.xlabel(r'$z$')
plt.ylim([-0.2,0])

plt.show()
