class Location(object):

    def __init__(self, name, description):

        self.name = name
        self.description = description
        self.visited = False

        self.exits = { }

    def add_location(self, location, direction):
        self.exits[direction] = location

    def move(self, direction):
        if direction not in self.exits:
            print("You are unable to go {0}").format(direction)

        print("You head {0} towards {1}").format(direction, self.exits[direction].name)
        print()
        print(self.exits[direction].description)

        if self.visited:
            print("The {1} looks just as it did before").format(self.exits[direction].name)

        self.visited = True

class Locations(object):

    def __init__(self):

        # List of all locations we can go to
        self.areas = {}

        # Area we are currently in
        self.area = "start"


    def add(self, key, title, desc):

        self.areas[key] = dict( name = title, description = desc, exits = {})

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

        print(self.areas[self.area]["description"])


# Create an instance of the Locations class
world = Locations()

# Populate the world with locations
world.add("start", "Dungeon Entrance", "The start of your journey for fame and riches. What adventure awaits you?")
world.add("cavern", "Cavern", "You step foot into a very large cavern")

# Add connections between the locations
world.add_connection("start", "north", "cavern")
world.add_connection("cavern", "south", "start")