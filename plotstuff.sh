#!/bin/env bash

python plotter_triangle_metal_comparison.py  
python plotter_triangle_Planck_binned.py  
python plotter_triangle_SFR_comparison.py   
#python plotter_triangle_SNvsPK_SFRsys.py
python plotter_triangle_NOsys_comparison.py  
python plotter_triangle_Planck_LCDM.py    
#python plotter_triangle_SNvsPK_metalsys.py
python plotter_triangle_Planck_wconst.py  
#python plotter_triangle_SNvsPK_nosys.py 

python wbinned_plot.py

top
