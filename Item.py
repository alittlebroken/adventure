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

# Create some Items
dagger = Item("dagger", "A simple silver dagger", "weapon", 1)
gold = Item("gold", "A single gold coin", "coin", 1)
key = Item("key", "A rusty old key. Wonder what lock it opens?", "quest", 0)