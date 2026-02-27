from class_caretaker import *
from class_animals import *
from class_habitat import *
from evolutiongame_methods import *
import player_history

menuflag = True
while menuflag == True:
    #print("\nMenu:")
    #print("1. Exit Menu")
    #choice = input("Enter your choice: ")

    #if choice == '1':
        #menuflag = False
        #print("Exiting game. Goodbye!")
    #else:
        #print("Invalid choice. Please enter a number from 1 to 1.")


    #def main() -> None:
        #print("=== Evolution Game (CLI) ===")

    while True:
        print("\nMenu: [H]abitat  [T]rait  [V]iew  [Q]uit")
        cmd = input("> ").strip().lower()

        if cmd == "h":
            player_history.get_player_habitat()

        elif cmd == "t":
            player_history.get_player_traits()

        elif cmd == "v":
            player_history.refresh_screen()

        elif cmd == "q":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

#if __name__ == "__main__":
        #main()