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
    def __init__(self, temperature, humidity, elevation, terrestial, aqeous):
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestial = terrestial
        self.aqeous = aqeous
    
caretaker_list = []

species_list = []

def add_species():
    domain = input("Enter domain: ")
    kingdom = input("Enter kingdom: ")
    phylum = input("Enter phylum: ")
    clas = input("Enter class: ")
    order = input("Enter order: ")
    family = input("Enter family: ")
    genus = input("Enter genus: ")
    species = input("Enter species: ")

    animal_type = input("Is the animal terrestial or aquatic? (Enter 'terrestial' or 'aquatic'): ")

    if animal_type.lower() == 'terrestial':
        lungs = input("Does the animal have lungs? (yes/no): ")
        fur = input("Does the animal have fur? (yes/no): ")
        colour = input("Enter the colour of the animal: ")
        limbs = input("Enter the number of limbs the animal has: ")
        new_species = terrestial(domain, kingdom, phylum, clas, order, family, genus, species, lungs, fur, colour, limbs)
    
    elif animal_type.lower() == 'aquatic':
        gills = input("Does the animal have gills? (yes/no): ")
        fins = input("Does the animal have fins? (yes/no): ")
        scales = input("Does the animal have scales? (yes/no): ")
        new_species = aquatic(domain, kingdom, phylum, clas, order, family, genus, species, gills, fins, scales)

    else:
        print("Invalid animal type. Please enter 'terrestial' or 'aquatic'.")
        return
    species_list.append(new_species)
    print(f"{species} has been added to the species list.")

def add_caretaker():
    name = input("Enter caretaker's name: ")
    age = int(input("Enter caretaker's age: "))
    specialty = input("Enter caretaker's specialty: ")
    new_caretaker = Caretakers(name, age, specialty)
    caretaker_list.append(new_caretaker)
    print(f"{name} has been added to the caretaker list.")