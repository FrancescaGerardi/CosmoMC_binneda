import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['SFRSys_wconst_Planck_JLA_BAO','metalSys_wconst_Planck_JLA_BAO','phenoSys_wconst_Planck_JLA_BAO','NOSys_wconst_Planck_JLA_BAO']
#roots = ['SFRSys_wconst_Planck']
params = [u'binw1',u'omegam',u'H0']
colors = ['#8E001C','#FFB300','navy','black']
labels = [ 'SFR', 'metallicity', 'phenomenological', 'No sys']
#labels = ['SFR sys']

param_3d = None
g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=[True,True,True,False], shaded=False)
g.export('results_plots/triplot_Planck_JLA_BAO_wconst.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_Planck_JLA_BAO_wconst.pdf')
