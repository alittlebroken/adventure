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

        # Check to see if the current area has an item matching the key passed in
        if item_key not in self.areas[self.area]["items"]:
            print("This area does not have an item called {0}".format(item_key))
            return
        
        # Remove the item from the location
        self.areas[self.area]["items"].remove(item_key)
        print("You pick up the {0} and place it in your bag.".format(item_key))
        print()

        # return the item picked up to the player
        return item_key

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
            print("You must supply a vlaid area to add a mob to")
            return
        
        # Remove the mob from the location
        self.areas[key]["mobs"].remove(mob)
        return

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
                print(mob)
            print()

        # Display any items this location has
        if len(self.areas[self.area]["items"]) > 0:
            print("Items you see:")
            for item in self.areas[self.area]["items"]:
                print(item)
            print()

        # Check the exits this location has
        if len(self.areas[self.area]["exits"]) > 0:
            print("You can go:")
            for exit in self.areas[self.area]["exits"]:
                print(exit)
            print()


# Create an instance of the Locations class
world = Locations()

# Populate the world with locations
world.add("start", "Dungeon Entrance", ["The start of your journey for fame and riches.", "What adventure awaits you?"])
world.add("cavern", "Cavern", ["You step foot into a very large cavern"])

# Add items to a location
world.add_item("start", "key")
world.add_item("cavern", "gold")
world.add_item("cavern", "dagger")

# Add some mobs
world.add_mob("cavern", "skeleton")

# Add connections between the locations
world.add_connection("start", "north", "cavern")
world.add_connection("cavern", "south", "start")