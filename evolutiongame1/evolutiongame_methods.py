from class_caretaker import *
from class_animals import *
from class_habitat import *
generation_counter = 0
player_xp = 300
species_list = []
caretaker_list = []

def add_species():
    xp_req = 100
    if len(species_list) >= 4:
        print("Maximum number of species reached.")
        return

    if player_xp < xp_req:
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
    global player_xp
    player_xp -= xp_req
    print(f"Species added! You now have {player_xp} XP.")

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
    specialty = input("Enter caretaker's specialty: ")
    new_caretaker = Caretakers(name, age, specialty)
    caretaker_list.append(new_caretaker)
    print(f"{name} has been added to the caretaker list.")
