from Locations import *

# TODO
# - Ability to collect and spend money
# - Add more rooms
# - Add more mobs
# - Add more items
# - Create a game class and object
# - Create a player class and object
# - Move the commands list from if statements to a switch [DONE]
# Ideas ( Inspiration from Zork ):
# - to move in a direction just say the direction [DONE]
# - use look to describe the room you are in
# - Attack things with the command attack <mob> with <weapon> ( Have no slots, just has to be in your bag )
# - To give an item to something use give <item> to <something>
# - Other directions aside form north, south, east and west can be up, down
# - Don't list what objects or exits there are on screen, have the player gues by using commands like north or search or look etc
# - A room can have objects which can be interacted with, perhaps a new room etc or a chest with loot inside
# - Set the command prompt to just > [DONE]

# Process commands entered by the player
def process_cmd(command):
    
    global running, location

    # Split out the cmd passed in by the space character
    cmds = command.split(" ")

    # Perform the correct action based on the first command entered
    # Each case will need to access the other parts of the commands ( if provided )
    # to perform properly
    match cmds[0]:
        case "north":
            location = world.move_to(cmds[0])
            return
        case "east":
            location = world.move_to(cmds[0])
            return
        case "south":
            location = world.move_to(cmds[0])
            return
        case "west":
            location = world.move_to(cmds[0])
            return
        case "help":
            help()
            return
        case "quit":
            print("Thanks for playing, bye.")
            running = False
            return
        case "look":
            world.describe()
            return
        case "take":
            world.take_item(cmds[1])
            player_bag.append(cmds[1])
            return
        case "inventory":
            if len(player_bag) > 0:
                print("You are carrying the following items:")
                # Dispay the contents
                for item in player_bag:
                    print(item)
                print()
            else:
                print("You currently have no items in your bag.")
            return
        case "drop":
            
             # Check if an item has been specified
            if len(cmds) <= 1:
                print("You must supply the name of an item you wish to drop")
            else:
                # Are we carrying that item in the bag?
                if cmds[1] not in player_bag:
                    print("You are not carrying that item so you can't drop it")
                else:
                    # Remove the item from the players bag
                    player_bag.remove(cmds[1])

                    # Add the item to the list of items the area has
                    world.add_item(location, cmds[1])

        case "equip":
            # Equip the item
            equip_item(cmds[1], cmds[2])
        case "unequip":
            # Unequip the item
            unequip_item(cmds[1], cmds[2])
        case "show":
             # Show those slots of yours
            show_slots()
        case "fight":
            
            # check that a monster was specified to fight
            if len(cmds) <= 1:
                print("You must specify the monster you wish to attack")
            else:
                # Attack the specified monster
                fight_mob(location, cmds[1])

        case "search":
            # Search the area for any goodies
            world.search()

        case _:
            print("That is not a recognised command. Type help for a listing of the commands")
            return

# Name of the APP
appName = "Caverns of Mysteria"
introText = [
    "You are an intrepid adventurer in search of the fabled treasure of Mysteria",
    "Many adventurers before you have tried and failed to recover it, will you be any different?",
    " ",
    "As you step foot into the caverns entrance, you hear a rumble and the door is covered by falling rocks.",
    "It seems the only way is forward. Onwards to glory or death."
]

# Sets the game running
running = True

# Stores the location we are currently in
location = "start"

# The players bag for any items they pick up
player_bag = []

# The slots for a player
player_slots = { 
    "weapon": None,
    "head": None,
    "shoulders": None,
    "chest": None,
    "hands": None,
    "belt": None,
    "legs": None,
    "feet": None,
    "back": None 
}

# Help menu
def help():
    print("You can perform the following commands:")
    print()
    print("q or quit or exit - Leave the game")
    print("help - Display this menu")
    print()
    print("look - Describe the area you are in")
    print("take <item> - Take an item that the area has")
    print("inventory - Show the items you have in your bag")
    print("drop <item> - Drop an item to the ground")
    print("equip <item> <slot> - Equip an item you have stored in your bag to yourself ( Slots: weapon )")
    print("unequip <item> <slot> - Unequip an item you have equipped for a particluar slot ( Slots: weapon )")
    print("show - Show what items you have equiiped in which slot")
    print("fight <mob> - Fight the specified mob")
    print("search - Look for loot in the location you are in")
    print()

# Equip an item to the character to be used
def equip_item(item, slot):

    # Check if we have the item first
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

def unequip_item(item, slot):

    # Check if the slot for the player is available
    if slot not in player_slots:
        print("The player does not have a slot matching that description")
        return
    
    # Check if the slot has that item equipped
    if player_slots[slot] != item:
        print("You do no have that item equipped in that slot")
        return
    
    # Remove the item from the slot
    player_slots[slot] = None

    # Place the item back into the players bag
    player_bag.append(item)

    # Display a message to the user
    print("You have unequipped {0} and placed it back into your bag".format(item))
    return

def fight_mob(area, mob):

    global running

    # Check the mob exists in the area
    if world.has_mob(area, mob):
        # Do we have a weapon to foght the mob with?
        if player_slots["weapon"] != None:
            print("You defeated the {0}".format(mob))

            # remove the mob from the area
            world.remove_mob(area, mob)
        else:
            print("You attemped to fight the {0} without a wepaon. You were defeated. Game Over".format(mob))
            running = False

def show_slots():

    for index, (key, value) in enumerate(player_slots.items()):
        if value != None:
            print("{1} is equipped in your {0} slot.".format(key, value))
    
    print()
    return

# Display the intro text
print()
print("*" * len(appName))
print(appName)
print("*" * len(appName))
print()

for line in introText:
    print(line)
print()

# Keep looping until the game is own, lost or quit
while running:

    # Get any inut from the player
    command = input("> ")

    process_cmd(command)
