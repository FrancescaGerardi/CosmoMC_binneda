import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'/data1/martinelli/Projects/MY_PROJECTS/SNsys/CosmoMC_binneda/chains',analysis_settings=analysis_settings)


roots = ['NOSys_wconst','NOSys_wconst_Planck']
#roots = ['SFRSys_wconst_Planck']
params = [u'binw1',u'omegam',u'H0']
colors = ['#8E001C','#FFB300','navy','#8E001C','#FFB300','navy']
labels = [ 'SN', 'Planck+SN']
filling = [True, True, True]
#labels = ['SFR sys']

param_3d = None
g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=filling, shaded=False)
g.export('results_plots/triplot_nosys_wconst_SNvsPlanck.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_nosys_wconst_SNvsPlanck.pdf')
