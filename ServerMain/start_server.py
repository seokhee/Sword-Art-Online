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
import log
import time

start_time = time.time()
version = 'v0.0.1.001'

print('''
##############################################
#        SAO MMORPG Project (c)2013          #
##############################################
 ''')
log.log('Start Server')
log.log('Server Version : ' + version)

# Server Program
           
PORT = 10010
HOST = '59.14.14.2'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
log.log('server is running on '+HOST+':'+str(PORT))
sock.listen(1000)

while True:
	(conn, addr) = sock.accept()
	addr

conn.close()
# End Server Program

end_time1 = time.time()
run_time = end_time1 - start_time

log.log('Server is run during ' + str(run_time) + ' sec')
log.log('server closed')
