import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


roots = ['NOSys_wbinned_Planck_JLA_BAO','NOSys_wconst_Planck_JLA_BAO','NOSys_LCDM_Planck_JLA_BAO']
params = [u'H0',u'omegam']
colors = ['#8E001C','#FFB300','navy']
labels = [ r'$w(z)$CDM', r'$w$CDM',r'$\Lambda$CDM']
fillcont = [True,True,True,False,False,False]
param_3d = None

#g.settings.axes_fontsize = 20
#g.settings.lab_fontsize = 20
#g.settings.legend_fontsize = 20
#g.settings.x_label_rotation=45
#g.settings.set_yticks([0.26,0.28,0.30,0.32,0.34])#,5])

g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=fillcont, shaded=False,lims=[65,75,0.25,0.35])
g.export('results_plots/triplot_NOsys_comparison_JLA.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_NOsys_comparison_JLA.pdf')
