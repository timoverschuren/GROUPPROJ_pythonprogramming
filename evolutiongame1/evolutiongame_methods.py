from class_caretaker import *
from class_animals import *
from class_habitat import *


generation_counter = 0
player_xp = 300
species_list = []
caretaker_list = []

def add_species():
    global player_xp
    xp_req = 100
    if len(species_list) >= 4:
        print("Maximum number of species reached.")
        return
    print(f"Adding a new species costs {xp_req} XP. You currently have {player_xp} XP.")
    print("Do you want to add a new species? (yes/no)")
    choice = input("> ").strip().lower()
    if choice != "yes":
        print("Species addition cancelled.")
        return

    if player_xp < xp_req:
        print("Not enough XP to add a new species.")
        return
    species = input("Enter the new species name: ")
    health = 100
    new_species = Animal(species, health)
    species_list.append(new_species)

    # deduct cost from global XP and inform player
    player_xp -= xp_req
    print(f"{xp_req} XP spent. You now have {player_xp} XP remaining.")
    return player_xp

def add_traits(animal, traits):
    print("Adding traits to species costs 50 XP. You currently have {player_xp} XP.")

def restart_game():
    """Reset game state: clear species and caretakers, reset generation and XP."""
    global species_list, caretaker_list, generation_counter, player_xp
    species_list.clear()
    caretaker_list.clear()
    generation_counter = 0
    player_xp = 300
    print("Game restarted: species and caretakers cleared, generation reset, XP restored.")

def iterate_generation():
    global generation_counter
    generation_counter += 1
    print(f"Generation {generation_counter} has begun!")
    if len(species_list) == 0:
        print("Youve lost! No species left to evolve.")           
        restart_game()

def add_caretaker():
    if len(caretaker_list) >= 1:
        print("Maximum number of caretakers reached.")
        return
    name = input("Enter caretaker's name: ")
    age = int(input("Enter caretaker's age: "))
    specialty = input("Enter caretaker's specialty (Aqueous, Terrestrial, Mountaineering, Hot climates, Cold climates): ")
    valid_specialties = ["Aqueous", "Terrestrial", "Mountaineering", "Hot climates", "Cold climates"]
    if specialty not in valid_specialties   :
        print("Invalid specialty. Please choose from the listed options.")
        return
    else: print(f"Caretaker specialty is now {specialty}.")
    new_caretaker = Caretakers(name, age, specialty)
    caretaker_list.append(new_caretaker)
    print(f"{name} has been added to the caretaker list.")

def display_species_details():
    flag = False #flag to check if species is found, if not found after cycling through all species, print error message
    while flag == False:

        for x in species_list:
            print(f"Species: {x.species}") #print all species to help user know which one to choose

        species_name = input("Enter the name of the species you want details on: ")
        for x in species_list: #cycle all species to find the one the user wants details on and print its details
            if x.species.lower() == species_name.lower():
                print(f"Species: {x.species}")
                print(f"Health: {x.health}")
                if isinstance(x, terrestial):
                    print(f"Lungs: {x.lungs}")
                    print(f"Fur: {x.fur}")
                    print(f"Colour: {x.colour}")
                    print(f"Limbs: {x.limbs}")
                elif isinstance(x, aquatic):
                    print(f"Gills: {x.gills}")
                    print(f"Fins: {x.fins}")
                    print(f"Scales: {x.scales}")
                flag = True
                break
        if not flag:
            print("Species not found. Please try again.")

#Health system methods.
#compare animal traits with habitat attributes to calculate if animal loses "health" or not, and if it does, 10 health is lost. If health reaches 0, the species is removed from the species list.
def health_system_habitat(animal, habitat):
    if isinstance(animal, species_list) != habitat("terrestrial") and isinstance(animal, species_list) !=habitat("aqueous"):
        animal.health -= 10
def health_system_temperature(animal, habitat):
    if isinstance(animal, species_list) != habitat("temperature"):
        animal.health -= 10
def health_system_humidity(animal, habitat):
    if isinstance(animal, species_list) != habitat("humidity"):
        animal.health -= 10
def health_system_elevation(animal, habitat):
    if isinstance(animal, species_list) != habitat("elevation"):
        animal.health -= 10


#Remove the species when the population (health) reaches 0
def species_removal():
    for animal in species_list:
        if animal.health <= 0:
            print(f"{animal.species} species has gone extinct due to insufficient population.")
            species_list.remove(animal)
def health_check():
    for animal in species_list:
        print(f"{animal.species} health: {animal.health}")
