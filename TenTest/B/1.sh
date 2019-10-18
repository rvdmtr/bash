#!/bin/bash

echo "Где встречается Tensor">_result.txt;
#1.1.1
#grep Tensor ./* >>_result.txt
echo "В каких строках встречается слово: ">>_result.txt;
#1.1.2
grep -n Tensor ./* >> _result.txt 2>/dev/null;
echo "Сколько вхождений и в каком файле: ">>_result.txt;
#1.1.3
grep -c  Tensor ./* >> _result.txt 2>/dev/null;

