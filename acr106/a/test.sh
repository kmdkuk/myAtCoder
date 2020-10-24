#!/usr/bin/env bash
for i in `seq 100`
do
    for j in `seq 100`
    do
        res=`python test.py $i $j | python main.py`
        if [ res = '-1']; then
            echo 'error'
            echo '$i $j'
        fi
    done
done
