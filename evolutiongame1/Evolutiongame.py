from class_caretaker import *
from class_animals import *
from class_habitat import *
from evolutiongame_methods import *

menuflag = True
while menuflag == True:
    print("\nMenu:")
    print("1. Exit Menu")
    choice = input("Enter your choice: ")

    if choice == '1':
        menuflag = False
        print("Exiting game. Goodbye!")
    else:
        print("Invalid choice. Please enter a number from 1 to 1.")