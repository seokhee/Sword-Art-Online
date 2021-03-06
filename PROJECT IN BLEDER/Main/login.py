##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# File Name : login.py
# Edit in UTF-8
# Tabsize = 4 space.

# A BGUI System setup to work with Blender.
import sys
import bgui
import bge
import time
import os
import log
from bge import logic

log.log(''+os.getcwd())

identity = 'ID'
password = 'Password'

if not os.path.isdir('.sao'):
	os.mkdir('.sao')
	log.log('''mkdir ".sao" ''')
	log.log(os.getcwd())

file1 = open('.sao/id.idi')
identity = file1.read()
file1.close()

file2 = open('.sao/pass.idi')
password = file2.read()
file2.close()
log.log_prefix = 'Login : '
iss = 1

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
		bgui.System.__init__(self, 'themas/login')
		log.log('start game')
		
		#button create
		self.button = bgui.FrameButton(self, 'btn', base_color = [0.1,0.1,0.1,0.9], text='Link Start!',pt_size = 35, size=[0.11, 0.06], pos=[0.665, 0.21], options = bgui.BGUI_DEFAULT)
		self.button.on_click = self.login
		self.button.on_hover = self.hover_sound
		self.button.on_mouse_exit = self.setting
		
		#Active lable
		#id
		self.input2 = bgui.TextInput(self, 'identity',identity,pt_size = 38 , color = [0,0,0,1],size=[0.21, 0.08], pos=[0.23, 0.2],
			input_options = bgui.BGUI_INPUT_SELECT_ALL)
		self.input2.on_hover = self.hover_sound
		self.input2.on_mouse_exit = self.setting
		
		#password
		self.input3 = bgui.TextInput(self, 'password', password,pt_size = 38, size=[0.21, 0.08], pos=[0.45, 0.2], input_options = bgui.BGUI_INPUT_SELECT_ALL, options = bgui.BGUI_DEFAULT)
		self.input3.on_hover = self.hover_sound
		self.input3.on_mouse_exit = self.setting
		
		# Create Key Map
		self.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}
		
	def login(self, widget):
		log.log("login")
		#Change Scene...
		try:
			log.log('cheak .sao folder')
			dirname = './.sao'
			if not os.path.isdir('./.sao'):
				os.mkdir('./.sao')
				log.log('''mkdir ".sao" ''')
			log.log('start write id')
			file1 = open('./.sao/id.idi','w')
			file1.write(self.input2.text)
			file1.close()
			log.log('start write pass')
			file2 = open('./.sao/pass.idi', 'w')
			file2.write(self.input3.text)
			file2.close()
			scene = bge.logic.getCurrentScene()
			scene.replace('First_effect')
			log.log('go login scene')
		except:
			scene = bge.logic.getCurrentScene()
			scene.replace('error')
			log.log('Error on login')
	
	def hover_sound(self, widget):
		global iss ######!!! IMPORTANT !!!  Make sure
		if iss == 1:
			iss = 0
			cont = bge.logic.getCurrentController()
			act = cont.actuators['hvr']
			act.startSound()
		
	def setting(self, widget):
		global iss
		if iss == 0:
			iss = 1
	
	def sceret(self):
		self.input3.text = '*' * len(self.input3.text)
		
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
	mouse = bge.logic.mouse
	
	#print(os.getcwd())
	
	if 'sys' not in own:
		# Create our system and show the mouse
		own['sys'] = MySys()
		mouse.visible = True
	else:
		own['sys'].main()
