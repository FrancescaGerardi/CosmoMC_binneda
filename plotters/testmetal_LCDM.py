import getdist.plots as gplot
import os
import matplotlib.pyplot as plt


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['./fakechains/metalSys_LCDM_Planck_Pantheon_BAO','metalSys_LCDM_Planck_Pantheon_BAO']#,'metalSys_wbinned_Planck_Pantheon_BAO_free']
params = [u'H0',u'omegam','metal_y','metal_R']
colors = ['#8E001C','#FFB300','navy']
labels = [ r'old', r'new']
fillcont = [True,True,True,False,False,False]
param_3d = None

g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=fillcont, shaded=False)
plt.rcParams["axes.labelsize"] = 22
g.export('results_plots/triplot_metallicity_comparison_Pantheon.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/testmetal_LCDM.pdf')
