alignment = 0
companions = ["Bison","Becky"] 
towns = {"town 1": "Bob's Village",}

# Creates a selection menu for the user.
def print_menu():
    print("\nMain Menu")
    print("1. Start Game")
    print("2. Exit")

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
        break
    
    # Catches any input besides 1 or 2 and prompts the user to try again. 
    else:
        print("Invalid input. Try again.")

# Defining 1st story function/choice.
def story_1():
    print("\nStory text")
    print("1: 1st option")
    print("2: 2nd option")

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
    else:
        print("Invalid input.")

# Testing alignment changes properly.
print(alignment)

# testing alingment system and placeholder for endings
def endings():
    print("\nStory text")
    print("1: lastchoice1")
    print("2: lastchoice2")

while(True):
    endings()
    lastchoice_1 = input("Make your choice: ")

    if(lastchoice_1 == '1'):
            print("Ends the story with chosen 1")

    elif(lastchoice_1 == '2'):
            print("ends the story with chosen story 2")

    # basic alignment check to determine ending        
    while(True):
        if(alignment == 1):
            print("The world has imploded")
            break
        
        elif(alignment == -1):
            print("The world remains the same")
            break
    break
    

        
