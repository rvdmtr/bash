#!/bin/bash

#2.1.1
#mkdir ./N1;
#mv ./N/* ./N1/

#2.1.2
#mkdir ./N1;
#mv ./N/*/* ./N1/

#2.1.3
#2.3

#mv -v ./N1/*/* ./N1/ |grep renam|awk '{print $2}'|sed 's|.*/||' > ./N1/_result.txt;cd N1/;
#cat _result.txt |awk -F "'" '{print $1}'|xargs -I% ls -lh "%" |awk -F " " '{print "Date_"$7"_"$6"  Time_"$8"  Size_"$5"b  Name_"$9}'>_result.txt

