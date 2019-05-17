#!/bin/env bash


export timestamp=$(date +%s)

#module unload mpi
#module load openmpi-slurm
#module load gcc/5.4



make clean
make delete
make

ulimit -s unlimited

srun -n 4 ./cosmomc_$timestamp parameter_files/JLA/params_metalSys_wbinned_Planck_BAO.ini > metal.out &
