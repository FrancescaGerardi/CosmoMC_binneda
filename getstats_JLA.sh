#!/bin/env bash

python python/GetDist.py chains/NOSys_wbinned_Planck_JLA_BAO
python python/GetDist.py chains/SFRSys_wbinned_Planck_JLA_BAO
python python/GetDist.py chains/metalSys_wbinned_Planck_JLA_BAO
python python/GetDist.py chains/metalSys_wbinned_Planck_JLA_BAO_free
python python/GetDist.py chains/NOSys_wconst_Planck_JLA_BAO
python python/GetDist.py chains/SFRSys_wconst_Planck_JLA_BAO
python python/GetDist.py chains/metalSys_wconst_Planck_JLA_BAO
python python/GetDist.py chains/NOSys_LCDM_Planck_JLA_BAO
python python/GetDist.py chains/SFRSys_LCDM_Planck_JLA_BAO
python python/GetDist.py chains/metalSys_LCDM_Planck_JLA_BAO

python python/GetDist.py chains/NOSys_LCDM_Planck_JLA
python python/GetDist.py chains/NOSys_wconst_Planck_JLA
python python/GetDist.py chains/NOSys_wbinned_Planck_JLA

python python/GetDist.py chains/SFRSys_LCDM_Planck_JLA
python python/GetDist.py chains/SFRSys_wconst_Planck_JLA
python python/GetDist.py chains/SFRSys_wbinned_Planck_JLA

python python/GetDist.py chains/metalSys_LCDM_Planck_JLA
python python/GetDist.py chains/metalSys_wconst_Planck_JLA
python python/GetDist.py chains/metalSys_wbinned_Planck_JLA



python python/GetDist.py chains/LCDM_Planckonly
python python/GetDist.py chains/wconst_Planckonly
python python/GetDist.py chains/wbinned_Planckonly

