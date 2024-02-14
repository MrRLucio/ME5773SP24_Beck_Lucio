#!/bin/bash
#
#SBATCH -J linalg_tests
#SBATCH -o linalgOut.txt
#SBATCH -e linalgError.txt
#SBATCH -p compute1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 80
#SBATCH -t 00:05:00

module load anaconda3

conda activate environment.yml

export MKL_NUM_THREADS=1

python3 linalg.py

export MKL_NUM_THREADS=2

python3 linalg.py

export MKL_NUM_THREADS=4

python3 linalg.py

export MKL_NUM_THREADS=8

python3 linalg.py

export MKL_NUM_THREADS=16

python3 linalg.py

export MKL_NUM_THREADS=20

python3 linalg.py

export MKL_NUM_THREADS=40

python3 linalg.py


