import sys, platform, os
import numpy as np
import matplotlib
matplotlib.use('pdf')
from matplotlib import pyplot as plt
import pandas as pd





rootdir = 'output/'
roots   = ['NOSys','SFRSys','metalSys','phenoSys']
DEtype  = ['wbinned','wconst']#,'LCDM']
DEtitle = ['w(z) reconstruction','constant w',r'$\Lambda$CDM'] 
cols    = ['parameter','mean','sddev','lower1','upper1','limit1','lower2','upper2','limit2','lower3','upper3','limit3','latex','fake1','fake2']

#setup for plot
colors = ['black','#8E001C','#FFB300','navy']
labels = ['No systematics', 'SFR', 'metallicity', 'phenomenological']


fig, axs = plt.subplots(len(DEtype),1, figsize=(5, 6), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .5, wspace=.001)

HST_low = 74.03 - 1.42
HST_high= 74.03 + 1.42

axs = axs.ravel()

for DE in range(len(DEtype)):

    axs[DE].set_title(DEtitle[DE])

    for case in range(len(roots)):

       #Getting data from margestats
       data   = pd.read_csv(rootdir+roots[case]+'_'+DEtype[DE]+'_Planck_JLA_BAO.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
       mean   = data.loc[data.parameter=='H0*','mean'].values[0]
       sigma  = data.loc[data.parameter=='H0*','sddev'].values[0]
       lower1 = data.loc[data.parameter=='H0*','lower1'].values[0]
       upper1 = data.loc[data.parameter=='H0*','upper1'].values[0]
       lower2 = data.loc[data.parameter=='H0*','lower2'].values[0]
       upper2 = data.loc[data.parameter=='H0*','upper2'].values[0]
       error  = [[mean-lower1,upper1-mean]]


       axs[DE].errorbar(mean,case+1,xerr=np.array(error).T, fmt='o', color=colors[case], ecolor=colors[case])

    axs[DE].axvspan(HST_low, HST_high, alpha=0.5, color='gray')
    axs[DE].legend(loc='lower left')
    axs[DE].set_ylim(0,6)
    axs[DE].set_xlim(64,76)
    axs[DE].set_ylabel(r'')
    axs[DE].set_xlabel(r'$H_0$')
    axs[DE].set_yticks([1,2,3,4])
    axs[DE].set_yticklabels(labels)
plt.savefig('results_plots/errorbarH0_JLA.pdf', bbox_inches='tight')
plt.savefig('/data1/martinelli/Dropbox/Projects/SNsys/errorbarH0_JLA.pdf', bbox_inches='tight')
