#!/bin/bash
#
#SBATCH -J int_study
#SBATCH -o integral_out.txt
#SBATCH -e integral_error.txt
#SBATCH -p compute1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 80
#SBATCH -t 00:05:00

module load anaconda3

conda activate envTeam1

for ((i = 1; i <= 8; i = i*2))
do
    export OMP_NUM_THREADS=$i
    export NUMEXPR_NUM_THREADS=$i
    python3 integral.py
    #echo $i
   
done
