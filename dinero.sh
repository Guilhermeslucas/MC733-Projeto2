#!/bin/bash

path="/home/ec2014/ra157537/traces/"
dirs=`ls $path`

for i in $dirs;
do
    touch $i\_"output.txt"
done

for j in {2..6};
do
    for k in {1..64}
    do
        for i in $dirs;
        do
            aux=${i:4}
            aux1=`echo $aux | cut -d'.' -f1`
            aux2=`echo $aux | cut -d'.' -f2`
            aux=`echo $aux1\_$aux2`
            (cd /home/ec2014/ra157537/traces/$i && /home/ec2014/ra157537/dinero/d4-7/dineroIV -informat s -trname $aux -maxtrace 20 -l1-isize 1024k -l1-dsize 1024k -l1-ibsize `echo "2^$j" | bc`  -l1-dbsize `echo "2^$j" | bc` -l1-iassoc $k -l1-dassoc $k >> $i\_"second_output.txt")
        done
    done
done
