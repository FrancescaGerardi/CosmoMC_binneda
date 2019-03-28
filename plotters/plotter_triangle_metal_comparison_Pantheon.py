import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'/data1/martinelli/Projects/MY_PROJECTS/SNsys/CosmoMC_binneda/chains',analysis_settings=analysis_settings)


roots = ['metalSys_wbinned_Planck_Pantheon_BAO','metalSys_wconst_Planck_Pantheon_BAO','metalSys_LCDM_Planck_Pantheon_BAO']
params = [u'H0',u'omegam','metal_y','metal_R']
colors = ['#8E001C','#FFB300','navy']
labels = [ r'$w(z)$CDM', r'$w$CDM',r'$\Lambda$CDM']
fillcont = [True,True,True,False,False,False]
param_3d = None

g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=fillcont, shaded=False)
g.export('results_plots/triplot_metallicity_comparison_Pantheon.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_metallicity_comparison_Pantheon.pdf')
