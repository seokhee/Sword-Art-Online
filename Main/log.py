##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# FileName : log.py (For Game main)
# Edit in UTF-8
# Tabsize = 4 space.

import time
from time import localtime, strftime

log_prefix = ''
log_endfix = ''

def log(text):
	try:
		prt = "["+strftime('%Y-%m-%d %H:%M:%S', localtime())+"] "+ log_prefix + text + log_endfix
		logfile = open('.sao/game.log','a')
		logfile.write(prt+'\n')
		logfile.close()
		print(prt)
	except IOError as err:
		print('-File I/O Error-\n'+"Detail : "+err)
