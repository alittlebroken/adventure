from Locations import *

# Sets the game running
running = True

# Stores the location we are currently in
location = "start"

# Help menu
def help():
    print("You can perform the following commands:")
    print()
    print("q or quit or exit - Leave the game")
    print("help - Display this menu")
    print("g or go <direction> - Travel in the direction given ( Can be one of north, south, east or west )")

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
            world.move_to(cmd[1])
    elif (cmd[0] == "help" or cmd[0] == "h"):
        help()
    else:
        print("Sorry. That command is not recognised.")
