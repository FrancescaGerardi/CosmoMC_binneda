import sys, platform, os
import numpy as np
import matplotlib
matplotlib.use('pdf')
from matplotlib import pyplot as plt
import pandas as pd
from argparse import ArgumentParser
import ConfigParser

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

parser = ArgumentParser()
parser.add_argument("-r", "--range", action="store", dest="endred", default=5,
                  help="Ending redshift of plotting range")
parser.add_argument("-d", "--data", action="store", type=str, dest="datapath", default='dataframes/',
                  help="path to margestats files (adjusted)")
parser.add_argument("-b","--bounds", action="store", type=int, dest="bound", default=2,
                  help="choose if to plot 1 or 2 sigma bounds on error bars")
args           = parser.parse_args()
endred         = args.endred
datapath       = args.datapath
sigma          = args.bound


bound = str(sigma)+'sigma'

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

plotred = np.logspace(np.log10(0.01),np.log10(float(endred)),1000)#np.arange(0,2,0.01)

LCDM = np.array([-1]*len(plotred))

eps = 0.01*binwidth[aind]

#NO SYS
data  = pd.read_csv(datapath+'/NOSys_wbinned_Planck.txt',skiprows=0,sep='\s+',usecols=['parameter', 'mean','sddev','lower1','upper1','lower2','upper2'])
mean_nosys = np.array([data.loc[data.parameter=='binw'+str(i+1),'mean'].values[0] for i in range(4)])
sigma_nosys = np.array([data.loc[data.parameter=='binw'+str(i+1),'sddev'].values[0] for i in range(4)])
if bound == '1sigma':
   lower_nosys= np.array([data.loc[data.parameter=='binw'+str(i+1),'lower1'].values[0] for i in range(4)])
   upper_nosys= np.array([data.loc[data.parameter=='binw'+str(i+1),'upper1'].values[0] for i in range(4)])
elif bound == '2sigma':
   lower_nosys= np.array([data.loc[data.parameter=='binw'+str(i+1),'lower2'].values[0] for i in range(4)])
   upper_nosys= np.array([data.loc[data.parameter=='binw'+str(i+1),'upper2'].values[0] for i in range(4)])
else:
   print 'WTF?'
   exit()

int_nosys = np.empty(len(plotred))
for ind in range(len(plotred)):
    int_nosys[ind] = interpolation(redshifts,mean_nosys,plotred[ind])


#SFR SYS
data  = pd.read_csv(datapath+'/SFRSys_wbinned_Planck.txt',skiprows=0,sep='\s+',usecols=['parameter', 'mean','sddev','lower1','upper1','lower2','upper2'])
mean_SFRsys = np.array([data.loc[data.parameter=='binw'+str(i+1),'mean'].values[0] for i in range(4)])
sigma_SFRsys = np.array([data.loc[data.parameter=='binw'+str(i+1),'sddev'].values[0] for i in range(4)])
if bound == '1sigma':
   lower_SFRsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'lower1'].values[0] for i in range(4)])
   upper_SFRsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'upper1'].values[0] for i in range(4)])
elif bound == '2sigma':
   lower_SFRsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'lower2'].values[0] for i in range(4)])
   upper_SFRsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'upper2'].values[0] for i in range(4)])
else:
   print 'WTF?'
   exit()

int_SFRsys = np.empty(len(plotred))
for ind in range(len(plotred)):
    int_SFRsys[ind] = interpolation(redshifts,mean_SFRsys,plotred[ind])


#METAL SYS
data  = pd.read_csv(datapath+'/metalSys_wbinned_Planck.txt',skiprows=0,sep='\s+',usecols=['parameter', 'mean','sddev','lower1','upper1','lower2','upper2'])
mean_metalsys = np.array([data.loc[data.parameter=='binw'+str(i+1),'mean'].values[0] for i in range(4)])
sigma_metalsys = np.array([data.loc[data.parameter=='binw'+str(i+1),'sddev'].values[0] for i in range(4)])
if bound == '1sigma':
   lower_metalsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'lower1'].values[0] for i in range(4)])
   upper_metalsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'upper1'].values[0] for i in range(4)])
elif bound == '2sigma':
   lower_metalsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'lower2'].values[0] for i in range(4)])
   upper_metalsys= np.array([data.loc[data.parameter=='binw'+str(i+1),'upper2'].values[0] for i in range(4)])
else:
   print 'WTF?'
   exit()

int_metalsys = np.empty(len(plotred))
for ind in range(len(plotred)):
    int_metalsys[ind] = interpolation(redshifts,mean_metalsys,plotred[ind])


plt.figure()
plt.errorbar(mean_redshifts,mean_nosys,yerr=[mean_nosys-lower_nosys,upper_nosys-mean_nosys], fmt='o', color='navy', ecolor='navy')
plt.plot(plotred,int_nosys, color='navy', label='Planck+SN NO sys')
plt.errorbar(mean_redshifts+eps,mean_SFRsys,yerr=[mean_SFRsys-lower_SFRsys,upper_SFRsys-mean_SFRsys], fmt='o',ecolor='#8E001C',color='#8E001C')
plt.plot(plotred,int_SFRsys, color='#8E001C', label='Planck+SN SFR sys')
plt.errorbar(mean_redshifts-eps,mean_metalsys,yerr=[mean_metalsys-lower_metalsys,upper_metalsys-mean_metalsys], fmt='o',ecolor='#FFB300',color='#FFB300')
plt.plot(plotred,int_metalsys, color='#FFB300', label='Planck+SN metal sys')
plt.plot(plotred,LCDM, color='black', label=r'$\Lambda$CDM')
plt.xscale('log')
plt.ylim(-5,0)
plt.ylabel(r'$w(z)$')
plt.xlabel(r'$z$')
plt.legend(loc='lower left')
#plt.show()
plt.savefig('results_plots/wreconstruction.pdf')
plt.savefig('/data1/martinelli/Dropbox/Projects/SNsys/wreconstruction.pdf')


