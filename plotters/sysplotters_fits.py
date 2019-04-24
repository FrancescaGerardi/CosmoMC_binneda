import sys, platform, os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pandas as pd
import scipy.integrate as integrate


#smoothed spline interpolator
def getw(ytab,xin):

    #Bin settings and preparing redshifts for plots
    Nbins  = 4
    scales = np.array([0.95,0.7,0.55,0.4])
    xtab = -1+1/scales

    smoothfac = 10
    yout = ytab[0]
    if xin > xtab[-1]:
       yout = ytab[-1]
    else:
       for ind in range(len(xtab)-1):
           if ind == 0:
              yout += (ytab[ind+1]-ytab[ind])/2 * (1+np.tanh( smoothfac*(xin-xtab[ind])/((xtab[ind])/2)  ) )
           else:
              yout += (ytab[ind+1]-ytab[ind])/2 * (1+np.tanh( smoothfac*(xin-xtab[ind])/((xtab[ind]-xtab[ind-1])/2)  ) )


    return yout


def lumdist(z,wpars,om,H0):

    clight = 299792.458

    zmin  = 0.
    zmax  = z
    zsamp = 1000
    dz    = (zmax-zmin)/zsamp
    zint  = np.linspace(zmin,zmax,zsamp)

    integrand = np.zeros(zsamp)
    for ind in range(zsamp):
        integrand[ind] = Eofz(zint[ind],wpars,om)**(-1.)

    dL = (clight/H0)*integrate.trapz(integrand, dx=dz)


    return dL

def Eofz(z,wpars,om):

    zmin  = 0.
    zmax  = z
    zsamp = 1000
    dz    = (zmax-zmin)/zsamp
    zint  = np.linspace(zmin,zmax,zsamp)

    integrand = np.zeros(zsamp)
    for ind in range(zsamp):
        integrand[ind] = 3.*(1+getw(wpars,zint[ind]))/(1+zint[ind])#Eofz(zint[ind],wpars,om)**(-1.)


    E = np.sqrt(om*(1+z)**3.+(1-om)*np.exp(integrate.trapz(integrand, dx=dz)))#(1+z)**(3.*(1+getw(wpars,z))))

    return E

def metal_xi(z):

    xi = 0.015*((1+z)**2.7)/(1+((1+z)/2.9)**5.6)

    return xi

def metal_psi(z,wpars,om,H0):

    intred      = np.linspace(z,10,1000)
    dz          = (10-z)/1000
    numerator   = np.zeros(len(intred))
    denominator = np.zeros(len(intred))

    for ind in range(len(intred)):
        numerator[ind]   = metal_xi(intred[ind])
        denominator[ind] = H0*Eofz(intred[ind],wpars,om)*(1+intred[ind])
    

    psi = integrate.trapz(numerator/denominator, dx=dz)

    return psi

def getsys(z,root,data,w,om,H0):
    
    if 'NOSys' in root:
       sys = 0.
    elif 'metalSys' in root:
       metal_R  = data.loc[data.parameter=='metal_R','mean'].values[0]
       metal_y  = data.loc[data.parameter=='metal_y','mean'].values[0]
       ombh2    = data.loc[data.parameter=='omegabh2','mean'].values[0]

       Gconst = 4.30091e-3
       Zsun   = 0.0134
       rhoc   = (3*H0**2.)/(8.*3.14159*Gconst)
       omegab = ombh2/(H0/100)**2.

       metal_rhostar = (1-metal_R)*metal_psi(z,w,om,H0)
       metal_Zb      = metal_y*(metal_rhostar/((omegab)*rhoc))*(3.0857e13/(3600*24*365.25))
       
       sys = -2.5*np.log10(1-0.18*(metal_Zb/Zsun)*(1-0.10*metal_Zb/Zsun))-0.191
    elif 'SFRSys' in root:
       Dgamma   = data.loc[data.parameter=='SFR_Dgamma','mean'].values[0]
       phi      = data.loc[data.parameter=='SFR_phi','mean'].values[0]        
       kappa    = data.loc[data.parameter=='SFR_kappa','mean'].values[0]
       sys      = Dgamma*(1+kappa*(1+z)**phi)**(-1.)
    elif 'phenoSys' in root:
       eps   = data.loc[data.parameter=='pheno_eps','mean'].values[0]
       delta = data.loc[data.parameter=='pheno_delta','mean'].values[0]
       sys   = eps*z**delta

    return sys


rootdir = 'output/'
bin_roots = ['SFRSys_wbinned_Planck_JLA_BAO','metalSys_wbinned_Planck_JLA_BAO','NOSys_wbinned_Planck_JLA_BAO']
w_roots = ['SFRSys_wconst_Planck_JLA_BAO','metalSys_wconst_Planck_JLA_BAO','NOSys_wconst_Planck_JLA_BAO']
lam_roots = ['SFRSys_LCDM_Planck_JLA_BAO','metalSys_LCDM_Planck_JLA_BAO']
cols  =['parameter','mean','sddev','lower1','upper1','limit1','lower2','upper2','limit2','lower3','upper3','limit3','latex','fake1','fake2']


colors = ['#8E001C','#FFB300','black']
labels = ['SFR', 'metallicity','No sys']
plotred = np.linspace(0.01,3,1000)


#computing mus

#1: baseline LCDM no sys

data     = pd.read_csv(rootdir+'NOSys_LCDM_Planck_JLA_BAO.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
wconst   = -1.
omegam   = data.loc[data.parameter=='omegam*','mean'].values[0]
H0       = data.loc[data.parameter=='H0*','mean'].values[0]
    #here sys pars

mu_base = np.empty(len(plotred))
for ind in range(len(plotred)):
        mu_base[ind] = 5*np.log(lumdist(plotred[ind],np.array([wconst]*4),omegam,H0))

print 'Finished?'
exit()

level = np.array([0]*len(plotred))


fig, axs = plt.subplots(3,1, figsize=(5, 6), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .5, wspace=.001)


axs = axs.ravel()

axs[0].set_title('w(z) reconstruction')


for case in range(len(bin_roots)):

    #Getting data from margestats
    data     = pd.read_csv(rootdir+bin_roots[case]+'.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
    wconst   = np.array([data.loc[data.parameter=='binw'+str(i+1),'mean'].values[0] for i in range(Nbins)]) 
    omegam   = data.loc[data.parameter=='omegam*','mean'].values[0]
    H0       = data.loc[data.parameter=='H0*','mean'].values[0]
    #here sys pars

    mu = np.empty(len(plotred))
    for ind in range(len(plotred)):
        mu[ind] = 5*np.log(lumdist(plotred[ind],np.array(wconst),omegam,H0))

    sys = np.empty(len(plotred))
    for ind in range(len(plotred)):
        sys[ind] = getsys(plotred[ind],w_roots[case],data,np.array([wconst]*4),omegam,H0)

    axs[0].plot(plotred,((mu+sys)-mu_base)/mu_base, color=colors[case], label=labels[case])

    print '{} done!'.format(bin_roots[case])


axs[0].plot(plotred,level, color='gray', ls='--')
axs[0].legend(loc='lower right')
axs[0].set_ylabel(r'$(\mu(z)-\mu^0(z))/\mu^0(z)$')
axs[0].set_xlabel(r'$z$')


axs[1].set_title('constant w')


for case in range(len(w_roots)):

    #Getting data from margestats
    data     = pd.read_csv(rootdir+w_roots[case]+'.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
    wconst   = data.loc[data.parameter=='binw1','mean'].values[0]
    omegam   = data.loc[data.parameter=='omegam*','mean'].values[0]
    H0       = data.loc[data.parameter=='H0*','mean'].values[0]
    #here sys pars

    mu = np.empty(len(plotred))
    for ind in range(len(plotred)):
        mu[ind] = 5*np.log(lumdist(plotred[ind],np.array([wconst]*4),omegam,H0))

    sys = np.empty(len(plotred))
    for ind in range(len(plotred)):
        sys[ind] = getsys(plotred[ind],w_roots[case],data,np.array([wconst]*4),omegam,H0)

    axs[1].plot(plotred,((mu+sys)-mu_base)/mu_base, color=colors[case], label=labels[case])
    print '{} done!'.format(w_roots[case])

axs[1].plot(plotred,level, color='gray', ls='--')
axs[1].legend(loc='lower right')
axs[1].set_ylabel(r'$(\mu(z)-\mu^0(z))/\mu^0(z)$')
axs[1].set_xlabel(r'$z$')


axs[2].set_title(r'$\Lambda$CDM')

for case in range(len(lam_roots)):

    #Getting data from margestats
    data     = pd.read_csv(rootdir+lam_roots[case]+'.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
    wconst   = -1. 
    omegam   = data.loc[data.parameter=='omegam*','mean'].values[0]
    H0       = data.loc[data.parameter=='H0*','mean'].values[0]
    #here sys pars

    mu = np.empty(len(plotred))
    for ind in range(len(plotred)):
        mu[ind] = 5*np.log(lumdist(plotred[ind],np.array([wconst]*4),omegam,H0))

    sys = np.empty(len(plotred))
    for ind in range(len(plotred)):
        sys[ind] = getsys(plotred[ind],lam_roots[case],data,np.array([wconst]*4),omegam,H0)

    axs[2].plot(plotred,((mu+sys)-mu_base)/mu_base, color=colors[case], label=labels[case])
    print '{} done!'.format(lam_roots[case])

axs[2].plot(plotred,level, color='gray', ls='--')
axs[2].legend(loc='lower right')
axs[2].set_ylabel(r'$(\mu(z)-\mu^0(z))/\mu^0(z)$')
axs[2].set_xlabel(r'$z$')

#plt.savefig('sysplot_fits.pdf')
plt.show()
