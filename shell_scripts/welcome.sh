#!/bin/bash
#Create a file called welcome.sh($vi welcome.sh)
greeting="Welcome"
user=$(whoami)
day=$(date +%A)

echo "$greeting back $user! Today is $day, which is the best day !"
echo "Your Bash shell version is: $BASH_VERSION. Enjoy!"

#For giving permissions $chmod 777 welcome.sh 
#to execute $./welcome.sh
# Welcome back Incredibles' ! Today is Monday, which is the best day !
# Your Bash shell version is: 5.0.17(1)-release. Enjoy!
