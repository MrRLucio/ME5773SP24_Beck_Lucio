#!/bin/bash

ftorial=1

for ((i = 1; i <= $1; i += 1))
do
	ftorial=$((ftorial*i))
	echo $i! = $ftorial
done
