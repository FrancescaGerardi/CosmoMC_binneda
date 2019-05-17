import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['./fakechains/metalSys_wconst_Planck_Pantheon_BAO','metalSys_wconst_Planck_Pantheon_BAO']#,'metalSys_wbinned_Planck_Pantheon_BAO_free']
params = [u'H0',u'omegam','binw1','metal_y','metal_R']
colors = ['#8E001C','#FFB300','navy']
labels = [ r'old', r'new',r'old free']
fillcont = [True,True,True,False,False,False]
param_3d = None

g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=fillcont, shaded=False)
g.export('results_plots/triplot_metallicity_comparison_Pantheon.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/testmetal_wconst.pdf')
