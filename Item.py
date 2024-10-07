# Represents an item that the player can use or collect somehow
class Item(object):
    def __init__(self, name, description, type, value):
        
        self.name = name
        self.description = description
        self.type = type
        self.value = value

    def describe(self):
        # Show the itrms description
        for line in self.description:
            print(line)
        print()