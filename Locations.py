from Item import *
from Mob import *

class Locations(object):

    def __init__(self):

        # List of all locations we can go to
        self.areas = {}

        # Area we are currently in
        self.area = "start"

    def add(self, key, title, desc = []):

        self.areas[key] = dict( name = title, description = desc, exits = {}, items = [], mobs = [] )

    def add_connection(self, target_key, dir, source_key):

        # Before we add any connections ensure that the locations being connected first exist
        if target_key not in self.areas:
            print("Unable to add {0} to {1}.".format(source_key, target_key))
            return
        
        if source_key not in self.areas:
            print("{0} is not a valid location and can not be added to {1}".format(source_key, target_key))
            return
        
        # Add a connection between the target and source locations
        self.areas[target_key]["exits"][dir] = source_key
        return 
    
    def add_item(self, key, item):

        # Ensure an item is passed to the method
        if not item:
            print("You must supply an item to add to this location")
            return

        # Ensure the location is valid
        if key not in self.areas:
            print("You must supply a vlaid area to add an item to")
            return
        
        # Add the item to the location
        self.areas[key]["items"].append(item)
        return

    def take_item(self, item_key):

        # Check if the item being taken exists in the area being searched
        for item in self.areas[self.area]["items"]:
            
            if item.name == item_key:
                # Remove the item from the area
                self.areas[self.area]["items"].remove(item)
                print("You pick up the {0} and place it in your bag.".format(item_key))
                print()
                # Give the item to the player
                return item

    def add_mob(self, key, mob):

        # Ensure an item is passed to the method
        if not mob:
            print("You must supply a mob to add to this location")
            return

        # Ensure the location is valid
        if key not in self.areas:
            print("You must supply a vlaid area to add a mob to")
            return
        
        # Check if a mob is already in this area
        if len(self.areas[key]["mobs"]) > 0:
            print("This area already has a mob asigned to it. You can't assign another.")
            return
        
        # Add the item to the location
        self.areas[key]["mobs"].append(mob)
        return
    
    def remove_mob(self, key, mob):

        # Ensure a mob is passed to the method
        if not mob:
            print("You must supply a mob to remove from this location")
            return

        # Ensure the location is valid
        if key not in self.areas:
            print("You must supply a vlaid area to remove a mob from")
            return
        
        # Get this locations mob
        local_mob = self.get_mob(mob)
        print(local_mob)
        # Remove the mob from the location#
        self.areas[key]["mobs"].remove(local_mob)
        return

    def has_mob(self, key, mob):
        # Determines if a area has the specified mob, true if it does false otherwise

        # Is the area valid
        if key not in self.areas:
            print("You must input a valid area")
            return False
        
        # Check we have mobs to check against
        if len(self.areas[key]["mobs"]) > 0:

            # Check each mob and see if it matches the passed in mob name
            for areaMob in self.areas[key]["mobs"]:
                if areaMob.name.lower() == mob.lower():
                    return True
                else:
                    return False

        else:
            return False

        # Is the mob valid?
        print()
        if self.areas[key]["mobs"] != mob:
            print("{0} does not exist at this location.".format(mob.name))
            return False
        
        # The mob exists, return true
        return True

    def move_to(self, target):
        ###
        #   Move the player to a new location
        ###

        # Check if the target exists first
        if target not in self.areas[self.area]["exits"]:
            print("{0} is not a valid direction.".format(target))
            return
        else:
            # Set the new area that we wish to go to
            self.area = self.areas[self.area]["exits"][target]

            # Display the main text for the area
            print("You enter a {0}".format(self.areas[self.area]["name"]))
            self.describe()
            return self.area
        
    def describe(self):

        # Display location name
        print()
        print("=" * len(self.areas[self.area]["name"]))
        print(self.areas[self.area]["name"])
        print("=" * len(self.areas[self.area]["name"]))
        print()

        # Display the main description
        for line in self.areas[self.area]["description"]:
            print(line)

        print()

        # Are there any mobs we can fight?
        if len(self.areas[self.area]["mobs"]) > 0:
            print("Monsters you see:")
            for mob in self.areas[self.area]["mobs"]:
                print(mob.name)
            print()

    def search(self):
        
        # Performs a search of the rook you are in for any goodies
        if len(self.areas[self.area]["items"]) > 0:
            print("You search the area and find: ")
            for item in self.areas[self.area]["items"]:
                print(item.name)
        else:
            print("You did not find anything")
        print()

    def get_mob(self, name):
        
        # Loop through the mobs and return the first one found
        for mob in self.areas[self.area]["mobs"]:
            if mob.name.lower() == name:
                return mob
        
        return False

# Create an instance of the Locations class
world = Locations()

# Populate the world with locations
world.add("start", "Cavern Entrance", [
    "As the dust starts to settle, you see there is no way to unblock the entrance.",
    "",
    "There is now just the one exit going north."
    ])


world.add("cavern", "Cavern", ["You step foot into a very large cavern"])

# Add items to a location
world.add_item("start", key)
world.add_item("cavern", gold)
world.add_item("cavern", dagger)

# Add some mobs
world.add_mob("cavern", skeleton)

# Add connections between the locations
world.add_connection("start", "north", "cavern")
world.add_connection("cavern", "south", "start")