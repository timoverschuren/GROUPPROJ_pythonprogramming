from class_habitat import habitats
from class_animals import traits
from player_history import selected_traits, selected_habitat
class Caretakers:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty_list.get(specialty, {})
#specialty increases an animals attribute values
specialty_list = {
    "Terrestrial": {
        "temperature": 10,
        "terrestrial": 20
    },
    "Aquatic": {
        "temperature": 5,
        "aqueous": 15,
        "elevation": -5
    },
    "Mountaineer": {
        "temperature": -10,
        "elevation": 20
    },
    "Hot climate": {
        "temperature": 30,
        "aqueous": -10
    },
    "Cold climate": {
        "temperature": -30,
        "terrestrial": -10
    }}
#adding to animal attributes
def add_specialty_to_animal(animal, specialty):
    for attr, value in specialty.items():
        if hasattr(animal, attr):
            setattr(animal, attr, getattr(animal, attr) + value)