class Animal:  # parent class
    def __init__(self, species, health):
        self.species = species
        self.health = health

class terrestial(Animal):  # subclass 1):
    def __init__(self, species, health, lungs, fur, colour, limbs):
        super().__init__(species, health)
        self.lungs = lungs
        self.fur = fur
        self.colour = colour
        self.limbs = limbs


class aquatic(Animal):  # subclass 2)
    def __init__(self, species, health, gills, fins, scales):
        super().__init__(species, health)
        self.gills = gills
        self.fins = fins
        self.scales = scales
