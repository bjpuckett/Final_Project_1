alignment = 0

while(True):
    # Creates a selection menu for the user
    def print_menu():
        print("\nMain Menu")
        print("1. Start Game")
        print("2. Exit")
    print_menu()
    menu_options = input("Select 1 or 2: ")

    # Selects option 1 and asks the user to enter a name.
    if(menu_options == '1'):
        player_character = input("What is your name? ")
        print(player_character)
        break
        
    # Exits the program
    else:
        break
