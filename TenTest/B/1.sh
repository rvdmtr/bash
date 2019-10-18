#!/bin/bash

echo "Где встречается word">_result.txt;
#1.1.1
#grep word ./* >>_result.txt
echo "В каких строках встречается слово: ">>_result.txt;
#1.1.2
grep -n word ./* >> _result.txt 2>/dev/null;
echo "Сколько вхождений и в каком файле: ">>_result.txt;
#1.1.3
grep -c  word ./* >> _result.txt 2>/dev/null;

