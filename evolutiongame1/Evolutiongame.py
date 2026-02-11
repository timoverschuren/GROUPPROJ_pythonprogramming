class Animal: #parent class
    def __init__(self, species, xp, health):
        self.species = species
        self.xp = xp
        self.health = health

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
    
caretaker_list = []

species_list = []

def add_species(self):

    xp_req = 100
    if len(species_list) >= 4:
        print("Maximum number of species reached.")
        return
    
    if self.xp < xp_req:
        print("Not enough XP to add a new species.")
        return
    species = input("Enter species: ")
    xp = 100
    health = 100

    animal_type = input("Is the animal terrestial or aquatic? (Enter 'terrestial' or 'aquatic'): ")

    if animal_type.lower() == 'terrestial':
        lungs = input("Does the animal have lungs? (yes/no): ")
        fur = input("Does the animal have fur? (yes/no): ")
        colour = input("Enter the colour of the animal: ")
        limbs = input("Enter the number of limbs the animal has: ")
        new_species = terrestial(species, xp, health, lungs, fur, colour, limbs)
    
    elif animal_type.lower() == 'aquatic':
        gills = input("Does the animal have gills? (yes/no): ")
        fins = input("Does the animal have fins? (yes/no): ")
        scales = input("Does the animal have scales? (yes/no): ")
        new_species = aquatic(species, xp, health, gills, fins, scales)

    else:
        print("Invalid animal type. Please enter 'terrestial' or 'aquatic'.")
        return
    species_list.append(new_species)
    self.xp -= xp_req
    print(f"Species added! You now have {self.xp} XP.")

def add_caretaker():
    if len(caretaker_list) >= 1:
        print("Maximum number of caretakers reached.")
        return
    name = input("Enter caretaker's name: ")
    age = int(input("Enter caretaker's age: "))
    specialty = input("Enter caretaker's specialty: ")
    new_caretaker = Caretakers(name, age, specialty)
    caretaker_list.append(new_caretaker)
    print(f"{name} has been added to the caretaker list.")

generation_counter = 0
def iterate_generation(self):
    global generation_counter
    generation_counter += 1
    print(f"Generation {generation_counter} has begun!")
    if len(species_list) == 0:
        print("Youve lost! No species left to evolve.")
        
        return
