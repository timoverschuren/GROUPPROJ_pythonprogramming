import class_animals
import class_habitat
import slope
import tree_visualization

# Expected:
# class_animals.traits = { "TraitName": {"value": <number>, ...}, ... }
# class_habitat.habitats = { "HabitatName": {"value": <number>, ...}, ... }

traits: dict = getattr(class_animals, "traits", {})
habitats: dict = getattr(class_habitat, "habitats", {})


# Player choices
selected_traits: list[str]= []
# This list will grow as the player picks traits
selected_habitat: str | None = None
# This will hold the habitat the player chose

def get_player_habitat() -> None:
    """ Handles the player's habitat choice."""
    global selected_habitat
    global habitats
    print(f"Available habitats:")
    for name in habitats.keys():
        print(f" - {name}")
    choice = input("Select habitat: ").strip().lower()
    choice = choice.capitalize()
    if choice in habitats:
        selected_habitat = choice
        print(f"Selected habitat: {selected_habitat}")
    else:
        print("Invalid choice. Please try again.")

def get_player_traits() -> None:
    """ Handles the player's trait choice (adds one trait at a time)."""
    global selected_traits
    global traits
    print(f"Available traits:")
    for name in traits.keys():
        print(f" - {name}")

    choice = input("Select trait: ").strip().lower()
    choice = choice.capitalize()
    if choice in traits:
        selected_traits.append(choice) # Pushes choices to list
        print(f"Added trait: {choice}")
        refresh_screen() # Automatically triggers visuals after update
    else:
        print("Invalid choice. Please try again.")

def refresh_screen() -> None:
    """ Clears the view and redraws the tree and slope."""
    print("\n" * 5)
    # Builds the habitat curve if available; else default to flat line of mean=0
    habitat_name = selected_habitat or "Unknown habitat"
    habitat_curve = []
    if selected_habitat and selected_habitat in habitats:
        habitat_curve = habitats[selected_habitat].get("target_curve", [])

    # Extract numeric values for selected traits (missing keys are ignored)
    trait_values = [traits[t]["value"] for t in selected_traits if t in traits and "value" in traits[t]]

    # Render plots
    tree_visualization.render_tree(selected_traits, habitat_name)
    slope.render_slope_comparison(
        selected_traits=selected_traits,
        habitat_curve=habitat_curve,
        habitat_name=habitat_name,
    )

