#!/usr/bin/env python

'''Example of simple text wrapping without using layout.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

from pyglet.GL.VERSION_1_1 import *
from pyglet.window import *
from pyglet.window.event import *
from pyglet.window.key import *
from pyglet.clock import *
from pyglet.scene2d.textsprite import *
from pyglet.text import *

window = Window()
font = Font('Arial', 24)
text = 'Type away... '

def on_resize(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    sprite.width = width
    sprite.x = 10

def on_text(text):
    sprite.text += text.replace('\r', '\n')

def on_key_press(symbol, modifiers):
    if symbol == K_BACKSPACE:
        sprite.text = sprite.text[:-1]
    else:
        return EVENT_UNHANDLED

exit_handler = ExitHandler()
window.push_handlers(exit_handler)
window.push_handlers(on_resize)
window.push_handlers(on_text)
window.push_handlers(on_key_press)

sprite = TextSprite(font, text, color=(0, 0, 0, 1))

glClearColor(1, 1, 1, 1)

on_resize(window.width, window.height)

while not exit_handler.exit:
    window.dispatch_events()

    glClear(GL_COLOR_BUFFER_BIT)
    sprite.y = sprite.height # TODO align on bottom
    sprite.draw()
    window.flip()