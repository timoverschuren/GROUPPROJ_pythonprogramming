import class_animals
import class_habitat
import slope
import tree_visualization

traits: dict = getattr(class_animals, "traits", {})
habitats: dict = getattr(class_habitat, "habitats", {})

# Player choices
selected_traits: list[str] = []      # grows with player picks
selected_habitat: str | None = None  # single choice

def get_player_habitat() -> None:
    """Handles player's habitat choice."""
    global selected_habitat

    print("Available habitats:")
    for name in habitats.keys():
        print(f" - {name}")

    choice = input("Select habitat: ").strip()
    # normalize capitalization to match your dictionary keys
    choice = choice.capitalize()

    if choice in habitats:
        selected_habitat = choice
        print(f"Selected habitat: {selected_habitat}")
    else:
        print("Invalid choice. Please try again.")


def get_player_traits() -> None:
    """Handles adding one trait to the player's history."""
    global selected_traits

    print("Available traits:")
    for name in traits.keys():
        print(f" - {name}")

    choice = input("Select trait: ").strip()
    choice = choice.capitalize()

    if choice in traits:
        selected_traits.append(choice)
        print(f"Added trait: {choice}")
        refresh_screen()  # auto update visuals
    else:
        print("Invalid choice. Please try again.")


def refresh_screen() -> None:
    """Clears the view and redraws the tree and slope."""
    print("\n" * 5)

    # Use raw selected trait *names*
    trait_names = selected_traits.copy()

    # Extract numeric trait values
    trait_values = [
        traits[t]["value"]
        for t in trait_names
        if t in traits and "value" in traits[t]
    ]

    # Only set a habitat name if selected
    habitat_name = selected_habitat if selected_habitat else "Unknown"

    # --- Render ---
    tree_visualization.render_tree(trait_names, habitat_name)

    slope.render_slope_comparison(
        selected_traits=trait_names,   # list of trait names
        habitat_name=habitat_name,     # name only
    )
