#!/bin/bash
#2.3

mv -v ./N1/*/* ./N1 |grep renam|awk '{print $2}'|sed 's|.*/||' > aname.txt |awk -F "'" '{print $1}'|xargs -I% ls -lh "%" |awk -F " " '{print "Date_"$7"_"$6"  Time_"$8"  Size_"$5"b  Name_"$9}'
