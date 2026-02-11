class Animal: #parent class
    def __init__(self, domain, kingdom, phylum, clas, order, family, genus, species, health):
        self.domain = domain
        self.kingdom = kingdom
        self.phylum = phylum
        self.clas = clas
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species
        self.health = initial_health
        initial_health = 100


class terrestial(Animal): #subclass 1):
    def __init__(self, species, xp, health, lungs, fur, colour, limbs):
        super().__init__(species, xp, health)
        self.lungs = lungs
        self.fur = fur
        self.colour = colour
        self.limbs = limbs

class aquatic(Animal): #subclass 2)
    def __init__(self, species, xp, health, gills, fins, scales):
        super().__init__(species, xp, health)
        self.gills = gills
        self.fins = fins
        self.scales = scales

class Caretakers:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty

class Habitat:
    def __init__(self, temperature, humidity, elevation, terrestial, aqeous):
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestial = terrestial
        self.aqeous = aqeous
#humidity goes from 0/100 and elevation/temperature and terrestrial/aqeuos are 0/100 with respect to eachother are real numbers
Desert.habitat = Habitat(temperature = 40, humidity = 10, elevation = 20, terrestrial = 99, aqeous=1)
Ocean.habitat = Habitat(temperature = 10, humidity = 100, elevation = 0, terrestrial = 0, aqeous=100)
Forest.habitat = Habitat(temperature = 15, humidity = 40, elevation = 100, terrestrial = 75, aqeous=25)
Mountains.habitat = Habitat(temperature = -10, humidity = 60, elevation = 3000, terrestrial = 90, aqeous=10)
Lake.habitat = Habitat(temperature = 10, humidity = 100, elevation = 0, terrestrial = 0, aqeous=100)
shore.habitat = Habitat(temperature = 15, humidity = 80, elevation = 0, terrestrial = 40, aqeous=60)


