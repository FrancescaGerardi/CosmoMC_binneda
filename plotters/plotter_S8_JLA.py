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


kids_low = [(0.745-0.039)*np.sqrt(0.3), , (0.745-0.039)*np.sqrt(0.3)]
kids_high= [(0.745+0.039)*np.sqrt(0.3), , (0.745-0.039)*np.sqrt(0.3)]
kidsS8    = [0.745*np.sqrt(0.3), , 0.745*np.sqrt(0.3)]
kidssigma = [0.039*np.sqrt(0.3), ,0.039*np.sqrt(0.3)]
axs = axs.ravel()

for DE in range(len(DEtype)):

    axs[DE].set_title(DEtitle[DE])

    for case in range(len(roots)):

       #Getting data from margestats
       data   = pd.read_csv(rootdir+roots[case]+'_'+DEtype[DE]+'_Planck_JLA_BAO.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
       mean   = data.loc[data.parameter=='s8omegamp5*','mean'].values[0]
       sigma  = data.loc[data.parameter=='s8omegamp5*','sddev'].values[0]
       lower1 = data.loc[data.parameter=='s8omegamp5*','lower1'].values[0]
       upper1 = data.loc[data.parameter=='s8omegamp5*','upper1'].values[0]
       lower2 = data.loc[data.parameter=='s8omegamp5*','lower2'].values[0]
       upper2 = data.loc[data.parameter=='s8omegamp5*','upper2'].values[0]
       error  = [[mean-lower1,upper1-mean]]

       print 'Tension for case {} is {}'.format(roots[case]+'_'+DEtype[DE]+'_Planck_JLA_BAO.margestats', abs(kidsS8[DE]-mean)/np.sqrt(kidssigma[DE]**2.+sigma**2.))


       axs[DE].errorbar(mean,case+1.2,xerr=np.array(error).T, fmt='o', markersize='3', color=colors[case], ecolor=colors[case])

       #Getting data from margestats
       data   = pd.read_csv(rootdir+roots[case]+'_'+DEtype[DE]+'_Planck_JLA.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
       mean   = data.loc[data.parameter=='s8omegamp5*','mean'].values[0]
       sigma  = data.loc[data.parameter=='s8omegamp5*','sddev'].values[0]
       lower1 = data.loc[data.parameter=='s8omegamp5*','lower1'].values[0]
       upper1 = data.loc[data.parameter=='s8omegamp5*','upper1'].values[0]
       lower2 = data.loc[data.parameter=='s8omegamp5*','lower2'].values[0]
       upper2 = data.loc[data.parameter=='s8omegamp5*','upper2'].values[0]
       error  = [[mean-lower1,upper1-mean]]

       print 'Tension for case {} is {}'.format(roots[case]+'_'+DEtype[DE]+'_Planck_JLA.margestats', abs(kidsS8[DE]-mean)/np.sqrt(kidssigma[DE]**2.+sigma**2.))

       test=axs[DE].errorbar(mean,case+0.8,xerr=np.array(error).T, fmt='o', markersize='3', color=colors[case], ecolor=colors[case])
       test[-1][0].set_linestyle('--')



    data   = pd.read_csv(rootdir+DEtype[DE]+'_Planckonly.margestats',skiprows=3,sep='\s+',names=cols,usecols=cols[:-2])
    mean   = data.loc[data.parameter=='s8omegamp5*','mean'].values[0]
    sigma  = data.loc[data.parameter=='s8omegamp5*','sddev'].values[0]
    lower1 = data.loc[data.parameter=='s8omegamp5*','lower1'].values[0]
    upper1 = data.loc[data.parameter=='s8omegamp5*','upper1'].values[0]
    lower2 = data.loc[data.parameter=='s8omegamp5*','lower2'].values[0]
    upper2 = data.loc[data.parameter=='s8omegamp5*','upper2'].values[0]
    error  = [[mean-lower1,upper1-mean]]


    print 'Tension for case {} is {}'.format(roots[case]+'_'+DEtype[DE]+'_Planckonly.margestats', abs(kidsS8[DE]-mean)/np.sqrt(kidssigma[DE]**2.+sigma**2.))

    axs[DE].errorbar(mean,4,xerr=np.array(error).T, fmt='o', markersize='3', color='green', ecolor='green')



    axs[DE].axvspan(kids_low[DE], kids_high[DE], alpha=0.5, color='gray')
    #axs[DE].legend(loc='lower left')
    axs[DE].set_ylim(0,5)
    #axs[DE].set_xlim(64,80)
    axs[DE].set_ylabel(r'')
    axs[DE].set_xlabel(r'$\sigma_8\sqrt{\Omega_m}$')
    axs[DE].set_yticks([1,2,3,4])#,5])
    axs[DE].set_yticklabels(labels)
    axs[DE].yaxis.tick_right()


    #Adding the Planck only case (could be done better)
    


plt.savefig('results_plots/errorbarS8_JLA.pdf', bbox_inches='tight')
plt.savefig('/data1/martinelli/Dropbox/Projects/SNsys/errorbarS8_JLA.pdf', bbox_inches='tight')
