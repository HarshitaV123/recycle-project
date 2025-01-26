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
    if game_over:
        display_message("You lose!","Try again next time.")
    elif game_finish:
        display_message("You win!","Good job!")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items=make_items(current_level)


def make_items(extra_items):
    items_to_create=get_option(extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items


def get_option(extra_items):
    items_to_create=["paper"]
    for i in range(extra_items):
        random_choice = random.choice(ITEMS)
        items_to_create.append(random_choice)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option + "img")
        new_items.append(item)
    return new_items
    
def layout_items(items_to_layout):
    num_of_gaps=len(items_to_layout) + 1
    size_gap= WIDTH/num_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x=(index+1)*size_gap
        item.x=new_x

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration= START_SPEED - current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global items, current_level, animations, game_finish
    stop_animations(animations)
    if current_level== FINAL_LEVEL:
        game_finish=True
    else:
        current_level +=1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text,sub_heading_text):
    screen.draw.text(heading_text, fontsize=50,center=CENTER,color="white")
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X,CENTER_Y+30),color="white")




pgzrun.go()


