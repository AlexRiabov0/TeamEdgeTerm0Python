#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/


active = True
item = "orange"
welcome_message = "Hi! I'm your shopping assistant. What can I add or remove from your shopping list? \n"

print("Welcome to Shopping List!")
print(welcome_message)


#-->Todo: declare a shopping_list list
shopping_list = ["milk" , "eggs" , "flour" , "orange"]

def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")

    return reply

def check_answer(ans):
    if item in shopping_list:
        remove_item(item)
    else:
        add_item()

def add_item():
#this function can take in a string and store it in an array
    pass
    shopping_list.append(item)

def remove_item():
    shopping_list.remove(item)

while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True