#************************************************************
# CHOOSE YOUR OWN ADVENTURE GAME - YOUR NEW DESTINY
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

input_message = "Welcome to ..."
game_running = True # 
input_message = ""
current_location = None
name = ""
locations = []




#************** DEFINE CLASSES *******************
# Johnny's tasks: clearing, town, and city
# Alex's Tasks: camps/tents, find love interest, meet love interest, cave
# Joel's tasks: variables?
# Allison's tasks: middle of forest, stream (water collection), and wise man
# experience, each new location entered will give experience (ex. 8 points of exp)
# items will also give a bit of experience (ex. 1-2 points of exp)
# 
class Location: 
  def __init__(self, name=None, description=None, items=None, paths=None, visited=None, npcs=None, subLocations=None):
    self.name = name
    self.description = description
    self.items = items
    self.paths = paths # where you can go from this current location (a list [])
    self.npcs = npcs
    self.visited= visited
    self.subLocations = subLocations
        # self.key = key
class subLocation: 
  def __init__(self, name=None, description=None, items=None, npcs=None, belongingTo=None):
    self.name = name  
    self.description = description
    self.items = items
    self.npcs = npcs 
    self.belongingTo = belongingTo 
    # must return back to the location it belongs to
  # hide the love interest here!
  
# class MainCharacter: 
class MainCharacter: 
  def __init__(self, name=None, items=[], type="main character", description=None, location=None, health=None, hydration=None, nutrition=None, attackValue=None, experienceValue=none):
    self.name = name
    self.items = items 
    self.description = description 
    self.location = location
    self.health = health
    self.hydration = hydration 
    self.nutrition = nutrition
    self.attackValue = attackValue
    self.experienceValue = experienceValue
# class SideCharacter: 
class NPCs: 
  # specifications for the two types of NPCS:
  # Side Characters (non-harmful):
  #  will have advice
  # Enemies - Monsters (harmful): 
  def __init__(self, name=None, description=None, location=None, subLocation=None, advice=None, attackValue=None, type=None):
    self.name = name
    self.description = description
    self.location = location
    self.subLocation = subLocation
    self.advice = advice
    self.attackValue = attackValue
    self.type = type # specify whether a side character or an enemy

    
# class SideCharacter: 
#   def __init__(self, name=None, description=None, advice=None, location=None, subLocation=None, type=None): 
#     self.name = name
#     self.description = description
#     self.advice = advice
#     self.location = location
#     self.subLocation = subLocation
#     self.type = type 
# # class Enemy: 
# class Enemy: 
#   def __init__(self, name=None, description=None, location=None, subLocation=None, attackValue=None):
#   self.name = name
#   self.description = description
#   self.location = location
#   self.subLocation = subLocation
#   self.attackValue = attackValue
# class Item:  
    # food can increase your health and nutrition, 
    # water purifier at the water stream once to survive at least once

class Item: 
  def __init__(self, name=None, type=None, location=None, subLocation=None, healthValue=None, hydrationValue=None, nutritionValue=None, experienceValue=None, attackValue=None): 
    self.name = name
    self.type = type 
    # weapons - increases attackValue of character
    # consumables - increases healthValue, hydrationValue, nutritionalValue, etc
    self.location = location
    self.subLocation = subLocation
    # for consumables only
    self.healthValue = healthValue
    self.hydrationValue = hydrationValue
    self.nutritionValue = nutritionValue
    self.experienceValue = experienceValue
    self.attackValue = attackValue
#************** CREATION OF VARIABLES *********************

# starting values 

### MAIN CHARACTER ### 
    
player = MainCharacter()
player.items = []
player.health = 100
player.hydration = 78
player.nutrition = 85

### SIDE CHARACTERS ### 3

loveInterest = NPCs()
loveInterest.name = "Your Love Interest"
loveInterest.type = "Side Character" ;
loveInterest.location = "field with flowers"
loveInterest.advice = "'Hey...I'm Olive. Nice to meet you.' Warm eyes stare into yours and a smile graces your face. You finally feel at peace."

wiseMan = NPCs() 
wiseMan.name = "Wise Man"
wiseMan.type = "Side Character"
wiseMan.location = "hollow tree stump"
wiseMan.advice = "'I've been asleep for a while haven't I?' he pauses. 'I came from just around the riverbend a couple of years ago' he looks around at the large tree behind him. 'This is my tree hollow. You're welcome to stay, but I don't have any food to share. It's hard enough to come by now that I'm getting older and my traps are becoming less effective.' A small looking raccoon-dog scampers to his side. 'This is Jengo!' He smiles. 'Jengo has stuck by me for the last couple of months after I found him as a runt.' He mumbles something that you can't quite make out, and guffaws wholehartedly then promptly starts hacking and coughing. You smile and laugh along awkwardly. 'You need advice, soldier?' he states, boring into your eyes with his electric blue ones. You're suprised he can still make out your army uniform with all the dirt caked on. 'Be careful, and watch out for the monsters. Oh, and remember to hydrate' This makes you uneasy. You know riverwater can be deadly and you have the only water purifier for miles. You smile, and say 'Ok'. You turn to leave, and he says an old AKSA saying you distinctly remember hushed whispers about from your childhood:'May your prayers be heard by your people and may you forever feel at peace.' He salutes you the traditional AKSA way, and makes his way back into the hollow before you can reply with the expected response, 'And you, much fortune'."

### ENEMIES ###

enemy1 = NPCs()
enemy1.name = "GENDOM wolf"
enemy1.description = "An abnoramlly large deadly mammal"
enemy1.type = "Enemy"
enemy1.location = "forest near the camp"
enemy1.attackValue = 5.0

enemy2 = NPCs()
enemy2.name = ""
enemy2.description = ""
enemy2.type = "Enemy"
enemy2.location = ""
enemy2.attackValue = 0.0

enemy3 = NPCs()
enemy3.name = ""
enemy3.description = ""
enemy3.type = "Enemy"
enemy3.location = ""
enemy3.attackValue = 0.0

enemy4 = NPCs()
enemy4.name = ""
enemy4.description = ""
enemy4.type = "Enemy"
enemy4.location = ""
enemy4.attackValue = 0.0

enemy5 = NPCs()
enemy5.name = ""
enemy5.description = ""
enemy5.type = "Enemy"
enemy5.location = ""
enemy5.attackValue = 0.0

enemy6 = NPCs()
enemy6.name = ""
enemy6.description = ""
enemy6.type = "Enemy"
enemy6.location = ""
enemy6.attackValue = 0.0

enemy7 = NPCs()
enemy7.name = ""
enemy7.description = ""
enemy7.type = "Enemy"
enemy7.location = ""
enemy7.attackValue = 0.0

enemy8 = NPCs()
enemy8.name = ""
enemy8.description = ""
enemy8.type = "Enemy"
enemy8.location = ""
enemy8.attackValue = 0.0

enemy9 = NPCs()
enemy9.name = ""
enemy9.description = ""
enemy9.type = "Enemy"
enemy9.location = ""
enemy9.attackValue = 0.0


stream = Location()
stream.name = "Stream"
stream.description ="You come across a stream."
stream.items = ["raw water"]
stream.paths = ["Middle Of Forest"]

middle_of_forest = Location()
middle_of_forest.name = "middle of forest"
middle_of_forest.description = "You look around at your surroundings. There's trees on every side of you. You can go in all 4 directions."
middle_of_forest.items = ["mushrooms" , "wild okra" , "katniss" , "wild onions", "potatoes"]
middle_of_forest.paths = ["stream" , "hollow tree stump" , "camp" , "clearing"]
middle_of_forest.npcs = []


city = Location()
city.name = ""
city.description = ""
city.items = [""]
city.paths = ["town"]
city.npcs = [""]


town = Location()
town.name = ""
town.description = ""
town.items = [""]
town.paths = ["city" , "clearing"]
town.npcs = [""]

## Location Wise Man(advice) ##
wise_man = Location()
wise_man.name= "wise man"
wise_man.description =""
wise_man.items = [""]
wise_man.paths =["middle_of_forest", "camp", "field"]
wise_man.npcs = []
wise_man.visited = False

## Location Stream ##
stream = Location()
stream.name= "stream"
stream.description =""
stream.items = [""]
stream.paths =["middle_of_forest", "camp", "field"]
stream.npcs = []
stream.visited = False

# subLocation for Stream(hill)
hill = subLocation()
hill.name= "tent"
hill.description =""
hill.items = ["Knife","Lighter","Bandaid"]
hill.npcs = []
hill.belongingTo = ["camp"]

## Location CAMP ##
camp = Location()
camp.name= "camp"
camp.description ="As you walk further through the forest, you stumble upon a deserted camp. You are too weakened to be concerned by the potential of danger to ponder why it might be there. What do you choose to explore in the camp area?"
camp.items = ["Tent","Axe"]
camp.paths =["tent", "camp area", "forest near camp", "cave", "middle forest", "hollow tree stump"]
camp.npcs = []
camp.visited = False

# subLocation for CAMP(tent)
tent = subLocation()
tent.name= "tent"
tent.description ="You hesitantly step into the abandoned tent. A dusty musk tickles your nostrils--it smells faintly of dried blood. The air is thick with your uncertainty and you strive to avoid the humidity by covering your mouth and nose with your shirt. You look to see what might be useful to you."
tent.items = ["Knife","Lighter","Bandaid"]
tent.npcs = []
tent.belongingTo = ["camp"]

# subLocation for CAMP(camp area)
camp_area = subLocation()
camp_area.name= "camp area"
camp_area.description ="You see a thin trail of smoke floating up from a recently put-out fire. You feel a bit of apprehension. It hasn't been long since the camp's inhabitants were here..."
camp_area.items = ["Wood"]
camp_area.npcs = []
camp_area.belongingTo = ["camp"]

# subLocation for CAMP(forest near the camp) with enemy
forest_near_camp = subLocation()
forest_near_camp.name= "forest near the camp"
forest_near_camp.description ="You exit the camp and walk towards the forest on the other side where you see a GENDOM, or genetically modified, wolf among the trees just 10 feet from the site. It's foaming at the mouth, and you assess that it has probably contracted some uncurable sickness. It snarls at you, it's teeth are stained red and yellow and bits of flesh escape with drool. It looks like it's coming straight for you."
forest_near_camp.items = []
forest_near_camp.npcs = []
forest_near_camp.belongingTo = ["camp"]

## location CAVE(cave) ##
cave = Location()
cave.name= "cave"
cave.description ="You come across a cave opening under a couple of logs in the forest. Sounds of running water can be heard."
cave.items = ["Fish"]
cave.paths ["camp", "field with flowers", "small lake", "stalactites"]
cave.npcs = []
cave.visited = False

# subLocation for CAVE(small lake) with enemy
small_lake = subLocation()
small_lake.name= "small lake"
small_lake.description = "You find a small lake. You peel off your clothes that are caked with mud and wade in, rinsing your body. You see a large, steel-looking fish swimming in the depths"
small_lake.items = ["fish"]
small_lake.npcs = []
small_lake.belongingTo = ["cave"]

# subLocation for CAVE(stalactites)
stalactites = subLocation()
stalactites.name= "stalactites"
stalactites.description = "You enter a small subsection of the cave where there are beautiful stalactites hanging down from the ceiling. They're radiant. They provide you a moment of peace, as you stare up at the beautiful presumably artificially embedded crystals in each. As your gaze turns to the floor, you see a small pile of animal bones. They provide a bit of a warning among the beauty."
stalactites.items = ["Stalactites","Bones"]
stalactites.npcs = []
stalactites.belongingTo = ["cave"]

## location FIELD with flowers(location(FIND love interest)) ##
field = Location()
field.name= "Field with flowers"
field.description =""
field.items = ["Water"]
field.paths =["wise man", "cave", "river", "cottage","edge"]
field.npcs = []
field.visited = False

# subLocation for FIELD(river)
river = subLocation()
river.name= "river"
river.description = ""
river.items = [""]
river.npcs = []
river.belongingTo = ["field"]

# subLocation for FIELD(cottage in the meadow)
cottage = subLocation()
cottage.name= "Cottage in the meadow"
cottage.description = ""
cottage.items = ["First-Aid Kit","Beer","Pork","Katana"]
cottage.npcs = []
cottage.belongingTo = ["field"]

# subLocation for FIELD(edge of a wood)#meeting with love
edge = subLocation()
edge.name= "edge of a wood"
edge.description = ""
edge.items = [""]
edge.npcs = []
edge.belongingTo = ["field"]

### ITEMS ### 

    ## WEAPONS ##
    # Guns: Glock, AK-47, AR-15, Minigun, etc
    # Melee Weapons: Baseball Bat, Knife, Katana, Brass Knuckles, Axe
item1 = Item()
item1.name = "Glock-19"
item1.type = "weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = None
item1.hydrationValue = None
item1.nutritionValue = None
item1.attackValue = 15.0

item1 = Item()
item1.name = "ak-47"
item1.type = "weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 35.0

item1 = Item()
item1.name = "knife"
item1.type = "weapon/tool"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 10.0

item1 = Item()
item1.name = "axe"
item1.type = "weapon/tool"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 10.0


item1 = Item()
item1.name = "chainsaw"
item1.type = "weapon/tool"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 15.0

item1 = Item()
item1.name = "first aid kit"
item1.type = "Healing"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "bow and arrow"
item1.type = "Weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 20.0

item1 = Item()
item1.name = "chicken"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "fish"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "cow"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "baseball bat"
item1.type = "Weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 5.0

item1 = Item()
item1.name = "nectar"
item1.type = "drink"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "wild pig"
item1.type = "food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "pistol"
item1.type = "weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 15.0

# ["mushrooms" , "wild okra" , "katniss" , "wild onions", "potatoes"]
item1 = Item()
item1.name = "mushrooms"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "wild okra"
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.
item1.attackValue = 0.0

item1 = Item()
item1.name = "katniss"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "wild onions"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "potatoes"
item1.type = "Food"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = "sword"
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 20.0

item1 = Item()
item1.name = "grenades"
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.attackValue = 20.0


# self.healthValue = healthValue
#     self.hydrationValue = hydrationValue
#     self.nutritionValue = nutritionValue
#     self.experienceValue = experienceValue
#     self.attackValue = attackValue
    ## CONSUMABLES ## 
    # Food: Burrito, Sandwich, Fish, Pork etc
    # Drinks: Water, Mountain Dew, Beer, Lemonade, etc
    # Medical items: Bandaid, First-Aid Kit, etc

    ## Experience ##
    # Stalactites, Bones, Wood, Tent, Lighter

locations.append()

def check_answer(input): 
  global current_location, input_message, locations, player, game_running
  input_message = input

  if "go" in input_message: 
    message_list = input_message.split(" ")
    message = message_list[1:]

    new_location = " ".join(message)

    if new_location in current_location.paths:
      print("Ok, you can go there!")
    
  elif input_message == "help": 
    print("Here are some commands you can enter...")
    print("go -> head to a location next to this one")
    print("help -> lists the possible commands a player can do")
    print("location -> show what place the player is currently in")
    print("grab -> take an object")
    print("consume -> drink/eat a food/drink item for consumption")
    print("look -> show what the surroundings are")
    print("inventory -> shows what items the character currently has") 
    print("end -> end the game")
    print("make these into message")
          
    # help page *to be filled out*
  elif "location" in input_message: 
    # print the current location that the main character is in
  elif "grab" in input_message: 
    # grab "" should give the character the item that they chose to grab
  elif "consume" in input_message:
    # consume "" should "use up" the item, meaning the item should disappear from their inventory, restoring the corresponding values
  elif "look" in input_message: 

  elif "inventory" in input_message: 

  elif "end" in input_message: 
    # end the game here
    print("Ok... so you don't want to play anymore?")
    print("Alright then... See you next time :(")
    game_running = False
  else:   
    print("Please enter in a valid command!")
  
def prompt_user(): 
  reply = input("What action do you want to perform? >> ")
  return reply
#****************** START THE GAME ******************
def Start(): 
  global current_location 
  global name
  print("Welcome to 'Your New Destiny', Krawfen soldier. You have just betrayed secrets to the AKSA organization, the Krawfen empire's sworn enemy, and they pursue you while you run blindly into the woods located in the outskirts of your town. As you sprint through the vegetation, you look over your shoulder and see that the AKSA's army is falling behind and their shouts start to get quieter and quieter. You hide among the shrubs and bushes on the dirt floor, realizing your pursuers have lost you. A fleeting spark of hope feels like a lit fire in the pit of your stomach. Despite this, you find yourself alone in an expansive forest with nothing but a small pack containing crackers and a water purfier. You don't know what kinds of people and animals you will find in these woods. This used to be a testing site for freak animal combinations. As you peer through the genetically modified pines of 2084, you start to realize the implications of your situation. You are determined to survive.")
  name = input("What is your name, soldier?")
  
  print("Welcome, " + name)
  current_location = middle_of_forest
  print("You can type 'help' to learn how to play")
  print("Think you can find a way to survive in this dying world?")
  while game_running: 
    check_answer(prompt_user())
    # write a function to check the answesr from the user
    
Start()