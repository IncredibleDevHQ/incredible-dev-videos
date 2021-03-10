#welcome.sh
#!/bin/bash
greeting="Welcome"
user=$(whoami)
day=$(date +%A)

echo "$greeting back $user!"
echo "Today is $day, which is the best day !"
echo "Your Bash shell version is: $BASH_VERSION." 

#to execute $./welcome.sh
# Welcome back Incredibles' !
#Today is Monday, which is the best day !
# Your Bash shell version is: 5.0.17(1)-release. !
