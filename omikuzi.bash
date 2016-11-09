#!/bin/bash

echo "おみくずぃ"
rand=$(( (RANDOM % 4) ))
i=1.0
while :
do
	i=`echo "$i-0.1" | bc`
	echo 1 > /dev/myled0
	sleep $i
	echo 0 > /dev/myled0
	sleep $i
	if [ $i = .1 ] ; then
		break
	else
		continue
	fi
done
if [ $rand = 0 ] ; then
	echo "大吉"
elif [ $rand = 1 ] ; then
	echo "中吉"
elif [ $rand = 2 ] ; then
	echo "吉"
else
	echo "大凶"
fi
