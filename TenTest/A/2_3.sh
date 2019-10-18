#!/bin/bash

k=$1

if grep AM 2_1_datetime > /dev/null
then 
	cat 2_1_datetime
else
	cp 2_1_datetime 2_1_datetime.bak;date >>2_1_datetime.bak

fi



for ((i=1;i<=$k;i++))
do . 2_2.sh
done
