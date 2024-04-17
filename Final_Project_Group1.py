alignment = 0
companions = ["Bison","Becky"] 
towns = {"town 1": "Bob's Village",}

# Creates a selection menu for the user.
def print_menu():
    print("\nMain Menu")
    print("1. Start Game")
    print("2. Exit")

# Defining story functions/choices.
def story_1():
    print("\nWith a deep breath,", player_character, "reaches out to the Troika and makes his choice.\nA warm light envelops his hands as the gift of Celestial healing , and whispers of ancient tongues fill his mind, granting him the powers of Mental Manipulation into his being. ")
    print("\n",player_character,"is teleported to a path that  leads him to a village on the brink of despair.\nThe village almost looks like it is in shambles. The eyes or the villages look like they have lost all sense of purpose and hope. A sickness has taken hold, one that no medicine can cure.\nThe villagers eye him fear, ",player_character,"does look pretty scary, perhaps thinking he is a raider.")
    print("1: Seeing that people are in need and wanting to be just and ease their pain use Celestial Healing  to cure the villagers, potentially revealing his divine gifts to all.")
    print("2: Use Mental Manipulation to delve into the villagers’ minds, seeking the source of their affliction and attempting to free them from its grasp.")

def story_2():
    print("\nStory text")
    print("1: 1st option")
    print("2: 2nd option")

def story_3():
    print("\nStory text")
    print("1: 1st option")
    print("2: 2nd option")

def story_4():
    print("\nStory text")
    print("1: 1st option")
    print("2: 2nd option")

def story_5():
    print("\nStory text")
    print("1: 1st option")
    print("2: 2nd option")

# testing alingment system and placeholder for endings
def endings():
    print("\nStory text")
    print("1: lastchoice1")
    print("2: lastchoice2")

while(True):
    print_menu()
    menu_options = input("Select 1 or 2: ")

    # Selects option 1 and asks the user to enter a name.
    if(menu_options == '1'):
        player_character = input("What is your name? ")
        print(player_character)
        break
        
    # Exits the program
    elif(menu_options == '2'):
        exit()
    
    # Catches any input besides 1 or 2 and prompts the user to try again. 
    else:
        print("Invalid input. Try again.")

# Defining 1st story function/choice.

while(True):
    story_1()
    choice_1 = input("Make your choice: ")

    if(choice_1 == '1'):
        alignment =+ 1
        companions.append("Bob")
        print("Bob has joined the party")
        break
    
    elif(choice_1 == '2'):
        alignment =- 1
        towns_removed = towns.pop("town 1")
        print("Bob's town was destroyed")
        break
    elif(choice_1) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")

# Testing alignment changes properly.
print(alignment)
#Second story choice
while(True):
    story_2()
    choice_2 = input("Make your choice: ")

    if(choice_2 == '1'):
        alignment =+ 1
        companions.append("Bill")
        print("Bob has joined the party")#placeholder
        break
    
    elif(choice_2 == '2'):
        alignment =- 1
        towns_removed = towns.pop("town 1")
        print("Bob's town was destroyed")#placeholder
        break
    elif(choice_2) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")

print(alignment)
#Third story choice
while(True):
    story_3()
    choice_3 = input("Make your choice: ")

    if(choice_3 == '1'):
        alignment =+ 1
        companions.append("Ted")
        print("Bob has joined the party")#placeholder
        break
    
    elif(choice_3 == '2'):
        alignment =- 1
        towns_removed = towns.pop("town 1")
        print("Bob's town was destroyed")#placeholder
        break
    elif(choice_3) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")
        
print(alignment)

#Fourth story choice 
while(True):
    story_4()
    choice_4 = input("Make your choice: ")

    if(choice_4 == '1'):
        alignment =+ 1
        companions.append("Tom")
        print("Bob has joined the party")#placeholder
        break
    
    elif(choice_4 == '2'):
        alignment =- 1
        towns_removed = towns.pop("town 1")
        print("Bob's town was destroyed")#placeholder
        break
    elif(choice_4) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")
        
print(alignment)
while(True):
    # ending choice
    endings()
    lastchoice_1 = input("Make your choice: ")

    if(lastchoice_1 == '1'):
            print("Ends the story with chosen 1")

    elif(lastchoice_1 == '2'):
            print("ends the story with chosen story 2")

    # basic alignment check to determine the ending        
    while(True):
        if(alignment == 1):
            print("The world has imploded")
            break
        
        elif(alignment == -1):
            print("The world remains the same")
            break
    break
