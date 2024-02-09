#!/bin/bash
#
# This program shows the K-Fibbonacci Sequence up to term N,
# where N is the first input, and K is the second
#
#

N=$1
k=$2

if [[ "$N" -le "0" ]]; then
	echo "Please enter a positive, non-zero value for N"
	exit 1
elif [[ "$k" -le "0" ]]; then
	echo "Please enter a positive, non-zero value for K; The Fibbonacci Sequence cannot have K < 1"
	exit 1
fi

echo "Going to term $N of the $k-Fibbonacci Sequence"

#establishing a limiter, in case N < K
if [[ "$N" -le "$k" ]]; then
	lmtr=$N
else
	lmtr=$k
fi

##initializing the initial 1-terms of the K-Fibbonacci Sequence
#first making an array to append to
fib=(1)

#appending ones until there are K ones in the array.
for((i = 1; i<$lmtr; i+=1))
do
    fib+=(1)
done

#test for accuracy
#echo ${fib[@]}

#Finding the terms after the initial K ones.
counter=0
for((i = $k; i<$N; i++))
do
	#creating a variable toget the some of the previous K terms in the series
	counter=0

	#finding the previous k terms to the one being inserted, and adding them together
	for((j = $i; j>($i-$k); j--))
	do
		#arrays have a zero-based index, whereas the code is going by 1. Correcting with n
		n=j-1
		counter=$(($counter+${fib[n]}))
	done
	fib+=($counter)
done

echo ${fib[@]}
