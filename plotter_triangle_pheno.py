import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'/data1/martinelli/Projects/MY_PROJECTS/SNsys/CosmoMC_binneda/chains',analysis_settings=analysis_settings)

roots = ['AllSys_wconst','phenoSys_wconst','NOSys_wconst']
params = [u'binw1',u'omegam',u'pheno_eps',u'pheno_delta']
colors = ['#8E001C','#FFB300','navy']
labels = [ 'All sys', 'phenomenological sys','No sys']

param_3d = None
g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=[True,True,False], shaded=False)
g.export('results_plots/triplot_pheno.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_pheno.pdf')
