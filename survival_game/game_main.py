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

from time import sleep

input_message = "" #empty string for user inputs
game_running = True # 
input_message = ""
current_location = None
name = ""
locations = []
knapsack = ["crackers" , "water purifier"]


#************** DEFINE CLASSES *******************
# Johnny's tasks: clearing, town, and city
# Alex's Tasks: camps/tents, find love interest, meet love interest, cave
# Joel's tasks: variables
# Allison's tasks: middle of forest, stream (water collection), and wise man
# experience, each new location entered will give experience (ex. 8 points of exp)
# items will also give a bit of experience (ex. 1-2 points of exp)
# 
class Location: 
  def __init__(self, name=None, description=None, items=None, paths=None, visited=None, npcs=None):
    self.name = name
    self.description = description
    self.items = items
    self.paths = paths # where you can go from this current location (a list [])
    self.npcs = npcs
    self.visited= visited
        # self.key = key
# class subLocation: 
#   def __init__(self, name=None, description=None, items=None, npcs=None, belongingTo=None):
#     self.name = name  
#     self.description = description
#     self.items = items
#     self.npcs = npcs 
#     self.belongingTo = belongingTo 
    # must return back to the location it belongs to
  # hide the love interest here!
  
# class MainCharacter: 
class MainCharacter: 
  def __init__(self, name=None, items=[], type="main character", description=None, location=None, health=None, hydration=None, nutrition=None, attackValue=None, experienceValue=None):
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
player.hydration = 75
player.nutrition = 85
player.attackValue = 0
player.experienceValue = 0

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
wiseMan.advice = "'I've been asleep for a while haven't I?' he pauses. 'I came from just around the riverbend a couple of years ago' he looks around at the large tree behind him. 'This is my tree hollow. You're welcome to stay, but I don't have any food to share. It's hard enough to come by now that I'm getting older and my traps are becoming less effective.' A small looking raccoon-dog scampers to his side. 'This is Jengo!' He smiles. 'Jengo has stuck by me for the last couple of months after I found him as a runt.' He mumbles something that you can't quite make out, and guffaws wholehartedly then promptly starts hacking, coughing up blood. You smile and laugh along awkwardly. 'You need advice, soldier?' he states, boring into your eyes with his electric blue ones. You're suprised he can still make out your army uniform with all the dirt caked on. 'Be careful, and watch out for the monsters. Oh, and remember to hydrate' This makes you uneasy. You know riverwater can be deadly and you have the only water purifier for miles. You smile, and say 'Ok'. You turn to leave, and he says an old AKSA saying you distinctly remember hushed whispers about from your childhood:'May your prayers be heard by your people and may you forever feel at peace.' He salutes you the traditional AKSA way, and makes his way back into the hollow before you can reply with the expected response, 'And to you, much fortune'."

### ENEMIES ###

enemy1 = NPCs()
enemy1.name = "GENDOM wolf"
enemy1.description = "An abnoramlly large deadly mammal"
enemy1.type = "Enemy"
enemy1.location = "forest near the camp"
enemy1.attackValue = 5.0

enemy2 = NPCs()
enemy2.name = "goblins"
enemy2.description = "a wandering sprite that is usually mischievous but often malicious"
enemy2.type = "Enemy"
enemy2.location = ""
enemy2.attackValue = 5.0

enemy3 = NPCs()
enemy3.name = "aliens"
enemy3.description = "a species coming from a different planet"
enemy3.type = "Enemy"
enemy3.location = ""
enemy3.attackValue = 10.0

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



## Location Town ##(END OF GAME)
city = Location()
city.name= "city"
city.description ="Congratulations! You have reached the city!! You've won the game!"
city.items = []
city.paths = ["town"]
city.npcs = []
city.visited = False

## Location Town ##
town = Location()
town.name= "town"
town.description ="You come across a small town in the middle of nowhere. There are small cobblestones lining the pathway up to the largest building, which looks like a pub. You are inclined to walk in, but are a little nervous. Do you choose to go into the pub?"
town.items = ["old_toyota"]
town.paths = ["city", "clearing","pub" , "alexs_pub" , "allisons_farm" , "joel_grave" , "johnny_it_center"]
town.npcs = []
town.visited = False

# subLocation for Town(alexs_pub)
alexs_pub = Location()
alexs_pub.name= "alex's pub"
alexs_pub.description ="You walk into Alex's Pub, which a large sign on the door announced. You sit at a bench and ask for a drink from the bartender. They give you a bit of a side-eye, but they don't say anything. Maybe there have been bounties put on your head from the Krawden empire--maybe it's because you're dripping mud around the bar. You sigh and watch people around you, glad to finally be back in civilization."
alexs_pub.items = ["martini","whisky","beer"]
alexs_pub.npcs = []
alexs_pub.belongingTo = ["town"]

# subLocation for Town(allisons_farm)
allisons_farm = Location()
allisons_farm.name= "allison's farm"
allisons_farm.description ="You see some animals around a small-ish looking farm. You want to steal one for companionship. These animals don't look like they're GENMODs--they're familiar. You see chickens, cows and a pig. You're having a tough decision choosing which to pick."
allisons_farm.items = ["chickens","cows","pig"]
allisons_farm.npcs = []
allisons_farm.paths = ["town"]

# subLocation for Town(joel_grave)
joel_grave = Location()
joel_grave.name= "joel's grave"
joel_grave.description ="You pass a graveyard in the town. The largest grave is a clear whitish stone with polished letters. 'This must have been a mayor, or someone important,' you think to yourself. You read the grave which reads, 'beware'. Before you turn to leave, you see a small handgun glinting, buried in the grass next to the grave"
joel_grave.items = ["glock_19"]  
joel_grave.npcs = []
joel_grave.paths = ["town"]

# subLocation for Town(johnny_it_center)
johnny_it_center = Location()
johnny_it_center.name= "johnny's it center"
johnny_it_center.description ="There's a building that looms over the town, a pure white and grey box. You see an engraved emblem on the door that says 'Johnny's IT center'. You try to open the door but it won't budge. The box gives you an apprehensive feeling."
johnny_it_center.items = [""]
johnny_it_center.npcs = []
johnny_it_center.paths = ["town"]

## Location Middle_of_forest ##
middle_of_forest = Location()
middle_of_forest.name = "middle_of_forest"
middle_of_forest.description = "You look around at your surroundings. There's trees on every side of you. You can go in all 4 directions."
middle_of_forest.items = ["mushrooms" , "wild okra" , "katniss" , "wild onions", "potatoes"]
middle_of_forest.paths = ["stream" , "wise_man" , "camp" , "clearing"]
middle_of_forest.npcs = []

## Location Clearing ##
clearing = Location()
clearing.name= "clearing"
clearing.description ="You walk from the forest into a clearing. You're starting to get hungry again. You sigh at the sight of open grass, knowing that the Krawden soldiers have long given up. They wouldn't care about losing a single soldier because of the sheer number of them."
clearing.items = ["old tools", "plastic trash"]
clearing.paths =["middle_of_forest", "town", "route","excavation"]
clearing.npcs = []
clearing.visited = False

# subLocation for Clearing(route) with enemy
route = Location()
route.name= "route"
route.description =""
route.items = []
route.npcs = []
route.paths = ["clearing"]

# subLocation for Clearing(excavation)
excavation = Location()
excavation.name= "excavation"
excavation.description ="In exiting the clearing, you come across an excavation site. You realize that this must have been an abandoned mine from earlier in the century. You look around for anything useful and find a shovel. Do you choose to pick it up?"
excavation.items = ["Shovel" , "Gold"]
excavation.npcs = []
excavation.paths = ["clearing"]

## Location Wise Man(advice) ##
wise_man = Location()
wise_man.name= "wise_man"
wise_man.description = "'I've been asleep for a while haven't I?' he pauses. 'I came from just around the riverbend a couple of years ago' he looks around at the large tree behind him. 'This is my tree hollow. You're welcome to stay, but I don't have any food to share. It's hard enough to come by now that I'm getting older and my traps are becoming less effective.' A small looking raccoon-dog scampers to his side. 'This is Jengo!' He smiles. 'Jengo has stuck by me for the last couple of months after I found him as a runt.' He mumbles something that you can't quite make out, and guffaws wholehartedly then promptly starts hacking, coughing up blood. You smile and laugh along awkwardly. 'You need advice, soldier?' he states, boring into your eyes with his electric blue ones. You're suprised he can still make out your army uniform with all the dirt caked on.'Be careful, and watch out for the monsters. Oh, and remember to hydrate' This makes you uneasy. You know riverwater can be deadly and you have the only water purifier for miles. You smile, and say 'Ok'. You turn to leave, and he says an old AKSA saying you distinctly remember hushed whispers about from your childhood:'May your prayers be heard by your people and may you forever feel at peace.' He salutes you the traditional AKSA way, and makes his way back into the hollow before you can reply with the expected response, 'And to you, much fortune'."
wise_man.items = []
wise_man.paths =["middle_of_forest", "camp", "field"]
wise_man.npcs = []
wise_man.visited = False

## Location Stream ##
stream = Location()
stream.name= "stream"
stream.description ="You come across a stream. The water looks murky, but you're too parched to care. You can hardly wait to collect some."
stream.items = ["raw water"]
stream.paths =["middle_of_forest", "hill", "field"]
stream.npcs = []
stream.visited = False

# subLocation for Stream(hill)
hill = Location()
hill.name= "hill"
hill.description =""
hill.items = ["rabbit","Stick"]
hill.npcs = []
hill.paths = ["stream"]

## Location CAMP ##
camp = Location()
camp.name= "camp"
camp.description ="As you walk further through the forest, you stumble upon a deserted camp. You are too weakened to be concerned by the potential of danger to ponder why it might be there. What do you choose to explore in the camp area?"
camp.items = ["Tent","Axe"]
camp.paths =["tent", "camp area", "forest_near_camp", "cave", "middle_of_forest", "hollow tree stump"]
camp.npcs = []
camp.visited = False

# subLocation for CAMP(tent)
tent = Location()
tent.name= "tent"
tent.description ="You hesitantly step into the abandoned tent. A dusty musk tickles your nostrils--it smells faintly of dried blood. The air is thick with your uncertainty and you strive to avoid the humidity by covering your mouth and nose with your shirt. You look to see what might be useful to you."
tent.items = ["Knife","Lighter","Bandaid"]
tent.npcs = []
tent.paths = ["camp"]

# subLocation for CAMP(camp area)
camp_area = Location()
camp_area.name= "camp area"
camp_area.description ="You see a thin trail of smoke floating up from a recently put-out fire. You feel a bit of apprehension. It hasn't been long since the camp's inhabitants were here..."
camp_area.items = ["Wood", "Chainsaw"]
camp_area.npcs = []
camp_area.paths = ["camp"]

# subLocation for CAMP(forest near the camp) with enemy
forest_near_camp = Location()
forest_near_camp.name= "forest near the camp"
forest_near_camp.description ="You exit the camp and walk towards the forest on the other side where you see a GENDOM, or genetically modified, wolf among the trees just 10 feet from the site. It's foaming at the mouth, and you assess that it has probably contracted some uncurable sickness. It snarls at you, it's teeth are stained red and yellow and bits of flesh escape with drool. It looks like it's coming straight for you."
forest_near_camp.items = []
forest_near_camp.npcs = []
forest_near_camp.paths = ["camp"]

## location CAVE(cave) ##
cave = Location()
cave.name= "cave"
cave.description ="You come across a cave opening under a couple of logs in the forest. Sounds of running water can be heard."
cave.items = ["Brass Knuckles"]
cave.paths = ["camp", "field", "small_lake", "stalactites"]
cave.npcs = []
cave.visited = False

# subLocation for CAVE(small lake) with enemy
small_lake = Location()
small_lake.name= "small lake"
small_lake.description = "You find a small lake. You peel off your clothes that are caked with mud and wade in, rinsing your body. You see a large, steel-looking fish swimming in the depths"
small_lake.items = ["Fish", "AK-47"]
small_lake.npcs = []
small_lake.paths = ["cave"]

# subLocation for CAVE(stalactites)
stalactites = Location()
stalactites.name= "stalactites"
stalactites.description = "You enter a small subsection of the cave where there are beautiful stalactites hanging down from the ceiling. They're radiant. They provide you a moment of peace, as you stare up at the beautiful presumably artificially embedded crystals in each. As your gaze turns to the floor, you see a small pile of animal bones. They provide a bit of a warning among the beauty."
stalactites.items = ["Stalactites","Bones"]
stalactites.npcs = []
stalactites.paths = ["cave"]

## location FIELD with flowers(location(FIND love interest)) ##
field = Location()
field.name= "Field with flowers"
field.description ="You explore a local field that is covered with gorgeous flowers. You spot a purple dailip, a mutated tulip-daisy that has short petals that curl up towards the sun, along with a crysanthellysum, a chrysanthemum-alyssum creation. The tiny buds with large amounts of petals cover the ground between taller flowers. You know better than to pick either of them, though. Barbed thorns cover each stem. Their inventors wanted the beautiful plants to be weaponized, like virtually everything else in the forest."
field.items = ["Water", "Nectar"]
field.paths =["wise_man", "cave", "river", "cottage","edge"]
field.npcs = []
field.visited = False

# subLocation for FIELD(river)
river = Location()
river.name= "river"
river.description = "Following the sound of running water, you approach a clear blue river with angel fish and reeds. You stop to fill your canteen and purify it."
river.items = ["Pistol", "Bow and Arrow"]
river.npcs = []
river.paths = ["field"]

# subLocation for FIELD(cottage in the meadow)
cottage = Location()
cottage.name= "Cottage in the meadow"
cottage.description = "You approach a small, abandoned looking cottage. Inside, you find some food and a knife. 'Someone definitely lives here', you think to yourself."
cottage.items = ["First-Aid Kit","Beer","Pig","Katana"]
cottage.npcs = []
cottage.paths = ["field"]

# subLocation for FIELD(edge of a wood)#meeting with love
edge = Location()
edge.name= "edge of a wood"
edge.description = "The woods give way to a large and empty ocean basin. You stare off the cliff at the expanse of dirt and sweet-smelling adapted kelp. Your thoughts travel to existentialism"
edge.items = ["Baseball Bat"]
edge.npcs = []
edge.paths = ["field"]

# Adding locations

locations.append(city)
locations.append(town)
locations.append(middle_of_forest)
locations.append(clearing)
locations.append(wise_man)
locations.append(stream)
locations.append(camp)
locations.append(cave)
locations.append(field)

### ITEMS ### 

    ## WEAPONS ##
    # Guns: Glock-19, AK-47, AR-15, Minigun, etc
    # Melee Weapons: Baseball Bat, Knife, Katana, Brass Knuckles, Axe, Shovel
item1 = Item()
item1.name = "glock_19"
item1.type = "weapon"
item1.location = ""
item1.healthValue = None
item1.hydrationValue = None
item1.nutritionValue = None
item1.attackValue = 15.0

item2 = Item()
item2.name = "ak_47"
item2.type = "weapon"
item2.location = ""
item2.healthValue = 0.0
item2.hydrationValue = 0.0
item2.nutritionValue = 0.0
item2.attackValue = 35.0

item3 = Item()
item3.name = "knife"
item3.type = "weapon/tool"
item3.location = ""
item3.healthValue = 0.0
item3.hydrationValue = 0.0
item3.nutritionValue = 0.0
item3.attackValue = 10.0

item4 = Item()
item4.name = "axe"
item4.type = "weapon/tool"
item4.location = ""
item4.healthValue = 0.0
item4.hydrationValue = 0.0
item4.nutritionValue = 0.0
item4.attackValue = 10.0


item5 = Item()
item5.name = "chainsaw"
item5.type = "weapon/tool"
item5.location = ""
item5.healthValue = 0.0
item5.hydrationValue = 0.0
item5.nutritionValue = 0.0
item5.attackValue = 15.0

item6 = Item()
item6.name = "first aid kit"
item6.type = "Healing"
item6.location = ""
item6.healthValue = 30.0
item6.hydrationValue = 0.0
item6.nutritionValue = 0.0
item6.experienceValue = 0.0
item6.attackValue = 0.0

item7 = Item()
item7.name = "bow and arrow"
item7.type = "Weapon"
item7.location = ""
item7.healthValue = 0.0
item7.hydrationValue = 0.0
item7.nutritionValue = 0.0
item7.experienceValue = 0.0
item7.attackValue = 20.0

item8 = Item()
item8.name = "katana"
item8.type = "Weapon"
item8.location = ""
item8.healthValue = 0.0
item8.hydrationValue = 0.0
item8.nutritionValue = 0.0
item8.attackValue = 30.0

item9 = Item()
item9.name = "brass knuckles"
item9.type = "Weapon"
item9.location = ""
item9.healthValue = 0.0
item9.hydrationValue = 0.0
item9.nutritionValue = 0.0
item9.attackValue =15.0

item10 = Item()
item10.name = "chicken"
item10.type = "Food"
item10.location = ""
item10.healthValue = 0.0
item10.hydrationValue = 0.0
item10.nutritionValue = 10.0
item10.attackValue = 0.0

item11 = Item()
item11.name = "fish"
item11.type = "Food"
item11.location = ""
item11.healthValue = 0.0
item11.hydrationValue = 0.0
item11.nutritionValue = 10.0
item11.attackValue = 0.0

item12 = Item()
item12.name = "cows"
item12.type = "Food"
item12.location = ""
item12.healthValue = 0.0
item12.hydrationValue = 0.0
item12.nutritionValue = 5.0
item12.attackValue = 0.0

item13 = Item()
item13.name = "baseball bat"
item13.type = "Weapon"
item13.location = ""
item13.healthValue = 0.0
item13.hydrationValue = 0.0
item13.nutritionValue = 0.0
item13.attackValue = 5.0


item14 = Item()
item14.name = "shovel"
item14.type = "Weapon"
item14.location = ""
item14.healthValue = 0.0
item1.hydrationValue = 0.0
item14.nutritionValue = 0.0
item14.attackValue = 5.0

item15 = Item()
item15.name = "nectar"
item15.type = "drink"
item15.location = ""
item15.healthValue = 5.0
item15.hydrationValue = 10.0
item15.nutritionValue = 0.0
item15.attackValue = 0.0

item16 = Item()
item16.name = "pig"
item16.type = "food"
item16.location = "barn"
item16.healthValue = 0.0
item16.hydrationValue = 0.0
item16.nutritionValue = 10.0
item16.attackValue = 0.0

item17 = Item()
item17.name = "pistol"
item17.type = "weapon"
item17.location = "river"
item17.healthValue = 0.0
item17.hydrationValue = 0.0
item17.nutritionValue = 0.0
item17.attackValue = 15.0

# ["mushrooms" , "wild okra" , "katniss" , "wild onions", "potatoes" "rabbit"]
item18 = Item()
item18.name = "mushrooms"
item18.type = "Food"
item18.location = ""
item18.healthValue = 0.0
item18.hydrationValue = 0.0
item18.nutritionValue = 0.0
item18.attackValue = 10.0

item19 = Item()
item19.name = "wild okra"
item19.type = ""
item19.location = ""
item19.healthValue = 0.0
item19.hydrationValue = 0.0
item19.nutritionValue = 0.
item19.attackValue = 0.0

item20 = Item()
item20.name = "katniss"
item20.type = "Food"
item20.location = ""
item20.healthValue = 0.0
item20.hydrationValue = 0.0
item20.nutritionValue = 0.0
item20.attackValue = 0.0

item21 = Item()
item21.name = "wild onions"
item21.type = "Food"
item21.location = ""
item21.healthValue = 0.0
item21.hydrationValue = 0.0
item21.nutritionValue = 0.0
item21.attackValue = 0.0

item22 = Item()
item22.name = "potatoes"
item22.type = "Food"
item22.location = ""
item22.healthValue = 0.0
item22.hydrationValue = 0.0
item22.nutritionValue = 10.0
item22.attackValue = 0.0

item23 = Item()
item23.name = "rabbit"
item23.type = "Food"
item23.location = ""
item23.healthValue = 0.0
item23.hydrationValue = 0.0
item23.nutritionValue = 10.0
item23.attackValue = 0.0


item24 = Item()
item24.name = "sword"
item24.type = "Weapon"
item24.location = ""
item24.healthValue = 0.0
item24.hydrationValue = 0.0
item24.nutritionValue = 0.0
item24.attackValue = 20.0

item25 = Item()
item25.name = "grenades"
item25.type = "Weapon"
item25.location = ""
item25.healthValue = 0.0
item25.hydrationValue = 0.0
item25.nutritionValue = 0.0
item25.attackValue = 20.0

item26 = Item()
item26.name = "water"
item26.type = "drink"
item26.location = ""
item26.healthValue = 0.0
item26.hydrationValue = 10.0
item26.nutritionValue = 0.0
item26.attackValue = 0.0



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
    # Stalactites, Bones, Wood, Tent, Lighter, "Stick"


def check_answer(input): 
  global current_location, input_message, locations, player, game_running
  input_message = input
  print(
        "Your current stats:\n"
        "Nutrition: " + str(player.nutrition) + "\n" + 
        "Health: " + str(player.health) + "\n" + 
        "Hydration: " + str(player.hydration) + "\n" + 
        "Attack Value: " + str(player.attackValue) + "\n" + 
        "Experience Value: " + str(player.experienceValue)
       )
  # these stats update for each command the player runs
  if player.nutrition <= 0 or player.health <= 0 or player.hydration <= 0: 
    print("Unfortunately, you have died. Game Over!!!")
    game_running = False
  if player.experienceValue >= 100: 
    print("Congratulations! You have demonstrated mastery through your experience level and have won the game")
    game_running = False
  if "go" in input_message: 
    message_list = input_message.split(" ")
    message = message_list[1:]

    new_location = " ".join(message)

    if new_location in current_location.paths:
      print("Ok, you can go there!")
      for location in locations:  #Make challenge!!!!
        if location.name.lower() == new_location.lower():
          #set the current room by grabbing its index
          index = locations.index(location)
          current_location = locations[index]
          print("You are now at the : " + current_location.name)
          
          # return(current_location)
          # end of game(with exp)
      # if current_location == city.name:
      #     game_running = False
       
      print(current_location.description)
    
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
    
          
    # help page *to be filled out*
  elif "location" in input_message: 
    location_exact = input_message.split()
    if location_exact[1] in current_location.paths:
      print("yes, you can go there")
    
    # print the current location that the main character is in
  elif "grab" in input_message:
    print(f"these are items you can use:  {current_location.items}")
    print(input_message)
    items = current_location.items
    for item in items:
      if input_message in item:
        knapsack.append(items[item])
        print(knapsack)
    else:print("Sorry, try to input a valid resource again")
    # grab "" should give the character the item that they chose       to grab 
  elif "consume" in input_message:
    # consume "" should "use up" the item, meaning the item should disappear from their inventory, restoring the corresponding values
    for item in knapsack: 
      if input_message.contains(item.name): 
        # use up the item, delete from inventory
        player.nutrition += item.nutritionValue
        player.hydration += item.hydrationValue
        player.health += item.healthValue
        player.experienceValue += item.experienceValue
        player.attackValue = item.attackValue
        knapsack.remove(item) 
      else: 
        print("You dont have this item in your inventory!")
  elif "look" in input_message: 
    print(f"these are the places you can go:  {current_location.paths}")

  elif "inventory" in input_message: 
    print()
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
  name = input("What is your name, soldier?")
  
  print("Welcome to 'Your New Destiny', Krawfen soldier," + name + ". You have just betrayed secrets to the AKSA organization, the Krawfen empire's sworn enemy, and they pursue you while you run blindly into the woods located in the outskirts of your town.")
  sleep(1)
  print("As you sprint through the vegetation, you look over your shoulder and see that the AKSA's army is falling behind and their shouts start to get quieter and quieter. You hide among the shrubs and bushes on the dirt floor, realizing your pursuers have lost you. A fleeting spark of hope feels like a lit fire in the pit of your stomach.")
  sleep(1)
  print("Despite this, you find yourself alone in an expansive forest with nothing but a small pack containing crackers and a water purfier. You don't know what kinds of people and animals you will find in these woods. This used to be a testing site for freak animal combinations. As you peer through the genetically modified pines of 2084, you start to realize the implications of your situation. You are determined to survive.")
  
  

  current_location = middle_of_forest
  print("You can type 'help' to learn how to play")
  print("Think you can find a way to survive in this dying world?")
  while game_running ==  True: 
    check_answer(prompt_user())
    # write a function to check the answesr from the user




















    
    
Start()
