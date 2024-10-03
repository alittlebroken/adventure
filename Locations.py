class Locations(object):

    def __init__(self):

        # List of all locations we can go to
        self.areas = {}

        # Area we are currently in
        self.area = "start"


    def add(self, key, title, desc = []):

        self.areas[key] = dict( name = title, description = desc, exits = {}, items = [])

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
            return
        
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

# Add connections between the locations
world.add_connection("start", "north", "cavern")
world.add_connection("cavern", "south", "start")