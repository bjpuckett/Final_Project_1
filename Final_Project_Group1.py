alignment = 0
player_character = "Def"
companions = [] 
towns = {"town 1": "Corinth","town 2":"Cathedralis","town 3": "Beezlebub","town 4": "Tom's House","town 5": "Billybob Home"}

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
    print("\nYou leave the village headed East toward the capital city of Cathedralis. The village chief explained that the church called Conclave of Sanctification reigns supreme over the land of Troika.\nThe church originally were worshipers of Plegathon, but slowly began to change, abandoning Plegathon and creating their own God to worship.\nThe Conclave of Sanctification began a holy war against the demi-humans around 13 years ago, deeming them as unholy abominations. The Vatican mercilessly persecutes any non-human species and those who support them.")
    print("\nYour journey to Cathedralis you enter a forest. You have been traveling through the forest for five days.\n You are hating yourself for not asking to take some kind of beast for transportation, you hear a loud commotion. You hear the sound of metal clashing against metal and a frightening scream.\nYou quickly run to inspect what is going on. You surprisingly find yourself at the end of the forest in a beautiful valley. You scan the area and you find what alarmed you.\nYou spot two people engaged in mortal combat. One person is a human, who looks to be dressed in some type of clerical robes bleeding on the ground crawling potentially on the verge of death.\nThe human is crying to you to save him. The other is a being who resembles a large lizard clad in bright red armor. The lizard looks at you and raises his axe prepared to deal a death blow to a defenseless human.")
    print("1:You cast heal on the defenseless human and immediately go into battle. You are remarkably calm about raising your sword towards the intimidating lizard. You remember about the Heroes blessing that Troika gave to you. One of the powers of that blessing called (10,000 Arms) allowed you to learn fighting techniques from 10,000 combat specialists throughout time.  Your weapons clash violently. The lizard is a very capable fighter. It wields the heavy axe as if it were a mere dagger. The lizard's heavy blows are backing you down. He hits you with an overhead strike which you block but the sheer force brings you to take a knee. The lizard raises his axe in preparation to deliver the final blow. As the axe begins its descent you pull out a small dagger and stab the lizard through the food causing the axe to alter its course.\nThe axe hits the ground, and the lizard lets out a loud cry. You stand up and stab the lizard killing it. You cast heal on yourself and the priestly-looking figure.",)
    print("2:You cast Mental Manipulation on the lizard seeking to gain more information because you realize sometimes things are not always what they seem. Confused that he can hear your thoughts lowers his axe.\nYou learn that the man before you is an inquisitor of the Conclave of Sanctification who has just murdered an entire village of demi-humans unprovoked.\nThe lizard had been tracking him when he finally caught up with him in the valley you see. Peering into the inquisitor's mind you confirm all that the lizard said was true and more. Such horrific atrocities the inquisitor committed in the name of the Vatican and Beezlebub. You nod to the lizard and with a giant swing of his axe, splits the inquisitor in half.")

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
        if player_character.strip():  # Check if the input is not an empty string after removing leading/trailing spaces
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
        alignment += 1
        companions.append("Bob")
        print("Bob has joined the party")
        break
    
    elif(choice_1 == '2'):
        alignment -= 1
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
        alignment += 1
        companions.append("Damien")
        print("You learn that the priest is a warrior for the church called an inquisitor. He was heading to the capital city when he was attacked by the lizard. He tells you his name is Damien and joins you as you head toward the capital city Cathedralis")
        break
    
    elif(choice_2 == '2'):
        alignment -= 1
        companions.append("Talon")
        print("The lizard tells you his name is Talon and joins you on your quest as you head towards Cathedralis")#placeholder
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
        alignment += 1
        companions.append("Ted")
        print("Bob has joined the party")#placeholder
        break
    
    elif(choice_3 == '2'):
        alignment -= 1
        towns_removed = towns.pop("town 3")
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
        alignment += 1
        companions.append("Tom")
        print("Bob has joined the party")#placeholder
        break
    
    elif(choice_4 == '2'):
        alignment -= 1
        towns_removed = towns.pop("town 4")
        print("Bob's town was destroyed")#placeholder
        break
    elif(choice_4) == "exit": #option to exit
        exit()
    else:
        print("Invalid input.")
        
print(alignment)

#Fifth story choice 
while(True):
    story_5()
    choice_5 = input("Make your choice: ")

    if(choice_5 == '1'):
        alignment += 1
        companions.append("Billybob")
        print("Bob has joined the party")#placeholder
        break
    
    elif(choice_5 == '2'):
        alignment -= 1
        towns_removed = towns.pop("town 5")
        print("Bob's town was destroyed")#placeholder
        break
    elif(choice_5) == "exit": #option to exit
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

    elif(lastchoice_1) == "exit": #option to exit
        exit()

    # basic alignment check to determine the ending        
    while(True):
        if(alignment == 1):
            print("The world has imploded")
            break
        
        elif(alignment == -1):
            print("The world remains the same")
            break
    break
