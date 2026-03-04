# Evolution Simulation Game

Course: PRA2031 - Python Programming Language  
Date: P4 2026  

Team Members:  
Céleste Constans  
Ivet Georgieva  
Timo Verschuren  
Kristofer Katisko  
Kian Jongen  

---

## Overview

Evolution Simulation Game is a Python-based evolutionary game where players (caretakers) create species by selecting biological traits.

Each species develops an environmental profile based on selected traits, which is then compared to a chosen habitat to calculate its survival fitness.

After defining a species by picking one trait per category and choosing a habitat, the caretaker has to change one of the traits to simulate evolution, trying to increase the species’ fitness and its general health (representing its population state).

The game simulates evolution utilising:

- Environmental parameter database
- Trait-based species construction
- Mathematical fitness evaluation
- Fitness-based health system
- Generation iterator

---

## Structure

evolutiongame1

│  
├── Evolutiongame.py  
├── class_animals.py  
├── class_caretaker.py  
├── class_habitat.py  
├── evolutiongame_methods.py  
├── player_history.py  
├── slope.py  
└── tree_visualization.py  

---

## Core Concepts

Each species is defined by:
- One trait per category
- Changing over generations with an XP cost
- A computed environmental profile defined by the chosen traits
- A fitness score based on the selected habitat

The environmental model is based on five parameters.

Environmental Parameters:

-------------------------------------------------
Parameter        | Scale
-------------------------------------------------
Temperature      | 0.0 – 50.0
Humidity         | 0.0 – 100.0
Elevation        | 0.0 – 100.0
Terrestrial      | 0.0 – 100.0 (ratio with aqueous)
Aqueous          | 0.0 – 100.0 (ratio with terrestrial)
-------------------------------------------------

Each habitat has predefined environmental values.

Species health (survival) is determined by the distance between the species environmental means and habitat conditions — in other words, fitness.

---

## Game Loop

The game is based on a loop mechanic, going on as follows:

- Define caretaker
- Select habitat for species
- Choose traits to create species (costs XP)
- Display species details (chosen traits, fitness, and health status)
- Iterate new generation by making a trait change (evolve) and displaying evolved details (possible XP gain)
- If one species dies, create another if enough XP
- Restart the game if all species go extinct (Game Over)

---

## Install and Run the Project

Python 3.10+ is required.

Open a terminal (this can also be done inside Visual Studio Code) and navigate to the folder where you would like the project to be installed.

If you have Git installed, run:

git clone https://github.com/timoverschuren/GROUPPROJ_pythonprogramming.git  
cd GROUPPROJ_pythonprogramming  

To start the game, from inside the project directory, run:

python Evolutiongame.py

---

## Design Philosophy

This project is based on the following guidelines:

- Mathematical clarity
- Trait changes over generations
- Balanced environmental habitat modeling
- Evolution of health through generations and caretaker choices

These guidelines allow the game to be simple while remaining engaging and educational.

---

## Future Improvements

Possible extensions:

- Proto → Advanced trait development levels
- Interacting traits
- Weighted trait importance
- Random mutation mechanics inside the species’ population
- Reproduction probability based on fitness
- Population mechanics (advanced health system)
- Available resources and climate systems
- Self-generating habitat method
- Habitat migration system
- Species interaction system

---

## Contribution Guidelines

To contribute:

1. Fork repository
2. Create a feature branch
3. Commit changes
4. Submit pull request

Please maintain:

- Clean object-oriented structure
- Consistent environmental parameter usage for habitat and trait creation

---

## Contributions

All group members contributed to every aspect of the project, but on different scales depending on their knowledge and interest.

Main contributions:

- Evolutiongame.py: Timo
- class_animals.py: Ivet and Kian
- class_caretaker.py: Kristofer and Timo
- evolutiongame_methods.py: Timo
- player_history.py: Céleste and Ivet
- slope.py: Ivet
- tree_visualization.py: Ivet
- README: Kian

---

Evolution Simulation Game
