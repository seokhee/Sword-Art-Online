##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# FileName : lobby.py
# Edit in UTF-8
# Tabsize = 4 space.

import sys
import os
import time
import socket
import threading
import time
from time import localtime, strftime

host = ''
port = 2013
def main():
	print('''##############################################
#        SAO MMORPG Project (c)2013          #
##############################################''')
	log('')
	log('Start Server')
	cmd = input('>')

def log(text):
	try:
		prt = "["+strftime('%Y-%m-%d %H:%M:%S', localtime())+"] "+ text
		logfile = open('server.log','a')
		logfile.write(prt+'\n')
		logfile.close()
		print(prt)
	except IOError as err:
		print('-File I/O Error-\n'+"Detail : "+err)

main()

