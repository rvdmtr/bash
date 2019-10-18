#!/bin/bash

if grep AM 2_1_datetime > /dev/null
then 
	cat 2_1_datetime
else
	cp 2_1_datetime 2_1_datetime.bak;date >>2_1_datetime.bak

fi
