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
import time

log.log_prefix = "Story Mode : "
log.log('Link start!')
log.log('Play on Story Mode.')


class MySys(bgui.System):
	def __init__(self):
		'''
		Menual
		
		# Initialize the system
		bgui.System.__init__(self, '../GUI/BGUI/themes/default')
		
		# Use a frame to store all of our widgets
		self.frame = bgui.Frame(self, 'window', border=0)
		self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

		# A themed frame
		self.win = bgui.Frame(self, 'win', size=[0.6, 0.8],
			options=bgui.BGUI_DEFAULT|bgui.BGUI_CENTERED)
			
		# Create an image to display
		self.win.img = bgui.Image(self.win, 'image', 'img.jpg', size=[.92, .7], pos=[.01, .24],
			options = bgui.BGUI_DEFAULT|bgui.BGUI_CENTERX|bgui.BGUI_CACHE)
		
		# A button
		self.button = bgui.FrameButton(self.win, 'button', text='Click Me!', size=[.14, .09], pos=[.815, .03],
			options = bgui.BGUI_DEFAULT)
		self.audio_button = bgui.ImageButton(self.win, 'ab', sub_theme='Audio',
										size=[0.05, 0.05], pos=[0.75, 0.05])
		# Setup an on_click callback for the image
		self.button.on_click = self.on_img_click

		# Add a label
		self.lbl = bgui.Label(self, 'label', text="I'm a label!", pos=[0, 0.9],
			sub_theme='Large', options = bgui.BGUI_DEFAULT | bgui.BGUI_CENTERX)
		
		# A couple of progress bars to demonstrate sub themes
		self.progress = bgui.ProgressBar(self.win, "progess", percent=0.0, size=[0.92, 0.06], pos=[.2, 0.17],
											sub_theme="Progress", options=bgui.BGUI_DEFAULT | bgui.BGUI_CENTERX)
											
		self.health = bgui.ProgressBar(self.win, "health", percent=0.5, size=[0.92, 0.02], pos=[0, 0.14],
											sub_theme="Health",	options=bgui.BGUI_DEFAULT|bgui.BGUI_CENTERX)
			
		# A few TextInput widgets
		self.input = bgui.TextInput(self.win, 'input', "I'm active.", font="myfont.otf", size=[.4, .04], pos=[.04, 0.02],
			input_options = bgui.BGUI_INPUT_NONE, options = bgui.BGUI_DEFAULT)
		self.input.activate()
		self.input.on_enter_key = self.on_input_enter
		
		self.input2 = bgui.TextInput(self.win, 'input2', "I select all when activated.한글", size=[.4, .04], pos=[.04, 0.08],
			input_options = bgui.BGUI_INPUT_SELECT_ALL, options = bgui.BGUI_DEFAULT)
		
		# A counter property used for the on_img_click() method
		self.counter = 0
		
		# Create a keymap for keyboard input
		self.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}
		'''
		
		#init bgui
		bgui.System.__init__(self)
		log.log('Story Mode : ')
		
		# Create Key Map
		self.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}
		
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
