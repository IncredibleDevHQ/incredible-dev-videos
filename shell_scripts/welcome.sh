#!/bin/bash

greeting="Welcome"
user=$(whoami)
day=$(date +%A)

echo "$greeting back $user! Today is $day, which is the best day of the entire week!"
echo "Your Bash shell version is: $BASH_VERSION. Enjoy!"

# output
# Welcome back hemaalatha! Today is Monday, which is the best day of the entire week!
# Your Bash shell version is: 5.0.17(1)-release. Enjoy!
