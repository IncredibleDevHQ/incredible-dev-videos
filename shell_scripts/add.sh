sum=0
for i in $*
do
    sum=`expr $sum + $i`
done
echo "Summation of "$#" nos. is: "$sum

OUTPUT
***********
$./sum.sh 10 20
Summation of 2 nos. is: 30
