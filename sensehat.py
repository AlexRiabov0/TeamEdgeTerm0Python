from time import sleep
from sense_hat import SenseHat
import random
import threading

# init sensehat obj
sense = SenseHat()
sense.clear()

# global variables
game_over = False
timer_time = False
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

def update():
    sense.clear()
    sense.set_pixel(catcher_x,7,c)
    sense.set_pixel(berry_x,berry_y,p)

def move_left():
    global catcher_x
    if catcher_x >= 1:
        catcher_x -= 1

def move_right():
    global catcher_x
    if catcher_x <=6:
        catcher_x += 1


def cautcher_1():
        global berry_x
        global berry_y
        for event in sense.stick.get_events():
            if event.direction == "left" and event.action =="pressed":
                move_left()
                print(catcher_x)
                update()
            if event.direction == "right" and event.action =="pressed":
                move_right()
                print(catcher_x)
                update()  
            if catcher_x == berry_x and berry_y == 7:
                print("Win")
                plus_win_points()
                print(str(win_points))
                berry_y = 0
                berry_x = random.randint(0,7)
                    
            elif berry_y == 7 and catcher_x!= berry_y:
                print("Looser")
                sense.show_message("You loose", text_colour=o, scroll_speed=.05)
# *******
def start_fun():
    while timer_time == True:
        berry()
# *******

def berry():
        for i in range(0,8):
            global berry_y
            berry_y = i
            update()
            sleep(.7)
        start_fun()
 # multiprocessing




    
    
        
def timer_game():
    global timer_time
    timer_time = True
    for i in range(0,30):
        sleep(0.999999)
    game()
    sense.show_message("You win", text_colour=o, scroll_speed=.05)
    sense.show_letter(str(win_points))
    sense.set_pixel(berry_x,berry_y,o)



def game():
    global game_over
    game_over=True

    

# # multiprocessing
# Thread1 = threading.Thread(target = start_fun)
# Thread2 = threading.Thread(target = timer_game)


hello_message()
timer_game()
Thread1 = threading.Thread(target = cautcher_1)
Thread2 = threading.Thread(target = start_fun)
Thread1.start()
Thread2.start()
