#!/bin/sh
a=10
b=20
val=`expr $a + $b`
echo "a + b : $val" #30
val=`expr $a - $b` 
echo "a - b : $val" #-10
val=`expr $a \* $b` 
echo "a * b : $val" #200
val=`expr $b / $a`
echo "b / a : $val" #2
val=`expr $b % $a`
echo "b % a : $val" #0
