import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['NOSys_wbinned_Planck_Pantheon_BAO','NOSys_wconst_Planck_Pantheon_BAO','NOSys_LCDM_Planck_Pantheon_BAO']
params = [u'H0',u'omegam']
colors = ['#8E001C','#FFB300','navy']
labels = [ r'$w(z)$CDM', r'$w$CDM',r'$\Lambda$CDM']
fillcont = [True,True,True,False,False,False]
param_3d = None

g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=fillcont, shaded=False)
g.export('results_plots/triplot_NOsys_comparison_Pantheon.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_NOsys_comparison_Pantheon.pdf')
