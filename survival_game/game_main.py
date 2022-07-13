# ************************************************************
# CHOOSE YOUR OWN ADVENTURE GAME - THE SEARCH FOR SURVIVAL
# 
# The main character (you) will control will start in the middle of the forest. 
# They will need to progress through an apocalyptic world and find survival. 
# 
# GAME FEATURES: 
# 1. USER INPUT
# 2. A PLAYER CAN TYPE "GO TO" AND HEAD TO A LOCATION FROM THEIR CURRENT LOCATION
# 3. A PLAYER CAN TYPE "OBSERVE"
# 4. SOME LOCATIONS HAVE NPCs AND YOU CAN INTERACT WITH THEM TO LEARN MORE ABOUT YOUR SURROUNDINGS
# 5. BASED ON YOUR ACTIONS, YOU WILL UNLOCK DIFFERENT TYPES OF ENDINGS. 
# 6. IF A PLAYER ENTERS A LOCATION WITH A MONSTER, THEY WILL LOSE HEALTH
# 7. IF THEY REACH THE CITY, MEET LOVE INTEREST, OR DIE, THE GAME WILL END 
#
# ************************************************************

import random
from random import choices


# =======VARIABLES======
# variable to chance
global chance_survival
global chance_death
# other
current_room = None
rooms = []
input_message = ""
game_running = True # 


#************** DEFINE CLASSES *******************
# Johnny's tasks: clearing, town, and city
# Joel's Tasks: camps/tents, find girl, meet love interest, tree canopy 
# Alex's tasks: variables?
# Allison's tasks: middle of forest, stream (water collection), and wise man
# experience, each new location entered will give experience (ex. 8 points of exp)
# items will also give a bit of experience (ex. 1-2 points of exp)
# 
class Location: 
    def __init__(self, name=None, description=None, objects=None, paths=None, visited=None, npcs=None, key=None ):
        self.name = name
        self.description = description
        self.objects = objects
        self.paths = paths
        self.npcs = npcs
        self.visited= visited
        # self.key = key

# class MainCharacter: 
class MainCharacter: 
  def __init__(self, name=None, items=[], type=None, description=None, location=None, health=None, hydration=None, nutrition=None):
    self.name = name
    self.items = items 
    self.health = health
    self.hydration = hydration 
    self.nutrition = nutrition
# class SideCharacter: 
class SideCharacter: 
  def __init__(self, name=None, description=None,           advice=None, location=None, type=None): 
    self.name = name
    self.description = description
    self.advice = advice
    self.location = location
    self.type = type

# class Item:  
# food can increase your health and nutrition, 
# water purifier at the water stream once to survive at least once
class Item:
    def __init__(self, name=None, healthValue=None, hydrationValue=None, nutritionValue=None,location=None):
        self.name = name
        self.healthValue = healthValue
        self.hydrationValue = hydrationValue
        self.nutritionValue = nutritionValue
        self.location = location

# class Enemy: 
class Enemy: 


class Item:
    def __init__(self, name=None, healthValue=None, hydrationValue=None, nutritionValue=None,location=None):
        self.name = name
        self.healthValue = healthValue
        self.hydrationValue = hydrationValue
        self.nutritionValue = nutritionValue
        self.location = location
  
#************** CREATION OF VARIABLES *********************
player = MainCharacter()
player.items = []
player.health = 100
player.hydration = 78
player.nutrition = 85





#****************** START THE GAME ******************
def Start(): 
    global current_room
    print("Welcome to...*game*")
    name = input("What is your name?")
    
    player.name = name
    print("Welcome, " + name)
    print("You can type 'help' to learn how to play")
    # commands: 
    # help -> lists the possible commands a player can do
    # location -> show what room the player is currently in
    # grab -> take an object
    # consume -> drink/eat a food/drink item for consumption
    # look -> show what the surroundings are







# Chance to survival
# res = choices([1,2], weights=[.8, .2])



