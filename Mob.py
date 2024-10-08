# Representation of a mob in the game
class Mob(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    
# Some sample monsters to use
skeleton = Mob("Skeleton", "The reanimated remains of a former adventurer.")