##############################################
#        SAO MMORPG Project (c)2013          #
#      Editer : Lee Hee Jun @gmlwns5176      #
##############################################

# Edit in UTF-8
# Tabsize = 4 space.

import bgui
import bge

mouse = bge.logic.mouse

def end():
    mouse.visible = False
    
def UI():
    # TODO : Start GUI Script. #
    clicked = True
    ide = '''Error! - can't get your ID'''
    pasw = '''1234'''
    if clicked is True:
        connect(ide, pasw)

def connect(identity, password):
    idfile = open('Data/player/temp/id.idi', 'w')
    data = identity + "\n" + password
    idfile.write(data)
    
def main(cont):
    own = cont.owner
    UI()
    mouse.visible = True
    
