import sys, platform, os
import numpy as np
import matplotlib
matplotlib.use('pdf')
from matplotlib import pyplot as plt
import pandas as pd





rootdir = 'output/'
roots   = ['NOSys','SFRSys','metalSys']#,'phenoSys']
DEtype  = ['wbinned','wconst','LCDM']
DEtitle = ['w(z) reconstruction','constant w',r'$\Lambda$CDM'] 
cols    = ['parameter','mean','sddev','lower1','upper1','limit1','lower2','upper2','limit2','lower3','upper3','limit3','latex','fake1','fake2']

#setup for plot
colors = ['black','#8E001C','#FFB300','navy']
labels = ['No systematics', 'SFR', 'metallicity', 'Planck only']


fig, axs = plt.subplots(len(DEtype),1, figsize=(5, 6), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .8, wspace=.001)

HST_low = 74.03 - 1.42
HST_high= 74.03 + 1.42
sigmaHST = 1.42
HST = 74.03
axs = axs.ravel()

for DE in range(len(DEtype)):

    axs[DE].set_title(DEtitle[DE])

    for case in range(len(roots)):
       print 'Doing case {} {}'.format(DEtype[DE],roots[case])

       #Getting data from margestats
       data   = pd.read_csv(rootdir+roots[case]+'_'+DEtype[DE]+'_Planck_JLA_BAO.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
       mean   = data.loc[data.parameter=='H0*','mean'].values[0]
       sigma  = data.loc[data.parameter=='H0*','sddev'].values[0]
       lower1 = data.loc[data.parameter=='H0*','lower1'].values[0]
       upper1 = data.loc[data.parameter=='H0*','upper1'].values[0]
       lower2 = data.loc[data.parameter=='H0*','lower2'].values[0]
       upper2 = data.loc[data.parameter=='H0*','upper2'].values[0]
       error  = [[mean-lower1,upper1-mean]]

       print 'Tension for case {} is {}'.format(roots[case]+'_'+DEtype[DE]+'_Planck_JLA_BAO.margestats', abs(HST-mean)/np.sqrt(sigmaHST**2.+sigma**2.))

       axs[DE].errorbar(mean,case+1.2,xerr=np.array(error).T, fmt='o', markersize='3', color=colors[case], ecolor=colors[case])

       #Getting data from margestats
       data   = pd.read_csv(rootdir+roots[case]+'_'+DEtype[DE]+'_Planck_JLA.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
       mean   = data.loc[data.parameter=='H0*','mean'].values[0]
       sigma  = data.loc[data.parameter=='H0*','sddev'].values[0]
       lower1 = data.loc[data.parameter=='H0*','lower1'].values[0]
       upper1 = data.loc[data.parameter=='H0*','upper1'].values[0]
       lower2 = data.loc[data.parameter=='H0*','lower2'].values[0]
       upper2 = data.loc[data.parameter=='H0*','upper2'].values[0]
       error  = [[mean-lower1,upper1-mean]]

       print 'Tension for case {} is {}'.format(roots[case]+'_'+DEtype[DE]+'_Planck_JLA.margestats', abs(HST-mean)/np.sqrt(sigmaHST**2.+sigma**2.))

       test=axs[DE].errorbar(mean,case+0.8,xerr=np.array(error).T, fmt='o', markersize='3', color=colors[case], ecolor=colors[case])
       test[-1][0].set_linestyle('--')


    data   = pd.read_csv(rootdir+DEtype[DE]+'_Planckonly.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
    mean   = data.loc[data.parameter=='H0*','mean'].values[0]
    sigma  = data.loc[data.parameter=='H0*','sddev'].values[0]
    lower1 = data.loc[data.parameter=='H0*','lower1'].values[0]
    upper1 = data.loc[data.parameter=='H0*','upper1'].values[0]
    lower2 = data.loc[data.parameter=='H0*','lower2'].values[0]
    upper2 = data.loc[data.parameter=='H0*','upper2'].values[0]
    error  = [[mean-lower1,upper1-mean]]


    axs[DE].errorbar(mean,4,xerr=np.array(error).T, fmt='o', markersize='3', color='green', ecolor='green')

    print 'Tension for case {} is {}'.format(roots[case]+'_'+DEtype[DE]+'_Planckonly', abs(HST-mean)/np.sqrt(sigmaHST**2.+sigma**2.))

    axs[DE].axvspan(HST_low, HST_high, alpha=0.5, color='gray')
    #axs[DE].legend(loc='lower left')
    axs[DE].set_ylim(0,5)
    axs[DE].set_xlim(64,90)
    axs[DE].set_ylabel(r'')
    axs[DE].set_xlabel(r'$H_0$')
    axs[DE].set_yticks([1,2,3,4])#,5])
    axs[DE].set_yticklabels(labels)


    #Adding the Planck only case (could be done better)
    


plt.savefig('results_plots/errorbarH0_JLA.pdf', bbox_inches='tight')
plt.savefig('/data1/martinelli/Dropbox/Projects/SNsys/errorbarH0_JLA.pdf', bbox_inches='tight')
