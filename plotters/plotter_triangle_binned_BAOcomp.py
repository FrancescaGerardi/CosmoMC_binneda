import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['wbinned_Planckonly','SFRSys_wbinned_Planck_JLA','SFRSys_wbinned_Planck_JLA_BAO']
#roots = ['SFRSys_wconst_Planck']
params = [u'binw1',u'binw2',u'binw3',u'binw4',u'omegam',u'H0']
colors = ['black','#8E001C','#FFB300','navy','black']
labels = [ 'Planck','Planck+JLA', 'Planck+JLA+BAO', 'phenomenological', 'No sys']
#labels = ['SFR sys']

param_3d = None
g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=[False,True,True,True], shaded=False)
g.export('results_plots/triplot_binned_BAO_comparison.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_binned_BAO_comparison.pdf')
