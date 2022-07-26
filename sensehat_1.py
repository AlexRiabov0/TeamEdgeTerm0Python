from time import sleep
from sense_hat import SenseHat
import random
import threading

# init sensehat obj
sense = SenseHat()
sense.clear()

# global variables
game_over = False
catcher_x = 0
berry_x = random.randint(0,7)
berry_y = 0
win_points = 0

# catcher color
c = (0, 255, 255)

# pink color
p = (255, 0, 128)

# orange color
o = (255, 128, 0)

# fun for TIMER
def plus_win_points():
    global win_points
    win_points +=1



def hello_message():
    sense.show_message("Catcher", text_colour=o, scroll_speed=.05)
    sleep(.5)
    sense.show_letter("3")
    sleep(.5)
    sense.show_letter("2")
    sleep(.5)
    sense.show_letter("1")
    sleep(.5)



# TIMER
def timer_game():
    for i in range(0,30):
        sleep(0.999999)
    game()
    sense.show_message("You win", text_colour=o, scroll_speed=.05)
    sense.show_letter(str(win_points))
    sense.set_pixel(berry_x,berry_y,o)

def first_start():
    
