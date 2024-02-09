#!/bin/bash
#SBATCH -J twice_job
#SBATCH -p compute1
#SBATCH -o outfile_run1.txt
#SBATCH -N 1
#SBATCH -n 1 
#SBATCH -c 80
#SBATCH -t 00:05:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user william.beck@my.utsa.edu

startT=`date +%S`

srun --exclusive -J five    -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 5 &
srun --exclusive -J two     -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 2 &
srun --exclusive -J seven   -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 7 &
srun --exclusive -J six     -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 6 &
srun --exclusive -J one     -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 1 &
srun --exclusive -J three   -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 3 

wait

endT=`date +%S`

DeltaT=$((endT-startT))

echo "Total execution time was $DeltaT seconds"

##sacct -j 349971 --format=JobID,State,Elapsed,Nodelist,NCPUS

