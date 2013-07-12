##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# Edit in UTF-8
# Tabsize = 4 space.

# A BGUI System setup to work with Blender.

import bgui
import bge
def end():
    mouse.visible = False
        
def UI(self):
  
    # TODO : Start GUI Script. #
       
    ide = '''Error! - can't get your ID'''
    pasw = '''1234'''
     
    mouse = bge.logic.mouse  
    mouse.visible = True
    mouse_event = mouse.events
     
    pos = list(mouse.position)

def connect(identity, password):
    idfile = open('Data/player/temp/id.idi', 'w')
    data = identity + "\n" + password
    idfile.write(data)

def main(cont):    
    mouse = bge.logic.mouse
    UI()
    
