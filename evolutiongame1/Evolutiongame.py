from class_caretaker import *
from class_animals import *
from class_habitat import *
from evolutiongame_methods import *
from player_history import *

menuflag = True
while menuflag == True:
    print("\nMenu:")
    print("1. Exit Menu")
    print("2. Add Species")
    print("7. Add Traits to Species")
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
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")


    #def main() -> None:
        #print("=== Evolution Game (CLI) ===")

#     while True:
 #       print("\nMenu: [H]abitat  [T]rait  [V]iew  [Q]uit")
  #      cmd = input("> ").strip().lower()
   #     if cmd == "h":
    #        player_history.get_player_habitat()
#
 #       elif cmd == "t":
  #          player_history.get_player_traits()
#
 #       elif cmd == "v":
  #          player_history.refresh_screen()
#
 #       elif cmd == "q":
  #          print("Goodbye!")
   #         break
#
 #       else:
  #          print("Unknown command.")

#if __name__ == "__main__":
        #main()