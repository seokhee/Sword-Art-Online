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
is_Menu_Open = False
menu_Status = 5
iss = 1

class MySys(bgui.System):
	def __init__(self):
		#init bgui
		bgui.System.__init__(self, 'themas/story')
		log.log('Blender Graphic User Interface is Loaded')	
		
		# Show clock
		self.clockimg = bgui.Image(self, 'image', '../GUI/GUI_clock.png', size=[0.13, 0.06], pos=[0.86, 0.92], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.clocklbl = bgui.Label(self.clockimg, 'lblconnect', text=lctime, pt_size = 45 ,pos=[0.26,0.24], options = bgui.BGUI_DEFAULT)
		self.clocklbl.color = [0,0,0,0.5]
		
		# Show Main Menu
		self.main_frame = bgui.Frame(self, 'main_frame', border=0, size=[0.4,0.8], pos=[-1, 0.15]) # This Menu GoTo 0.3
		self.main_frame.colors = [[0,0,0,0]] * 4
		
		self.main_menu = bgui.Image(self.main_frame, 'main_menu', '../GUI/GUI_Main_Manu.png', size=[0.7,1], pos=[0, 0])
		self.main_menu.colors = [[0.9,0.9,0.9,0.5]] * 4
		
		# Show Sub Menu
		self.sub_menu = bgui.Frame(self.main_frame, 'sub_menu', border=0, size=[0.3,1.5], pos=[0.7, -0.9], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE) # 1:-0.9 2:-0.6  3:-0.3  4:0  5:0.3
		self.sub_menu.colors = [[0.5,0,0.5,0]] * 4
		
		# Show Sub Menu Menu
		self.sub_menu_1 = bgui.Image(self.sub_menu, 'sub_menu_1', '../GUI/Button_Empty.png', size=[1,0.2], pos=[0, 0], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.sub_menu_2 = bgui.Image(self.sub_menu, 'sub_menu_2', '../GUI/Button_Empty.png', size=[1,0.2], pos=[0, 0.2], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.sub_menu_3 = bgui.Image(self.sub_menu, 'sub_menu_3', '../GUI/Button_Empty.png', size=[1,0.2], pos=[0, 0.4], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.sub_menu_4 = bgui.Image(self.sub_menu, 'sub_menu_4', '../GUI/Button_Empty.png', size=[1,0.2], pos=[0, 0.6], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.sub_menu_5 = bgui.Image(self.sub_menu, 'sub_menu_5', '../GUI/Button_Empty.png', size=[1,0.2], pos=[0, 0.8], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		
		# Create Key Map
		self.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}

	def reclock(self):
		self.clocklbl.text = strftime('%p %I:%M:%S', localtime())
	
	def openMenu(self):
		self.main_frame.move([0.4, 0.15],300)
	
	def closeMenu(self):
		self.main_frame.move([-1, 0.15],300)
	
	def moveMenu(self):
		global menu_Status
		if menu_Status == 1:
			self.sub_menu.position = [0.7, 0.3]
		elif menu_Status == 2:
			self.sub_menu.position = [0.7, 0]
		elif menu_Status == 3:
			self.sub_menu.position = [0.7, -0.3]
		elif menu_Status == 4:
			self.sub_menu.position = [0.7, -0.6]
		elif menu_Status == 5:
			self.sub_menu.position = [0.7, -0.9]
	
	def hover_sound():
		global iss ######!!! IMPORTANT !!!  Make sure
		if iss == 1:
			iss = 0
			cont = bge.logic.getCurrentController()
			act = cont.actuators['sound_hover']
			act.startSound()
	
	def hover_sound_on(self):
		global iss
		iss = 1
	
	def start_sound(self, actuators):
		cont = bge.logic.getCurrentController()
		act = cont.actuators[actuators]
		act.startSound()
	
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
	global is_Menu_Open
	global menu_Status
	own = cont.owner	
	co = bge.logic.getCurrentController()
	# 'Keyboard' is a keyboard sensor
	keyboard = bge.logic.keyboard
	JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_RELEASED
	mouse = bge.logic.mouse
	if 'sys' not in own:
		# Create our system and show the mouse
		own['sys'] = MySys()
	else:
		own['sys'].main()
		own['sys'].reclock()
	
	if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED:
		if is_Menu_Open == False:
			menu_Status = 5
			own['sys'].moveMenu()
			own['sys'].openMenu()
			log.log('Open Menu')
			is_Menu_Open = True
			mouse.visible = True
			own['sys'].start_sound('window_open')
		
		elif is_Menu_Open == True:
			own['sys'].closeMenu()
			log.log('Close Menu')
			mouse.visible = False
			is_Menu_Open = False
			own['sys'].start_sound('window_close')
	if is_Menu_Open == True:
		if mouse.events[bge.events.WHEELUPMOUSE] == JUST_ACTIVATED:
			if menu_Status > 1:
				menu_Status = menu_Status - 1
				own['sys'].moveMenu()
				own['sys'].start_sound('sound_move')
		
		elif mouse.events[bge.events.WHEELDOWNMOUSE] == JUST_ACTIVATED:
			if menu_Status < 5:
				menu_Status = menu_Status + 1
				own['sys'].moveMenu()
				own['sys'].start_sound('sound_move')
	
os.chdir(bge.logic.expandPath('//'))
