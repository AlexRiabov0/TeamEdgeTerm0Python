import random

input_msg ="" #an empty string to hold our user inputs
game_is_on = True #the game loop will depend on this being true
current_room = None #to keep track of where we are
rooms = [] #append any new rooms you create to this list


zombie_img = [
    "           ",
    "  ▄███▄    ", 
    " ▒█████▒   ",
    "▒██░█░██▒  ",
    "▒██▄█▄██▒  ",
    " ▒█   █▒   ", 
    "  ▒█▓█▒    ",
    "           ",
    " ZOMBIE!!! ",
    "           ",    
   
   ]

zombie_img_str = "\n".join(zombie_img)

#print(zombie_img_str)

#******** DEFINE CLASSES *******************
class Room:
    def __init__(self, name=None, description=None, objects=None, paths=None, visited=None, npcs=None, key=None ):
        self.name = name
        self.description = description
        self.objects = objects
        self.paths = paths
        self.npcs = npcs
        self.visited= visited
        self.key = key
      
class Player:
    def __init__(self, name=None, items=[], hit_points=None):
        self.name = name
        self.items = items
        self.hit_points = hit_points

class Item:
    def __init__(self, name=None,type=None, description=None, location=None, power_level=None, special_power=None):
        self.name = name
        self.type = type
        self.description = description
        self.location = location
        self.power_level = power_level
        self.special_power=special_power


class Enemy:
    def __init__(self, type=None, name=None, description=None,  location=None, hit_points=None, weakness=None, image=None):
        self.type = type
        self.name = name
        self.description = description
        self.location = location
        self.hit_points = hit_points
        self.weakness = weakness
        self.image = image

#**********INSTANTIATE OBJECTS ***************
player = Player()
player.items =[]
player.hit_points = 100


kitchen = Room()
kitchen.name = "kitchen"
kitchen.description = "The kitchen is a really nice one! It has all the stuff you need to cook a healthy meal...of zombie parts!l"
kitchen.objects =["potion", "sandwich", "knife"]
kitchen.paths=["living room" , "bathroom" , "backyard" ]
kitchen.npcs = []
kitchen.visited = False
kitchen.key =  ""

bathroom = Room() 
bathroom.name= "bathroom"
bathroom.description ="You are in a Bathroom. Everything is a mess. There is blood on the floor. The shower is still on... "
bathroom.objects = ["towel" , "toothbrush", "toilet paper", "soap"]
bathroom.paths =["kitchen"]
bathroom.npcs = []
bathroom.visited = False
bathroom.key = ""

dining_room = Room()
dining_room.name= "dining room"
dining_room.description ="The dining room is in disarray. There are strange chewing noises coming from under the table."
dining_room.objects = ["letter" , "candle", "camera", "key"]
dining_room.paths =["study", "living room"]
dining_room.npcs = []
dining_room.visited = False
dining_room.key = ""

living_room = Room()
living_room.name= "living room"
living_room.description ="The Living room looks like the dead room. There are half eaten body parts wiggling on the ground. "
living_room.objects = ["forearm" , "lamp", "book", "leg"]
living_room.paths =["dining room", "stairs", "study", "hallway", "basement"]
living_room.npcs = []
living_room.visited = False
living_room.key = ""

stairs = Room()
stairs.name= "stairs"
stairs.description ="The stairs are old and wooden. There are pictures of happy people on the wall. \n Remnants of another time. \n There appears to be more rooms upstaris, but its dark."
stairs.objects = ["family portrait" ]
stairs.paths =["living room", "upstairs hallway"]
stairs.npcs = []
stairs.visited = False
stairs.key = ""

study = Room()
study.name= "study"
study.description ="This looks like a room to study. There is a comfy chair and a desk with a lamp. Pictures of landscapes adorn the walls."
study.objects = ["lamp" ]
study.paths =["living room"]
study.npcs = []
study.visited = False
study.key = ""

brendas_room = Room()
brendas_room.name = "Brenda's room"
brendas_room.description = "Brendas room is dark and humid. You can barely see. The sound of scurrying creatures underfoot makes you anxious."
brendas_room.objects = ["blue bottle" , "diary" ]
brendas_room.paths = ["upstairs hallway"] 
brendas_room.visited = False
brendas_room.npcs=[]
brendas_room.key ="gold key"

upstairs_hallway = Room()
upstairs_hallway.name = "upstairs hallway"
upstairs_hallway.description = "The hallway seems strangely crooked with an window at the end. Looks like a crow flew in and is busy picking over a torso."
upstairs_hallway.objects = []
upstairs_hallway.paths = ["brenda's room" , "master bedroom" , "gilbert's bedroom"] 
upstairs_hallway.visited = False
upstairs_hallway.npcs=[]
upstairs_hallway.key = ""

gilberts_bedroom = Room()
gilberts_bedroom.name = "Gilbert's Bedroom"
gilberts_bedroom.description = "Gilbert was just a kid, so his room is filled with kid things, toys, clothes, books, and ... dead things."
gilberts_bedroom.objects = ["chocolate bar", "science book" ]
gilberts_bedroom.paths = ["brenda's room" , "master bedroom" , "gilbert's bedroom"] 
gilberts_bedroom.visited = False
gilberts_bedroom.npcs=[]
gilberts_bedroom.key= ""

basement = Room()
basement.name = "basement"
basement.description = "The basement is dark, obviously. There are old boxes filled with junk. Grandma was a hoarder. There might be a way out if you look carefully."
basement.objects = ["hammer", "creepy doll" , "bones" ]
basement.paths = ["dungeon" , "living room"] 
basement.visited = False
basement.npcs=[]
basement.key = "green key"

backyard = Room()
backyard.name = "backyard"
backyard.description = "The backyard is overgrown and in need of a gardner. Oh wait, the gardner is there, partially eaten and gargling...."
backyard.objects = ["chainsaw", "hose" , "lawn chair" ]
backyard.paths = ["kitchen"] 
backyard.visited = False
backyard.npcs=[]
backyard.key = ""

dungeon = Room()
dungeon.name = "dungeon"
dungeon.description = "This room is dark and moist. There is a jail cell with a skeleton reading a book. There seems to be a metal door in the back."
dungeon.objects = ["skull", "book" , "shackles" ]
dungeon.paths = ["basement", "exit"] 
dungeon.visited = False
dungeon.npcs=[]
dungeon.key = ""

exit = Room()
exit.name = "exit"
exit.description = "You open the door with much effort and an exit is revealed! There is a long tunnel with light at the end."
exit.objects = []
exit.paths = ["dungeon"] 
exit.visited = False
exit.npcs=[]
exit.key = ""

#add the rooms to the rooms list

# locations.append(city)
# locations.append(town)
# locations.append(middle_of_forest)
# locations.append(clearing)
# locations.append(wise_man)
# locations.append(stream)
# locations.append(camp)
# locations.append(cave)
# locations.append(field)

rooms.append(kitchen)
rooms.append(bathroom)
rooms.append(living_room)
rooms.append(dining_room)
rooms.append(backyard)
rooms.append(basement)
rooms.append(dungeon)
rooms.append(exit)
rooms.append(study)
rooms.append(gilberts_bedroom)
rooms.append(brendas_room)
rooms.append(stairs)
rooms.append(upstairs_hallway)

#************* Make Zombies!!  *************************
zombie_1 = Enemy()
zombie_1.name = "Grandpa Zombie"
zombie_1.type = "Zombie"
zombie_1.description = "Grandpa Zombie has seen better days! He is hungry and will not listen to reason."
zombie_1.hit_points = 10
zombie_1.location = ""
zombie_1.weakness = ["chainsaw", "hammer"]

#************* HIDE ZOMBIE ******************
zombie_1.location = random.choice(rooms)
while zombie_1.location.name == "kitchen":
    zombie_1.location = random.choice(rooms)

#print(zombie_1.location.name)


#********** GAMEPLAY FUNCTIONS **********
def prompt_user():
     
    if game_is_on is False: #makes sure we don't re-prompt after we die
        print("Game Over")
         
        return
    reply = input("What do you want to do?  >>  ")

    return reply

def check_answer(input):
  global current_room, input_msg, rooms, player, game_is_on

  input_msg = input

  #GO
  if "go" in input_msg:
    #split the string into two arguments
    msg_array  = input_msg.split(" ")

    msg = msg_array[1:] #get every element after the first, in case multi-word input

    new_room = " ".join(msg)  # make a new string by joining the elements of the input array

    if new_room in current_room.paths:
        print("Yes you can go there")

        for room in rooms:  #Make challenge!!!!
            if room.name.lower() == new_room.lower():
            #set the current room by grabbing its index
                index = rooms.index(room)
                current_room = rooms[index]
                
        if current_room.name.lower() == "exit":
            print(current_room.description)
            print("You managed to escape without being eaten!! Thanks for playing!")
            game_is_on = False #end the game
            exit

        if new_room.lower()== zombie_1.location.name.lower():
            print(zombie_img_str)
            
            print("Oh no! You have been eaten by " + zombie_1.name)
            print("Thank you for dying...I mean playing.")
            game_is_on = False #end the game
            exit
        else:  
            print("You are now at the : " + current_room.name)
            print(current_room.description)
         


      #find the room that has that "key" new_room as a property
        
        
      
    else:
      print("No you can't go there")
      
  #LOOK          
  elif "look" in input_msg:
      #loop through all the objects and paths and print them out so user can see options
      print("You see the following: ") 

      for object in current_room.objects:
          print(" -  " + object)

      print("From here you can go to: ")

      for path in current_room.paths:
          print(" - " + path)
  #TAKE
  elif "take" in input_msg:
      print("Taking item...")

      items_list  = input_msg.split(" ")
      item = items_list[1:] #get the second element

      item_to_take = " ".join(item)

      #check to see if it is part of the room's inventory..

      if item_to_take in current_room.objects:
          print("Yes you can take this item: " + item_to_take)
          player.items.append(item_to_take) #add to the players items list

          #remove from room
          current_room.objects.remove(item_to_take)

          print("current room items after taking item " + str(current_room.objects))
          print("player has : " + str(player.items))

      else:
          print("No you can't pick that up")

  #NAME
  elif "room" in input_msg:
      print( "You are currently in: " + current_room.name)

  #INVENTORY
  elif "inventory" in input_msg:
      print("you have the following items:")
      for item in player.items:
          print("- " + item)


  #HELP
  elif "help" in input_msg:
      print(''' 
            You can type 'look' to look around and 'go' to follow a path.
            Type 'take' to grab an object
            Type 'room' to see what room you are in

             ''')
      
  elif input_msg == None:
      print(" input: " + input_msg)
        
      input_msg = input("What do you want to do? You can type 'help' for commands to use >>> ")
      
  else:
      print(" I don't understand that.")

#****************** START THE GAME ******************
def start():
    global current_room

    print("Welcome to...zombie manor")
 
    

    name = input("What is your name, player? ")
    player.name = name
    print("Welcome, " + name)
    print("You can type 'help' to learn how to play")

  #begin at the kitchen
    current_room = kitchen

    print("You are in a kitchen and everything looks normal. The air smells like death")
    print("Think you can escape this house before being eaten by a zombie? Try to find a way out.")
    #******* MAIN GAME LOOP
    while(game_is_on):
        check_answer(prompt_user()) #this makes the game continously prompt and check response


start()