import getdist.plots as gplot
import os
import matplotlib.pyplot as plt

analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['./fakechains/metalSys_wbinned_Planck_Pantheon','metalSys_wbinned_Planck_Pantheon']#,'metalSys_wbinned_Planck_Pantheon_BAO_free']
params = [u'H0',u'omegam','binw1','binw2','binw3','binw4','metal_y','metal_R']
colors = ['#8E001C','#FFB300','navy']
labels = [ r'new', r'old',r'old free']
fillcont = [True,True,True,False,False,False]
param_3d = None

g.settings.axes_fontsize = 20
g.settings.lab_fontsize = 20
g.settings.legend_fontsize = 20
g.settings.x_label_rotation=45

g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=fillcont, shaded=False,axes_fontsize=32)
g.export('results_plots/triplot_metallicity_comparison_Pantheon.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/testmetal_wbinned.pdf')
