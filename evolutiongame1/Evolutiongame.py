class Animal: #parent class
    def __init__(self, domain, kingdom, phylum, clas, order, family, genus, species):
        self.domain = domain
        self.kingdom = kingdom
        self.phylum = phylum
        self.clas = clas
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species

class terrestial(Animal): #subclass 1):
    def __init__(self, domain, kingdom, phylum, clas, order, family, genus, species, lungs, fur, colour, limbs):
        super().__init__(domain, kingdom, phylum, clas, order, family, genus, species)
        self.lungs = lungs
        self.fur = fur
        self.colour = colour
        self.limbs = limbs

class aquatic(Animal): #subclass 2)
    def __init__(self, domain, kingdom, phylum, clas, order, family, genus, species, gills, fins, scales):
        super().__init__(domain, kingdom, phylum, clas, order, family, genus, species)
        self.gills = gills
        self.fins = fins
        self.scales = scales

class Caretakers:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty

class Habitat:
    def __init__(self, temperature, humidity, elevation, terrestial, aqeous)
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestial = terrestial
        self.aqeous = aqeous
    
      