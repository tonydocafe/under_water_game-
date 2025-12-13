from pgzero.actor import Actor
from pgzero.clock import clock

explosion = Actor("explosion")
explosion.visible = False

def show_explosion(x, y):
    explosion.pos = (x, y)
    explosion.visible = True
    clock.schedule(hide_explosion, 0.3)

def hide_explosion():
    explosion.visible = False
