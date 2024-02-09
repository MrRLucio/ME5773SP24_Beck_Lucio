#!/bin/bash

N=$1
K=$2

#######Force user to enter filenname.sh <N> <K> or return error message
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <N> <K>"
	exit 1
fi

kfib(){

local  N=$1
local  K=$2

#declare -a array  makes an indexed array
#declare -i array  make the values integers
local series
declare -a series
declare -i series

if [ "$N" -le "$K" ]; then
	echo "1"
else
	series=( $(seq -s ' ' 1 $K) )

	for ((i=K+1; i<=N; i++)); do
		sum=0
		for ((j=1;j<=K;j++)); do
			sum=$((sum+series[i-j]))
		done 
		series[i]=$sum
	done
	echo "${series[N]}"
fi
}

result=$(kfib $N $K)

echo "The $N-th term for a K=$K series is: $result"


