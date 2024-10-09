# Represents the players bag for holiding items they collect on thier adventures
class Bag(object):
    def __init__(self):
        self.items = []
        self.size = 0

    # Checks if an item is in the bag
    def contains(self, name):

        for bagItem in self.items:
            
            if bagItem.name == name:
                return True
            
        return False

    # Adds an item to the bag
    def add(self, item):
        
        # Check to ensure the item is not already in the bag
        if self.contains(item):
            print("You can only have one of those items in the bag at a time")
            return
        else:
            self.items.append(item)
            self.size += 1
            return
        
    # Removes an item from the bag
    def remove(self, name):

        # Check to ensure the item is not already in the bag
        if self.contains(name):
            # Get a copy of the item we wish to remove
            item = self.getItem(name)
            self.items.remove(item)
            self.size -= 1
            return item
        else:
            print("You don't have that item in your bag to remove.")
            return False
        
    # Displays the contents of the bag
    def display(self):

        print("You are carrying the following items:")
        print()
        for item in self.items:
            print(item.name)

    # Gets the actual item based on it's name
    def getItem(self, name):

        for item in self.items:
            if item.name == name:
                return item
        