from sprites_Def import *

import pyglet

from pyglet import shapes 
from pyglet.gl import *
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


frase = input('insert frase: ')

sprite = input('insert sprite id: ')

if sprite == '':
  anim = Animation_000

if sprite == '000':
  anim = Animation_000

elif sprite == '001':
  anim = Animation_001

elif sprite == '002':
  anim = Animation_002

elif sprite == '003':
  anim = Animation_003

elif sprite == '004':
  anim = Animation_004

elif sprite == '005':
  anim = Animation_005

elif sprite == '006':
  anim = Animation_006

elif sprite == '007':
  anim = Animation_007

for i in range(2):
  Animation = pyglet.image.Animation.from_image_sequence(anim, 0.25, True)
  sprite = pyglet.sprite.Sprite(Animation)

window = pyglet.window.Window(1280, 720, "Ace Programmer", resizable=True)


path = 'D:\Python\Game1\Def/Stand_Def/banco.png'
path2 = 'D:\Python\Game1\Def/Stand_Def/courtroom.png'

desk = pyglet.image.load(path)

background = pyglet.image.load(path2)

label = pyglet.text.Label(frase,
                          font_name='Comic Sans',
                          font_size=19,
                          x=256, y=170,
                          anchor_x='center', anchor_y='center')

batch = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()
batch3 = pyglet.graphics.Batch()
batch4 = pyglet.graphics.Batch()

co_x = -1
co_y = 40
co2_y = 35
co3_y = 190

width = 1282
height = 150
height2 = 5

color = (0, 0, 51)
color2 = (255, 255, 255)

rec = shapes.Rectangle(co_x, co_y, width, height, color = color, batch = batch)

rec2 = shapes.Rectangle(co_x, co2_y, width, height2, color = color2, batch = batch2)

rec3 = shapes.Rectangle(co_x, co3_y, width, height2, color = color2, batch = batch3)

rec.opacity = 235
rec2.opacity = 255
rec3.opacity = 255

@window.event
def on_draw():
    window.clear

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    background.blit(0, 0)
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    sprite.draw()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    desk.blit(0, 0)
    
    batch2.draw()
    batch3.draw()
    batch.draw()
    label.draw()

if __name__ == '__main__':
  pyglet.app.run()
