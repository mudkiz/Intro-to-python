# Display starting menu
print('Welcome to my dragon text game!') #introduction
print('You must collect all six items including the dragons secret weakness to defeat the dragon!')#Goal
print('You move by typing go north, go south, go west, and go east.')#available commands
print('Type get then the nearby items name to add to your inventory!')#how to put items in inventory
input("Press any key to continue...")#prompt to start
#room set up for the game
rooms = {
    'Entrance': {'North': 'Main Corridor',},
    'Main Corridor': {'South': 'Entrance', 'West': 'Armory', 'East': 'Living Quarters', 'North': 'Dining Hall', 'Item': 'Shield'},
    'Armory': {'West': 'Training Area', 'East': 'Main Corridor', 'Item': 'Sword'},
    'Training Area': {'East': 'Armory', 'Item': 'Secret'},
    'Living Quarters': {'East': 'Officers Quarters', 'West': 'Main Corridor', 'Item': 'Armor'},
    'Officers Quarters': {'West': 'Living Quarters', 'Item': 'Helmet'},
    'Dining Hall': {'South': 'Main Corridor', 'North': 'Gathering Hall', 'Item': 'Two Coconuts'},
    'Gathering Hall': {'South': 'Dining Hall', 'Boss': 'Dragon'}
}
# List to track inventory
inventory = []
# Tracks current room
current_room = "Entrance"
# Tracks last move for display message
msg = ""
# Main loop
while True:
    # Displays what room the player is in and what they have in their inventory
    print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")
    # Display message
    print(msg)
    # Shows items if they are in inventory or nearby
    if "Item" in rooms[current_room].keys():
        nearby_item = rooms[current_room]["Item"]
        if nearby_item not in inventory:
                print(f"You see {nearby_item}")
    # Boss room script
    if "Boss" in rooms[current_room].keys():
        if len(inventory) < 6:
            print(f"You were eaten by the dragon. Game Over.")#if not then lose and break loop
            break
        else:
            print(f"You beat the dragon, congratulations!")#if all 6 items acquired win and break loop
            break
    # Accepts player's move as input
    user_input = input("Enter your move:\n")
    # Splits movement into words
    next_move = user_input.split(' ')
    # Sets first word as the action
    action = next_move[0].title()
    #Sets the second word as the object that the player is grabbing or the direction they are moving
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()
    item = " ".join(item).title()#adds item to inventory
    # Moving between rooms
    if action == "Go":#allows Go to signal movement
        try:#activates the movement command
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"
        except:
            msg = "You cannot move in that direction."#if the player cannot move that way then this tells them their command wont work
    # Picking up items
    elif action == "Get":#sets Get as the action word for picking up an item
        try:
            if item == rooms[current_room]["Item"]:#checks for an item in the current room
                if item not in inventory:#checks if the item is in the inventory
                    inventory.append(rooms[current_room]["Item"])#if item is not in inventory then it will be added
                    msg = f"{item} acquired!"#message showing that the player got the item!
                else:
                    msg = f"You already have the {item}"#if player tries to get an item they already have
            else:
                msg = f"Can't find {item}"#if there is not an item in the room
        except:
            msg = f"Can't find {item}"#fail safe
    elif action == "Exit":#if exit is typed then it breaks the game loop
        break
    # if any commands are typed that are not able to be registered then they are invalid
    else:
        msg = "Invalid command"