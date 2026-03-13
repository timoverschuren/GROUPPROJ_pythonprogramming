from player_history import *
from class_caretaker import *
from class_animals import *
from class_habitat import *
from evolutiongame_methods import *
from player_history import *

# Main menu loop
# Controls the main game menu. Keeps running until the player chooses to exit

menuflag = True
while menuflag == True:
    #  Display menu options available to player
    print("\nMenu:")
    print("1. Exit Menu")
    print("2. Add Species")
    print("3. Add Caretaker")
    print("4. Restart Game")
    print("5. Display Species Details")
    print("6. Iterate Generation")
    print("7. Add Traits to Species")
    print("8. Assign species to habitat")
    print("9. Generate Visuals")
    print("10. Check XP")
    print("11. Check species assigned habitats")
    choice0 = input("Enter your choice: ")


    if choice0 == '1':
        # If the player chooses to exit, set the menu flag to False to break the loop and end the game
        menuflag = False
        print("Exiting game. Goodbye!")
    elif choice0 == '2':
        # If the player chooses to add a species, call the add_species() function to add a new species to the game
        add_species()
    elif choice0 == '3':
        # If the player chooses to add a caretaker, call the add_caretaker() function to add a new caretaker to the game
        add_caretaker()
    elif choice0 == '4':
        # If the player chooses to restart the game, call the restart_game() function to reset the game state from scratch
        restart_game()
    elif choice0 == '5':
        # If the player chooses to display species details, call the display_species_details() function to ask which species they want the details to, and then give teh details of that one
        display_species_details()
    elif choice0 == '6':
        # If the player chooses to iterate the generation, call the iterate_generation() function to progress by one generation, will give or take hp from the species and if it doesn't die, player will get 50xp
        iterate_generation()
    elif choice0 == '7':
        # If the player chooses to add traits to a species, call the add_traits() function to allow the player to select a species and assign new traits to it, if the number of xp the player has allows it
        add_traits()
    elif choice0 == '8':
        # If the player chooses to assign species to habitats, call the assign_species_to_habitat() function to select a species and assign it to a habitat of the player's choice
        assign_species_to_habitat()
    elif choice0 == '9':
        # If the player chooses to generate visuals, call the render_visuals_for_species() function to create visual representations of the species's affinity to its habitat
        from evolutiongame_methods import render_visuals_for_species
        render_visuals_for_species()
    elif choice0 == '10':
        # If the player chooses to check XP, call the check_xp() function to display the current XP of the player
        check_xp()
    elif choice0 == '11':
        # If the player chooses to check assigned habitats, call the check_assigned_habitats() function to show which species are currently assigned to which habitats
        check_assigned_habitats()


    else:
        # If player types something that is not part of the options, this error message is shown
        print("Invalid choice. Please enter a number from 1 to 11.")
