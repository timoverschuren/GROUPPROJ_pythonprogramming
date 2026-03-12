from class_caretaker import *
from class_animals import *
import player_history as ph
from class_habitat import *
from player_history import refresh_screen

generation_counter = 0 # Global variable to track generations; reset on game restart
player_xp = 330 # Global variable to track player XP; reset on game restart
species_list = [] # Global variable to track species; reset on game restart
caretaker_list = [] # Global variable to track caretakers; reset on game restart

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
    new_species.habitat = None
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


def render_visuals_for_species():
    """
    On-demand rendering helper (call this from File 1 when user presses your menu #8).
    Lets the user choose a species; then copies ONLY that species' data
    into player_history's view-state and renders tree + slope.
    """
    if not species_list:
        print("No species available to render.")
        return

    # Pick a species to visualize
    target = None
    while target is None:
        print("Select a species to render:")
        for i, s in enumerate(species_list, start=1):
            print(f"{i}. {s.species} (habitat: {getattr(s, 'habitat', None)})")

        sel = input("Enter species number or name:\n> ").strip()
        if sel.isdigit():
            idx = int(sel) - 1
            if 0 <= idx < len(species_list):
                target = species_list[idx]
            else:
                print("Invalid species number. Try again.")
        else:
            target = next((s for s in species_list if s.species.lower() == sel.lower()), None)
            if target is None:
                print("Species not found. Try again.")

    # If species has no habitat, let the user choose one now (still on-demand)
    if getattr(target, "habitat", None) is None:
        print("\nThis species has no habitat yet. Choose one now (or press Enter to skip):")
        for h in habitats:
            print(f" - {h}")
        h_choice = input("Habitat name (optional): ").strip().lower()
        if h_choice:
            chosen = next((h for h in habitats if h.lower() == h_choice), None)
            if chosen is None:
                print("Invalid habitat. Proceeding without slope.")
            else:
                target.habitat = chosen

    # Sync ONLY this species' traits + habitat into the visualization module
    ph.selected_traits = target.traits.copy()
    ph.selected_habitat = getattr(target, "habitat", None)

    try:
        ph.refresh_screen()  # Will draw tree; slope draws only if both curves are valid
        print(f"Rendered visuals for '{target.species}' (habitat: {ph.selected_habitat}).")
        if ph.selected_habitat is None:
            print("(Note) No habitat set, so slope comparison will not render.")
    except Exception as e:
        print(f"(Note) Could not render visuals: {e}")

def assign_species_to_habitat():
    if not species_list:
        print("No species available to assign.")
        return

    # List available species
    print("Available species:")
    for x in species_list:
        print(f" - {x.species}")

    # Get species choice
    choice_s = input("Choose a species to assign to a habitat: ").strip()
    selected_species = None
    for x in species_list:
        if choice_s.lower() == x.species.lower():
            selected_species = x
            break
    if not selected_species:
        print("Invalid species name. Returning to menu.")
        return

    # List available habitats
    print("Available habitats:")
    for h in habitats:
        print(f" - {h}")

    # Get habitat choice
    choice_h = input("Choose a habitat to assign the species to: ").strip()
    # Find the exact habitat name (case-insensitive match)
    matched_habitat = None
    for h in habitats:
        if h.lower() == choice_h.lower():
            matched_habitat = h
            break
    
    if matched_habitat is None:
        print("Invalid habitat name. Returning to menu.")
        return
    
    # Update the species' habitat attribute
    selected_species.habitat = matched_habitat
    print(f"{selected_species.species} is now assigned to habitat: {matched_habitat}.")

def check_assigned_habitats():
    if not species_list:
        print("No species available.")
        return
    
    print("Current species to habitat assignments:")
    for species in species_list:
        if species.habitat is None:
            print(f" - {species.species} has no habitat assigned.")
        else:
            print(f" - {species.species} is assigned to {species.habitat}")

def restart_game():
    """Reset game state: clear species and caretakers, reset generation and XP."""
    global species_list, caretaker_list, generation_counter, player_xp
    species_list.clear()
    caretaker_list.clear()
    generation_counter = 0
    player_xp = 330
    print("Game restarted: species and caretakers cleared, generation reset, XP restored.")

def iterate_generation():
    global generation_counter, player_xp
    for x in species_list:
        if x.habitat is None:
            print(f"{x.species} is not assigned to a habitat. Assign all species to a habitat before iterating the generation.")
            return
        
    for x in species_list:
        if x.traits is None or len(x.traits) == 0:
            print(f"{x.species} has no traits. Add traits to all species before iterating the generation.")
            return
    
    generation_counter += 1
    player_xp += 50
    print(f"Generation {generation_counter} has begun!")
    health_check()  # Show health of all species at the start of the generation
    for x in species_list:
        health_system(x)

    live_check()  # Check if any species died after health loss

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
    return

def display_species_details():
    if len(species_list) == 0:
        print("No species available to display.")
        return
    
    max_retries = 3  # Prevent infinite loops; adjust as needed
    retries = 0
    
    while retries < max_retries:
        print("\nAvailable species:")
        for x in species_list:
            print(f" - {x.species}")
        
        choice = input("Enter the name of the species you want to view details for (or 'quit' to exit): ").strip()
        if choice.lower() == 'quit':
            print("Exiting species details view.")
            return
        
        # Find the matching species
        matched_species = None
        for x in species_list:
            if choice.lower() == x.species.lower():
                matched_species = x
                break
        
        if matched_species:
            # Print details (using the object's __str__ method for a full summary)
            print(f"\nDetails for '{matched_species.species}':")
            print(matched_species)  # This calls __str__ and shows species, health, traits
            return  # Exit on success
        else:
            retries += 1
            print(f"Species '{choice}' not found. Please try again ({max_retries - retries} attempts left).")
    
    print("Too many invalid attempts. Returning to menu.")


#Health system methods.
#compare animal traits with habitat attributes to calculate if animal loses "health" or not, and if it does, 10 health is lost. If health reaches 0, the species is removed from the species list.
def health_system(animal):
    healthloss = 10

    temp_score = (habitats[animal.habitat]["temperature"])-habitats[animal.chosen_habitat]["temperature"]
    temp_loss = (5 - healthloss * (1 - temp_score))
    animal.health -= temp_loss
    if temp_loss > 0:
        print(f"{animal.species} lost {temp_loss} health due to the temperature.")
    else:
        print(f"{animal.species} gained {abs(temp_loss)} health due to the temperature.")

    hum_score = habitats[animal.habitat]["humidity"]-habitats[animal.chosen_habitat]["humidity"]
    hum_loss = (5 - healthloss * (1 - hum_score))
    animal.health -= hum_loss
    if hum_loss > 0:
        print(f"{animal.species} lost {hum_loss} health due to the humidity.")
    else:
        print(f"{animal.species} gained {abs(hum_loss)} health due to the humidity.")

    elev_score = habitats[animal.habitat]["elevation"]-habitats[animal.chosen_habitat]["elevation"]
    elev_loss = (5 - healthloss * (1 - elev_score))
    animal.health -= elev_loss
    if elev_loss > 0:
        print(f"{animal.species} lost {elev_loss} health due to the elevation.")
    else:
        print(f"{animal.species} gained {abs(elev_loss)} health due to the elevation.")

    terr_score = habitats[animal.habitat]["terrestrial"]-habitats[animal.chosen_habitat]["terrestrial"]
    terr_loss = (5 - healthloss * (1 - terr_score))
    animal.health -= terr_loss
    if terr_loss > 0:
        print(f"{animal.species} lost {terr_loss} health due to the terrestrial factor.")
    else:
        print(f"{animal.species} gained {abs(terr_loss)} health due to the terrestrial factor.")

def health_check():
    for animal in species_list:
        print(f"{animal.species} health: {animal.health}")
    return

def check_xp():

    global player_xp
    print(f"You currently have {player_xp} XP.")
    return player_xp

def live_check():
    dead_species = []
    for x in species_list[:]:  # Iterate over a copy of the list
        if x.health <= 0:
            dead_species.append(x.species)  # Save the species name
            species_list.remove(x)  # Remove from the actual list
    
    # Print all dead species after removal
    for name in dead_species:
        print(f"Species {name} died")
