import getdist.plots as gplot
import os


analysis_settings = {'ignore_rows': u'0.3'}
g=gplot.getSubplotPlotter(chain_dir=r'./chains',analysis_settings=analysis_settings)


#roots = ['SFRSys_LCDM_Planck_Pantheon_BAO','metalSys_LCDM_Planck_Pantheon_BAO','phenoSys_LCDM_Planck_Pantheon_BAO','NOSys_LCDM_Planck_Pantheon_BAO']
roots = ['metalSys_LCDM_Planck_Pantheon_BAO','NOSys_LCDM_Planck_Pantheon_BAO']
#roots = ['SFRSys_wconst_Planck']
#params = [u'binw1',u'binw2',u'binw3',u'binw4',u'omegam',u'H0']
params = [u'omegam',u'H0']
colors = ['#8E001C','#FFB300','navy','black']
#labels = [ 'SFR sys', 'metallicity sys','No sys']
labels = ['metallicity','NO sys']

#g.settings.axes_fontsize = 20
#g.settings.lab_fontsize = 20
#g.settings.legend_fontsize = 20
#g.settings.x_label_rotation=45

param_3d = None
g.triangle_plot(roots, params, contour_colors=colors, legend_colors=colors, legend_labels=labels, plot_3d_with_param=param_3d, filled=[True,True,True,False], shaded=False)
g.export('results_plots/triplot_Planck_Pantheon_BAO_LCDM.pdf')
g.export('/data1/martinelli/Dropbox/Projects/SNsys/triplot_Planck_Pantheon_BAO_LCDM.pdf')
