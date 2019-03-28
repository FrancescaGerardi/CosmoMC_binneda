#!/bin/env bash

python python/GetDist.py chains/NOSys_wbinned_Planck_Pantheon_BAO
python python/GetDist.py chains/SFRSys_wbinned_Planck_Pantheon_BAO
python python/GetDist.py chains/metalSys_wbinned_Planck_Pantheon_BAO
python python/GetDist.py chains/NOSys_wconst_Planck_Pantheon_BAO
python python/GetDist.py chains/SFRSys_wconst_Planck_Pantheon_BAO
python python/GetDist.py chains/metalSys_wconst_Planck_Pantheon_BAO
python python/GetDist.py chains/phenoSys_wbinned_Planck_Pantheon_BAO
python python/GetDist.py chains/NOSys_LCDM_Planck_Pantheon_BAO
python python/GetDist.py chains/phenoSys_wconst_Planck_Pantheon_BAO


