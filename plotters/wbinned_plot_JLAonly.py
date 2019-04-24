import sys, platform, os
import numpy as np
import matplotlib
matplotlib.use('pdf')
from matplotlib import pyplot as plt
import pandas as pd



#smoothed spline interpolator
def interpolation(xtab,ytab,xin):

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


#Bin settings and preparing redshifts for plots
Nbins  = 4
scales = np.array([0.95,0.7,0.55,0.4])
redshifts = -1+1/scales
mean_redshifts = np.empty(len(scales))
binwidth = np.empty(len(scales))

for aind in range(len(scales)):
    if aind == 0:
       mean_redshifts[aind] = 0.5*(redshifts[aind])
       binwidth[aind] = redshifts[aind]
    else:
       mean_redshifts[aind] = 0.5*(redshifts[aind]+redshifts[aind-1])
       binwidth[aind] = redshifts[aind]-redshifts[aind-1]

endred  = 5.
plotred = np.logspace(np.log10(0.01),np.log10(float(endred)),1000)#np.arange(0,2,0.01)
eps = 0.01*binwidth #this is only to separate the redshifts a bit for the different cases



rootdir = 'output/'
roots = ['NOSys_wbinned_Planck_JLA','SFRSys_wbinned_Planck_JLA','metalSys_wbinned_Planck_JLA']#,'phenoSys_wbinned_Planck_JLA_BAO']#,'wbinned_Planckonly']
cols  =['parameter','mean','sddev','lower1','upper1','limit1','lower2','upper2','limit2','lower3','upper3','limit3','latex','fake1','fake2']

#setup for plot
colors = ['black','#8E001C','#FFB300','navy','green']
labels = ['No systematics', 'SFR', 'metallicity', 'phenomenological','Planck only']
endred  = 2.
plotred = np.logspace(np.log10(0.01),np.log10(float(endred)),1000)
eps = 0.1*binwidth #this is only to separate the redshifts a bit for the different cases
plt.figure()
plt.title('Planck+JLA')
plt.ylim(-3,0)
plt.ylabel(r'$w(z)$')
plt.xlabel(r'$z$')
plt.xscale('log')
LCDM = np.array([-1]*len(plotred))
plt.plot(plotred,LCDM, color='gray', ls='--', label=r'$\Lambda$CDM')

for case in range(len(roots)):

    #Getting data from margestats
    data   = pd.read_csv(rootdir+roots[case]+'.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
    mean   = np.array([data.loc[data.parameter=='binw'+str(i+1),'mean'].values[0] for i in range(Nbins)])
    sigma  = np.array([data.loc[data.parameter=='binw'+str(i+1),'sddev'].values[0] for i in range(Nbins)])
    lower1 = np.array([data.loc[data.parameter=='binw'+str(i+1),'lower1'].values[0] for i in range(Nbins)])
    upper1 = np.array([data.loc[data.parameter=='binw'+str(i+1),'upper1'].values[0] for i in range(Nbins)])
    lower2 = np.array([data.loc[data.parameter=='binw'+str(i+1),'lower2'].values[0] for i in range(Nbins)])
    upper2 = np.array([data.loc[data.parameter=='binw'+str(i+1),'upper2'].values[0] for i in range(Nbins)])

    interp = np.empty(len(plotred))
    for ind in range(len(plotred)):
        interp[ind] = interpolation(redshifts,mean,plotred[ind])

    shift = ((-1)**(case+1))*(round((1+case)/2))*eps
    plt.errorbar(mean_redshifts+shift,mean,yerr=[mean-lower1,upper1-mean], fmt='o', color=colors[case], ecolor=colors[case])
    plt.plot(plotred,interp, color=colors[case], label=labels[case])

plt.legend(loc='lower left')
plt.savefig('results_plots/wreconstruction_JLAonly.pdf')
plt.savefig('/data1/martinelli/Dropbox/Projects/SNsys/wreconstruction_JLAonly.pdf')
