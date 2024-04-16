alignment = 0
companions = []
towns = {}

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
        break
    
    elif(choice_1 == '2'):
        alignment =- 1
        break
    else:
        print("Invalid input.")

# Testing alignment changes properly.
print(alignment)
        
