##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# FileName : lobby.py
# Edit in UTF-8
# Tabsize = 4 space.

# A BGUI System setup to work with Blender.

import sys
import bgui
import bge
import os
import socket
import log
import socket
from threading import Thread

nick = ''
chat = '''System > Connect to server'''
tmp1 = ''''''
i = 0
host = '127.0.0.1'
port = 10135
svrstat = 0
ishvrsnd = True
log.log_prefix = 'Lobby : '
winfoot = '../GUI/window-foot.png'
winhead = '../GUI/window-head.png'
winbody = '../GUI/window-body.png'

try:
	log.log('try connect to server!')
	clis = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clis.connect((host,port))
	nickf = open('./.sao/id.idi','r')
	nick = nickf.read()
	clis.sendall(bytes(nick, 'utf-8'))
except:
	chat = tmp1 + 'System > Server Error!' + tmp1 + '''
	
	-Server is offline! You can play only Story mode'''
	log.log('Server Error! : ')
	log.log('	- Detail : Server '+ host + ':' + str(port) + ' is now offline!')
	log.log('	- How to fix this problem? Way1 : Edit line 24, 25 in lobby.py.')
	log.log('	- How to fix this problem? Way2 : Start Server yourself.')
	log.log('	- How to fix this problem? Way3 : Talk to Server Manager.')
	svrstat = 1

class MySys(bgui.System):
	def __init__(self):
		global winfoot, winbody, winhead
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
		bgui.System.__init__(self, 'themas/lobby')
		log.log('init')
		
		#draw connections window
		self.note = bgui.Frame(self, 'note', border=0, size=[0.305, 0.7], pos=[0.68, 0.17], options=bgui.BGUI_DEFAULT)
		self.note.colors = [[0.9,0.9,0.9,0.0]] * 4
		self.lbl = bgui.Label(self.note, 'lblconnect', text="Connections",pt_size = 35, pos=[0.4,0.93], options = bgui.BGUI_DEFAULT)
		self.lbl.color = [0,0,0,1]
		items = [nick]+['Kirito','Kaira','Korui','YoungZaCharac','Hello','World','World of Sao','Dev','Build','df','ddd','wer','dd','Asuna']
		i1 = len(items) - 13
		if i1 < 1:
			i1 = 'no more'
		item = items[0:12] + ['... And '+str(i1)+' players.']
		self.listf = bgui.Frame(self.note, 'notef', border=0, size=[1, 0.85], pos=[0, 0.05], options=bgui.BGUI_DEFAULT)
		self.listf.colors = [[0.5, 0.5, 0.5, 0.0]] * 4
		
		self.lb = bgui.ListBox(self.listf, "lb", items=item, padding=0.05, size=[0.9, 0.9], pos=[0.05, 0.07])
		
		#draw chat window
		self.chat = bgui.Frame(self, 'chat', border=0, size=[0.66, 0.96], pos=[0.01, 0.02], options=bgui.BGUI_DEFAULT)
		self.chat.colors = [[0.9, 0.9, 0.9, 0.0]] * 4
		
		self.head = bgui.Image(self.chat, 'img', winhead, size = [1,0.07], pos = [0,0.93], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.foot = bgui.Image(self.chat, 'im', winfoot, size = [1, 0.06], pos = [0,0],  options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.foot.colors=[[0.7,0.7,0.7,0.0]]*4
		
		self.lblchat = bgui.Label(self.head, 'lblchat', text="Lobby",pt_size = 35, pos=[0.45,0.3], options = bgui.BGUI_DEFAULT)
		self.lblchat.color = [0,0,0,1]
		
		self.listc = bgui.Image(self.chat, 'notec', winbody, size=[1, 0.87], pos=[0.0, 0.06], options = bgui.BGUI_DEFAULT|bgui.BGUI_CACHE)
		self.buttons = bgui.FrameButton(self.foot, 'buttons', text='Send',pt_size = 30, size=[0.085, 0.75], pos=[0.895, 0.15],options = bgui.BGUI_DEFAULT)
		self.buttons.on_click = self.sendmessage
		self.buttons.on_hover = self.hover_sound
		self.buttons.on_mouse_exit = self.setting
		
		self.lblat = bgui.Label(self.foot, 'lblat', text=">",pt_size = 30, pos=[0.03,0.3], options = bgui.BGUI_DEFAULT)
		self.lblat.color = [0.5,0.5,0.5,0.8]
		
		self.input2 = bgui.TextInput(self.foot, 'input2', "",pt_size = 35, size=[1, 0.95], pos=[0.04, 0.01],
			input_options = bgui.BGUI_INPUT_SELECT_ALL, options = bgui.BGUI_DEFAULT)
		self.input2.color = [0.5,0.5,0.5,0.8]
		
		if svrstat == 0:
			self.chattext = bgui.TextBlock(self.listc, 'chatting',text = chat, pt_size = 28, color = [0.3,0.85,0.3,1], size = [0.98, 0.98], pos = [0.02,0])
			self.chattext.text = tmp1 + 'System > Connect to server' + tmp1
		elif svrstat == 1:
			self.chattext = bgui.TextBlock(self.listc, 'chatting',text = chat, pt_size = 28, color = [1,0.6,0.2,1], size = [0.98, 0.98], pos = [0.02,0])

		#creat next button
		self.button = bgui.FrameButton(self, 'button', text='Join Server',pt_size = 50, size=[0.14, 0.13], pos=[0.845, 0.022],options = bgui.BGUI_DEFAULT)
		self.button.on_click = self.multi
		self.button.on_hover = self.hover_sound
		self.button.on_mouse_exit = self.setting
		
		self.button = bgui.FrameButton(self, 'button1', text='Story Mode',pt_size = 50, size=[0.14, 0.13], pos=[0.68, 0.022],options = bgui.BGUI_DEFAULT)
		self.button.on_click = self.story
		self.button.on_hover = self.hover_sound
		self.button.on_mouse_exit = self.setting
		
		#creat Hello
		
		file1 = open('./.sao/id.idi','r')
		data = file1.readlines()
		file1.close()
		
		self.note2 = bgui.Frame(self, 'note2', border=0, size=[0.305, 0.1], pos=[0.68, 0.9], options=bgui.BGUI_DEFAULT)
		self.note2.colors = [[1,1,1,0.0]] * 4
		
		self.lbl2 = bgui.Label(self, 'lab2', text="Hello, "+str(data[0])+".",pt_size = 55, pos=[0.701,0.928], options = bgui.BGUI_DEFAULT)
		self.lbl2.color = [0,0,0,1]
		
		self.lbl1 = bgui.Label(self, 'labl', text="Hello, "+str(data[0])+".",pt_size = 55, pos=[0.7,0.93], options = bgui.BGUI_DEFAULT)
		self.lbl1.color = [1,1,1,1]
		
		# Create Key Map
		self.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}

	def multi(self, widget):
		if svrstat == 0:
			scene = bge.logic.getCurrentScene()
			scene.replace('multi')
			bge.logic.mouse.visible = False
		if svrstat == 1:
			chat = tmp1 + 'System > Server is offline!!' + tmp1
			self.chattext.text = chat
			log.log(chat)
			cont = bge.logic.getCurrentController()
			act = cont.actuators["Sound"]
			act.startSound()
		
	def hover_sound(self, widget):
		global ishvrsnd 
		if ishvrsnd is True:
			cont = bge.logic.getCurrentController()
			act = cont.actuators['hvr']
			act.startSound()
			ishvrsnd = False
	
	def setting(self, widget):
		global ishvrsnd
		if ishvrsnd is False:
			ishvrsnd = True
	
	def clk_sound(self):
		cont = bge.logic.getCurrentController()
		act = cont.actuators['clk']
		act.startSound()
	
	def story(self, widget):
		log.log('story mode')
		scene = bge.logic.getCurrentScene()
		scene.replace('story')
		bge.logic.mouse.visible = True
	
	def sendmessage(self):
		log.log('send message')
		if svrstat ==0:
			clis.sendall(bytes(self.input2.text,'utf-8'))
			data = clis.recv(1024)
			log.log('Player Send Msg : ' + self.input2.text)
			self.input2.text = ''
			self.clk_sound()
		elif svrstat == 1:
			log.log('Player Lost Msg : ' + self.input2.text)
			self.input2.text = ''
			self.chattext.text = tmp1 + 'System > Server is offline!' + tmp1
			log.log('Server Error! cause:server is offline.')
			self.clk_sound()
			
			
	def con2ser(self, widget):
		print('link start')
	
	def rechat(self, widget):
		print('rechat')
	
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
	keyboard = bge.logic.keyboard
	JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_RELEASED
	if keyboard.events[bge.events.SPACEBAR] == JUST_ACTIVATED:
		own['sys'].sendmessage()
	
	if 'sys' not in own:
		# Create our system and show the mouse
		own['sys'] = MySys()
		mouse.visible = True
		log.log('add Mysys()')
	else:
		own['sys'].main()

clis.close()
