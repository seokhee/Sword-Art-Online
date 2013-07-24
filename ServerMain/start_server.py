##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# FileName : start_server.py
# Edit in UTF-8
# Tabsize = 4 space.

import sys
import os
import socket
import threading
from log import *
import time

start_time = time.time()
version = 'v0.0.1.094'

print('''
##############################################
#        SAO MMORPG Project (c)2013          #
##############################################
 ''')
log('Start Server')
log('Server Version : ' + version)

# Server Program
           
PORT = 10010
HOST = '59.14.14.2'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
log('server is running on '+HOST+':'+str(PORT))
sock.listen(1000)

while True:
	(conn, addr) = sock.accept()
	text = str(addr[0])+' is connect!'
	log(text)
	text = str(addr[0])+' : '+str(conn.recv(1024)).split("'")[1]
	log(text)
	conn.close()

conn.close()
# End Server Program

end_time1 = time.time()
run_time = end_time1 - start_time

log('Server is run during ' + str(run_time) + ' sec')
log('server closed')
