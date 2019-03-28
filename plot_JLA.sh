#!/bin/env bash

python plotters/plotter_triangle_metal_comparison_JLA.py  
python plotters/plotter_triangle_SFR_comparison_JLA.py   
python plotters/plotter_triangle_NOsys_comparison_JLA.py  
python plotters/plotter_triangle_pheno_comparison_JLA.py

#python plotters/plotter_triangle_Planck_LCDM_JLA.py    
python plotters/plotter_triangle_Planck_wconst_JLA.py  
python plotters/plotter_triangle_Planck_binned_JLA.py

python plotters/wbinned_plot_JLA.py
python plotters/plotter_H0_JLA.py
