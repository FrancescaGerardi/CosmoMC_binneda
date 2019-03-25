import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'/data1/martinelli/Projects/MY_PROJECTS/SNsys/CosmoMC_binneda/chains',analysis_settings=analysis_settings)


roots = ['SFRSys_LCDM_Planck','metalSys_LCDM_Planck','NOSys_LCDM_Planck']
#roots = ['SFRSys_wconst_Planck']
params = [u'omegam',u'H0']
colors = ['#8E001C','#FFB300','navy']
labels = [ 'SFR sys', 'metallicity sys','No sys']
#labels = ['SFR sys']

param_3d = None
g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=[True,True,False], shaded=False)
g.export('results_plots/triplot_metalSFRnosys_Planck_LCDM.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_metalSFRnosys_Planck_LCDM.pdf')
