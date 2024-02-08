#!/bin/bash


alarm=$(($1*2))
sleep $alarm
echo Terminated a task that takes $alarm seconds

