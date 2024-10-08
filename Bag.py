# Represents the players bag for holiding items they collect on thier adventures
class Bag(object):
    def __init__(self):
        self.items = []
        self.size = 0

    # Checks if an item is in the bag
    def exists(self, item):

        for bagItem in self.items:
            
            if bagItem.name == item.name:
                return True
            else: 
                return False

    # Adds an item to the bag
    def add(self, item):
        
        # Check to ensure the itrm is not already in the bag
        if self.inBag(item):
            print("You can only have one of those items in the bag at a time")
            return
        else:
            self.items.append(item)
            self.size += 1
            return
        
    # Removes an item from the bag
    def remove(self, item):

        # Check to ensure the item is not already in the bag
        if self.inBag(item):
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

