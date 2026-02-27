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
    new_species = animal_trait(species, health, [])
    species_list.append(new_species)

    # deduct cost from global XP and inform player
    player_xp -= xp_req
    print(f"{xp_req} XP spent. You now have {player_xp} XP remaining.")
    return player_xp

def add_traits():
    global player_xp
    xp_req = 10

    if player_xp < xp_req:
        print("Not enough XP to add traits.")
        return

    print(f"Adding traits to species costs {xp_req} XP. You currently have {player_xp} XP.")
    choice = input("Do you want to add traits to your species? (yes/no)\n> ").strip().lower()
    if choice != "yes":
        print("Trait addition cancelled.")
        return

    if not species_list:
        print("No species available to add traits to.")
        return

    # Select a species (with retry on invalid)
    species_choice = None
    while species_choice is None:
        print("Select a species to add traits to:")
        for i, s in enumerate(species_list, start=1):
            print(f"{i}. {s.species}")

        sel = input("Enter species number or name:\n> ").strip()
        if sel.isdigit():
            idx = int(sel) - 1
            if 0 <= idx < len(species_list):
                species_choice = species_list[idx]
            else:
                print("Invalid species number. Try again.")
        else:
            species_choice = next((s for s in species_list if s.species.lower() == sel.lower()), None)
            if species_choice is None:
                print("Species not found. Try again.")

    # Select trait category (with retry on invalid)
    trait_cat_choice = None
    while trait_cat_choice is None:
        print("Choose a trait type from the following options:")
        for trait in traits:
            print(trait)

        user_input = input("Enter the trait category:\n> ").strip()
        if user_input in traits:
            trait_cat_choice = user_input
        else:
            trait_cat_choice = next((c for c in traits if c.lower() == user_input.lower()), None)
            if trait_cat_choice is None:
                print("Invalid trait category. Try again.")

    # Select specific trait (with retry on invalid)
    trait_choice2 = None
    while trait_choice2 is None:
        print(f"Choose a trait from the following options for {trait_cat_choice}:")
        for spec_trait in traits[trait_cat_choice]:
            print(spec_trait)

        user_input = input("Enter the specific trait:\n> ").strip()
        if user_input in traits[trait_cat_choice]:
            trait_choice2 = user_input
        else:
            trait_choice2 = next((t for t in traits[trait_cat_choice] if t.lower() == user_input.lower()), None)
            if trait_choice2 is None:
                print("Invalid trait choice. Try again.")

    # Append trait and deduct XP
    species_choice.traits.append((trait_cat_choice, trait_choice2))
    print(f"Added the following trait: {trait_cat_choice} {trait_choice2} to {species_choice.species}.")

    player_xp -= xp_req
    print(f"{xp_req} XP spent. You now have {player_xp} XP remaining.")
    return player_xp

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
    if isinstance(animal, species_list) <= habitat("terrestrial") and isinstance(animal, species_list) <= habitat("aqueous"):
        animal.health -= 10
    elif isinstance(animal, species_list) >= habitat("terrestrial") and isinstance(animal, species_list) >= habitat("aqueous"):
        animal.health += 10
def health_system_temperature(animal, habitat):
    if isinstance(animal, species_list) <= habitat("temperature"):
        animal.health -= 10
    elif isinstance(animal, species_list) >= habitat("temperature"):
        animal.health += 10
def health_system_humidity(animal, habitat):
    if isinstance(animal, species_list) <= habitat("humidity"):
        animal.health -= 10
    elif isinstance(animal, species_list) >= habitat("humidity"):
        animal.health += 10
def health_system_elevation(animal, habitat):
    if isinstance(animal, species_list) <= habitat("elevation"):
        animal.health -= 10
    elif isinstance(animal, species_list) >= habitat("elevation"):
        animal.health += 10


#Remove the species when the population (health) reaches 0
def species_removal():
    for animal in species_list:
        if animal.health <= 0:
            print(f"{animal.species} species has gone extinct due to insufficient population.")
            species_list.remove(animal)
def health_check():
    for animal in species_list:
        print(f"{animal.species} health: {animal.health}")
