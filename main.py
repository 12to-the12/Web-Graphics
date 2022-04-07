from browser import document, window

from math import atan, degrees
from random import random
moving = document["button"]
page = document["page"]
x = 50
y = 50
dx = -5
dy = 0
gravity = 0.1
damping = 1
run = None
ang = 0
arena_width = page.width - 100
arena_height = page.height - 100
print(page.width)
print(page.height)
x = random()*arena_width
x = random()*arena_height


def render():
    global x, dx, y, dy, gravity
    global arena_width, arena_height
    moving.style.transform = f"translate({x}px,{y}px) rotate({angle()}deg)"
    x += dx
    y += dy
    if x>=arena_width: dx *= -1 # right wall
    if x<=0: dx *= -1 # left wall
    
    if y >= arena_height:# floor
        y = arena_height
        dy *= damping
        dy *= -1
    if y <= 0:# ceiling
        y = 0
        dy *= -1
    
    dy+=gravity

def angle():
    global dx, dy, ang
    # angles are clockwise so god help me
    if dx>0:
        if dy>0:# quadrant 4
            ang = 90 + degrees( atan(dy/dx) )
        elif dy<0:# quadrant 1
            ang = degrees( atan(dx/-dy) )
        else: return ang
    elif dx<0:
        if dy>0: # quadrant 3
            ang = 180 + degrees( atan(-dx/dy) )
        elif dy<0: # quadrant 2
            ang = 270 + degrees( atan(-dy/-dx) )
        else: return ang
    else: return ang
    return ang
    


def animloop(t):
    global run
    run = window.requestAnimationFrame(animloop)
    render()

run = window.requestAnimationFrame(animloop)