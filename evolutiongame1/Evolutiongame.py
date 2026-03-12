import player_history
from class_caretaker import *
from class_animals import *
from class_habitat import *
from evolutiongame_methods import *
from player_history import *

#main menu loop
#controls the main game menu. Keeps running until the player chooses to exit

menuflag = True
while menuflag == True:
    #display menu options available to player
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
        menuflag = False
        print("Exiting game. Goodbye!")
    elif choice0 == '2':
        add_species()
    elif choice0 == '3':
        add_caretaker()
    elif choice0 == '4':
        restart_game()
    elif choice0 == '5':
        display_species_details()
    elif choice0 == '6':
        iterate_generation()
    elif choice0 == '7':
        add_traits()
    elif choice0 == '8':
        assign_species_to_habitat()
    elif choice0 == '9':
        from evolutiongame_methods import render_visuals_for_species
        render_visuals_for_species()
    elif choice0 == '10':
        check_xp()
    elif choice0 == '11':
        check_assigned_habitats()


else:
        print("Invalid choice. Please enter a number from 1 to 8.")
