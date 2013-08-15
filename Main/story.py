##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# File Name : log.login.py
# Edit in UTF-8
# Tabsize = 4 space.

import log
import sys
import os
import bgui
import bge
from time import *

log.log_prefix = "Story Mode : "
log.log('Link start!')
log.log('Play on Story Mode.')

lctime = strftime('%H:%M:%S', localtime())

class MySys(bgui.System):
	def __init__(self):
		
		#init bgui
		bgui.System.__init__(self, 'default')
		log.log('Blender Graphic User Interface is Loaded')
		
		#clock text
		self.lbl = bgui.Label(self, 'lblconnect', text=lctime, pt_size = 45 ,pos=[0.85,0.92],sub_theme='Large', options = bgui.BGUI_DEFAULT)
		self.lbl.color = [0,0,0,0.5]
		
		# A themed frame
		self.win = bgui.Frame(self, 'win', border=0, size=[0.66, 0.96], pos=[0.01, 0.02], options=bgui.BGUI_DEFAULT)
			
		# Create an image to display
		self.win.img = bgui.Image(self.win, 'image', 'main_back.png', size=[.92, .7], pos=[.01, .24],	options = bgui.BGUI_DEFAULT|bgui.BGUI_CENTERX|bgui.BGUI_CACHE)
		
		# Create Key Map
		self.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}
	
	def reclock(self):
		self.lbl.text = strftime('%H:%M:%S', localtime())
	
	def main(self):
		"""A high-level method to be run every frame"""
		
		# Handle the mouse
		mouse = bge.logic.mouse
		
		pos = list(mouse.position)
		pos[0] *= bge.render.getWindowWidth()
		pos[1] = bge.render.getWindowHeight() - (bge.render.getWindowHeight() * pos[1])
		
		mouse_state = bgui.BGUI_MOUSE_NONE
		mouse_events = mouse.events
				
		if mouse_events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_JUST_ACTIVATED:
			mouse_state = bgui.BGUI_MOUSE_CLICK
		elif mouse_events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_JUST_RELEASED:
			mouse_state = bgui.BGUI_MOUSE_RELEASE
		elif mouse_events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_ACTIVE:
			mouse_state = bgui.BGUI_MOUSE_ACTIVE
		
		self.update_mouse(pos, mouse_state)
		
		# Handle the keyboard
		keyboard = bge.logic.keyboard
		
		key_events = keyboard.events
		is_shifted = key_events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE or \
					key_events[bge.events.RIGHTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE
					
		for key, state in keyboard.events.items():
			if state == bge.logic.KX_INPUT_JUST_ACTIVATED:
				self.update_keyboard(self.keymap[key], is_shifted)
		
		# Now setup the scene callback so we can draw
		bge.logic.getCurrentScene().post_draw = [self.render]

def main(cont):
	own = cont.owner
	if 'sys' not in own:
		# Create our system and show the mouse
		own['sys'] = MySys()
	else:
		own['sys'].main()
		own['sys'].reclock()
