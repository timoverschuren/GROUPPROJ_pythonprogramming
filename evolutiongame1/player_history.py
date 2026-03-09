import class_animals
import class_habitat
import slope
import tree_visualization

traits = class_animals.traits

selected_traits = []             # List[tuple(category, trait)]
selected_habitat = None          # string


def get_player_habitat():
    global selected_habitat

    print("\nAvailable habitats:")
    for h in class_habitat.habitats:
        print(f" - {h}")

    choice = input("Select habitat: ").strip().lower()

    selected_habitat = next((h for h in class_habitat.habitats if h.lower() == choice), None)

    if selected_habitat:
        print(f"Selected habitat: {selected_habitat}")
    else:
        print("Invalid habitat.")


def get_player_traits():
    global selected_traits

    print("\nTrait categories:")
    for category in traits:
        print(f" - {category}")

    cat_input = input("Select category: ").strip().lower()
    category = next((c for c in traits if c.lower() == cat_input), None)

    if category is None:
        print("Invalid category.")
        return

    print(f"\nOptions for {category}:")
    for t in traits[category]:
        print(f" - {t}")

    t_input = input("Select trait: ").strip().lower()
    trait = next((t for t in traits[category] if t.lower() == t_input), None)

    if trait is None:
        print("Invalid trait.")
        return

    selected_traits.append((category, trait))

    print(f"Added: ({category}, {trait})")
    refresh_screen()


def refresh_screen():
    print("\n" * 5)

    trait_tuples = selected_traits.copy()
    habitat_name = selected_habitat if selected_habitat else "Unknown"

    tree_visualization.render_tree(trait_tuples, habitat_name)
    slope.render_slope_comparison(trait_tuples, habitat_name)
