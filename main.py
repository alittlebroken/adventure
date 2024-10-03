from Locations import *

# Sets the game running
running = True

# Stores the location we are currently in
location = "start"

# The players bag for any items they pick up
player_bag = []

# The slots for a player
player_slots = { "weapon": None }

# Help menu
def help():
    print("You can perform the following commands:")
    print()
    print("q or quit or exit - Leave the game")
    print("help - Display this menu")
    print()
    print("l or look - Describe the area you are in")
    print("t or take <item> - Take an item that the area has")
    print("i or inv or inventory - Show the items you have in your bag")
    print("d or drop <item> - Drop an item to the ground")
    print("e or equip <item> <slot> - Equip an item you have stored in your bag to yourself ( Slots: weapon )")
    print("g or go <direction> - Travel in the direction given ( Can be one of north, south, east or west )")

# Equip an item to the character to be used
def equip_item(item, slot):

    print(player_slots)
    print(item)
    print(slot)

    # Check if wa have the item first
    if item not in player_bag:
        print("You can only equip an item you have placed in your bag")
        return
    
    # Check if the slot for the player is available
    if slot not in player_slots:
        print("The player does not have a slot matching that description")
        return
    
    # Equip the item
    player_slots[slot] = item

    # remove the item from your bag
    player_bag.remove(item)
    return

# Keep looping until the game is own, lost or quit
while running:

    # Get any inut from the player
    command = input("What would you like to do? > ")

    # split the command out for easier parsing
    cmd = command.split(' ')

    # Check what command was inout
    if (cmd[0] == "q" or cmd[0] == "quit" or cmd[0] == "exit"):
        print("Thank you for playing the game. Bye")
        running = False
    elif (cmd[0] == "g" or cmd[0] == "go"):

        # Check we have specified a location to move to
        if len(cmd) <= 1:
            print("You must specify a location to move to")
        else:
            # Attempt to move to the desired location
            location = world.move_to(cmd[1])
    elif (cmd[0] == "help" or cmd[0] == "h"):
        help()
    elif (cmd[0] == "l" or cmd[0] == "look"):
        # Describe the current location we are in
        world.describe()
    elif (cmd[0] == "t" or cmd[0] == "take"):
        item = world.take_item(cmd[1])
        # place the item in the players bag
        player_bag.append(item)
    elif (cmd[0] == "i" or cmd[0] == "inv" or cmd[0] == "inventory"):
        if len(player_bag) > 0:
            print("You are carrying the following items:")
            for item in player_bag:
                print(item)
            print()
        else:
            print("You currently are carrying no items in your bag.")
    elif (cmd[0] == "d" or cmd[0] == "drop"):
        
        # Check if an item has been specified
        if len(cmd) <= 1:
            print("You must supply the name of an item you wish to drop")
        else:
            # Are we carrying that item in the bag?
            if cmd[1] not in player_bag:
                print("You are not carrying that item so you can't drop it")
            else:
                # Remove the item from the players bag
                player_bag.remove(cmd[1])

                # Add the item to the list of items the area has
                world.add_item(location, cmd[1])
    elif (cmd[0] == "e" or cmd[0] == "equip"):
        # Equip the item
        equip_item(cmd[1], cmd[2])

    else:
        print("Sorry. That command is not recognised.")
