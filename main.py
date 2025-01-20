import pgzrun
import random

WIDTH = 800
HEIGHT = 600
CENTER_X= WIDTH/2
CENTER_Y= HEIGHT/2
CENTER=(CENTER_X,CENTER_Y)
FINAL_LEVEL=6
START_SPEED=10
ITEMS=["bag","battery","chips","bottle"]
game_finish=False
game_over=False
current_level=1
items=[]
animations=[]

def draw():
    global items,current_level,game_over,game_finish
    screen.clear()
    screen.blit("bg",(0,0))

def update():
    pass

pgzrun.go()


