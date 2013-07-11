import bgui
import bge

"""
A BGUI System setup to work with Blender
"""
def __init__(self):
# Initialize the system (replace the None with a path to a theme if you have one)
        bgui.System.__init__(self, None)

# Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, 'window', border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]
               
# Add widgets here and attach them to the frame
                
                # Create a keymap for keyboard input
        pself.keymap = {getattr(bge.events, val): getattr(bgui, val) for val in dir(bge.events) if val.endswith('KEY') or val.startswith('PAD')}

def main(self):
        mouse.visible = True
                """A high-level method to be run every frame.
                        This handles things like sending mouse and keyboard events to BGUI."""
                
                # Handle the mouse
        mouse = bge.logic.mouse
        mouse_events = mouse.events
                
                # Get the position
        pos = list(mouse.position)
        pos[0] *= bge.render.getWindowWidth()
        pos[1] = bge.render.getWindowHeight() - (bge.render.getWindowHeight() * pos[1])
                                
                # Get the mouse state
        if mouse_events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_JUST_ACTIVATED:
                mouse_state = bgui.BGUI_MOUSE_CLICK
        elif mouse_events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_JUST_RELEASED:
                mouse_state = bgui.BGUI_MOUSE_RELEASE
        elif mouse_events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_ACTIVE:
                mouse_state = bgui.BGUI_MOUSE_ACTIVE
        else:
                mouse_state = bgui.BGUI_MOUSE_NONE
                
                # Send the position and state to BGUI
        self.update_mouse(pos, mouse_state)
                
                # Handle the keyboard
        keyboard = bge.logic.keyboard
                
                # Get the keys
        key_events = keyboard.events
        is_shifted = key_events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE or \
                key_events[bge.events.RIGHTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE
                                        
                # Update keys for BGUI
        for key, state in keyboard.events.items():
                if state == bge.logic.KX_INPUT_JUST_ACTIVATED:
                        self.update_keyboard(self.keymap[key], is_shifted)
                
                # Now setup the scene callback so we can draw
        bge.logic.getCurrentScene().post_draw = [self.render]

def main(cont):
        """main() method to attach to a module controller in the BGE"""
        
        own = cont.owner
        mouse = bge.logic.mouse
        mouse.visible = True
        main()
        
