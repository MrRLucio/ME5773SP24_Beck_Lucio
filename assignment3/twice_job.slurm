#!/bin/bash
#SBATCH -J twice_job
#SBATCH -p amdonly
#SBATCH -o outfile_run5__amdonly.txt
#SBATCH -N 1
#SBATCH -n 4 
#SBATCH -c 8
#SBATCH -t 00:05:00

startT=`date +%s`
#echo $startT

srun --exclusive -J five    -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 5 &
srun --exclusive -J two     -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 2 &
srun --exclusive -J seven   -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 7 &
srun --exclusive -J six     -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 6 &
srun --exclusive -J one     -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 1 &
srun --exclusive -J three   -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 3 

wait

endT=`date +%s`
#echo $endT

DeltaT=$((endT-startT))
#echo $DeltaT

echo "Total execution time was $DeltaT seconds"

##sacct -j 349971 --format=JobID,State,Elapsed,Nodelist,NCPUS

