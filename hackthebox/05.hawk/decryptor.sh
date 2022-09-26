#!/bin/bash

declare -r file="message.decrypted"

while read password; do
	openssl aes-256-cbc -d -in message.crypted  -out message.decrypted -k $password 2>/dev/null
	if [ "$(echo $?)" == "0" ] ; then
		echo -e "\n [*] La Password es $password: [*] \n"
		cat $file
  		break
	fi
done < /usr/share/wordlists/rockyou.txt
